import csv
import pathlib  # import pathlib
import pandapower as pp  # import pandapower
import py_dss_interface  # import py dss interface
from py_dss_interface import DSS
import os  # import os

class PowerflowSimulator():
    
    """This is a conceptual class representing the basic structure for the power flow adapters

    :param network: Common network element to be simulated
    :type network: class:`Network.Network`
    :param injections: Common injection element that stores time data regarding loads and generators
    :type injection: class:'injections.Injection'
    """
    
    
    def __init__(self, network, injections):
        self.network = network
        self.injections = injections
        self.panda_power_adapter = PandaPowerAdapter(network, injections) #Why would power flow simulator hold subclasses of itself? Seems like the wrong place to make the translators
        self.open_dss_adapter = OpenDSSAdapter(network, injections)

    def _translate_network(self):
        pass

    def _translate_injections(self):
        pass

    def run_power_flow(self, type):
        if type == 'balanced':
            self.panda_power_adapter.run_power_flow()
        elif type == 'unbalanced':
            self.open_dss_adapter.run_power_flow()
        else:
            print("Invalid power flow type")

    def get_results(self, type):
        if type == 'balanced':
            self.panda_power_adapter.get_results()
        elif type == 'unbalanced':
            self.open_dss_adapter.get_results(type='voltage')
        else:
            print("Invalid power flow type")


class PandaPowerAdapter(PowerflowSimulator):
    
    """Converts from the common network to PandaPower networks and solves using Pandapower simulations

    :param network: Common network element to be simulated
    :type network: class:`Network.Network`
    :param injections: Common injection element that stores time data regarding loads and generators
    :type injection: class:'injections.Injection'
    """

    def __init__(self, network, injections):
        self.network = network  # common network object
        self.injections = injections  # injections object
        self.net = pp.create_empty_network()  # pandapower network object

    #update translate_network whenever network class is updated to hold actual network elements instead of just dictionaries
    def translate_network(self):

        for bus in self.network.net['bus']:
            
            pp.create_bus(self.net,name = bus["name"], vn_kv = bus["vn_kv"],type = bus["type"],zone=bus["zone"])

        print(self.net.bus)

        for line in self.network.net['line']:

            pp.create_line_from_parameters(self.net, from_bus=line["from_bus_id"], to_bus=line["to_bus_id"], length_km=line["length_km"], name=line["name"],index=line["id"],r_ohm_per_km=line["r_ohm_per_km"],x_ohm_per_km=line["x_ohm_per_km"],c_nf_per_km=line["c_nf_per_km"],max_i_ka=line["max_amp"],)

        print(self.net.line)   
            
        for load in self.network.net['load']:
            
            pp.create_load(self.net,name=load["name"], bus=load["bus_id"],p_mw= (load["p_kw"])*1000 )

        print(self.net.load)

        for trafo in self.network.net['transformer']:

            pp.create_transformer_from_parameters(self.net, hv_bus=trafo["hv_bus_id"], lv_bus=trafo["lv_bus_id"], name=trafo["name"], sn_mva=(trafo["sn_kva"]/1000), vn_hv_kv=trafo["hv_kv"], vn_lv_kv=trafo["lv_kv"], vk_percent=trafo["vk_percent"], vkr_percent=trafo["vkr_percent"], pfe_kw=trafo["pfe_kw"], i0_percent=trafo["i0_percent"])

        print(self.net.trafo)

        for generator in self.network.net['generator']:

            pp.create.create_gen(self.net,name=generator["name"], bus=generator["bus_id"], p_mw= generator["p_kw"])

        print(self.net.gen)


        """
        for switch in self.network.net['switch']:
        
            # (et) element type: “l” = switch between bus and line, “t” = switch between bus and transformer, “b” = switch between two buses

            pp.create.create_switch(self.net,bus=switch["bus_id"],et=switch["type"],element = 1)

        """

        #TEMP - check for all network elements

        return

    def translate_injections(self):
        pass

    def run_power_flow(self, net=None, algorithm='nr', calculate_voltage_angles=True, init="auto",
                       max_iteration="auto", tolerance_mva=1e-8, trafo_model="t",
                       trafo_loading="current", enforce_q_lims=False, check_connectivity=True,
                       voltage_depend_loads=True, consider_line_temperature=False,
                       run_control=False, distributed_slack=False, tdpf=False, tdpf_delay_s=None, power_system="balanced", **kwargs):

        # run balanced power flow
        pp.runpp(net=self.net, algorithm=algorithm, calculate_voltage_angles=calculate_voltage_angles, init=init,
                 max_iteration=max_iteration, tolerance_mva=tolerance_mva, trafo_model=trafo_model,
                 trafo_loading=trafo_loading, enforce_q_lims=enforce_q_lims, check_connectivity=check_connectivity,
                 voltage_depend_loads=voltage_depend_loads, consider_line_temperature=consider_line_temperature,
                 run_control=run_control, distributed_slack=distributed_slack, **kwargs)

    def get_results(self):
        print(self.net.res_bus)
        return self.net.res_bus  # , self.net.res_line, self.net.res_trafo


class OpenDSSAdapter(PowerflowSimulator):

    """Converts from the common network to PandaPower networks and solves using Pandapower simulations

    :param network: Common network element to be simulated
    :type network: class:`Network.Network`
    :param injections: Common injection element that stores time data regarding loads and generators, defaults to None
    :type injections: class:'injections.Injection', optional
    """

    def __init__(self, network, injections):
        self.script_path = os.path.dirname(os.path.dirname(os.path.abspath(
            __file__)))  # get path of parent directory

        self.network = network  # common network object

        self.injections = injections  # injections object

        self.out_dir = pathlib.Path(self.script_path).joinpath(
            "output_files")  # path to output directory

        self.results = pathlib.Path(self.out_dir).joinpath(
            "results.csv")  # path to dss file

        self.net = pathlib.Path(self.out_dir).joinpath(
            "OpenDSS.dss")  # path to dss file

        # Tommy - Was having trouble creating this object, not sure if its code related or how my VScode is setup. unneeded for translate network
        # self.dss = py_dss_interface.DSS()  # create dss object

        with open(self.net, "w") as file:
            file.write("Clear\n")  # clear dss file

            # Mock external grid. TO-DO: Implement external grid in network data structure
            file.write(
                f"new circuit.0\n")
            file.write(
                f"~ basekv=110 pu=1.02 phases=3 ")
            file.write(f"bus1=0\n")

    def translate_network(self):
        """Translate network elements to OpenDSS format
        """

        with open(self.net, "a") as file:
            # pandas to OpenDSS translator
            """ for ext_grid in self.network.net["ext_grid"]:
                file.write(
                    f"new circuit.{idx}\n")
                file.write(
                    f"~ basekv={self.network.bus.iloc[ext_grid.bus].vn_kv} pu={ext_grid.vm_pu} phases=3 ")
                file.write(f"bus1={ext_grid.bus}\n") """

            for load in self.network.net["load"]:
                file.write(
                    f"new load.{load['id']} bus1={load['bus_id']} phases=3 kw={load['p_kw']} kvar={load['q_kvar']}")

                if self.injections:
                    file.write(f" daily=load.{load['id']}\n")
                else:
                    file.write("\n")

            for gen in self.network.net['generator']:
                file.write(
                    f"new generator.{gen['id']} bus1={gen['bus_id']} phases=3 kw={gen['p_kw']} kvar={gen['q_kvar']}")

                if self.injections:
                    file.write(f" daily=generator.{gen['id']}\n")
                else:
                    file.write("\n")

            for trafo in self.network.net['transformer']:
                # LoadLoss and NoLoadLoss are placeholders. TO-DO: Use Pandapower docs to calculate them properly
                # This is hard-coded to 150 deg at the moment. TO-DO: Implement phase shifter functionality
                file.write(
                    f"new transformer.{trafo['id']} phases=3 windings=2 %LoadLoss={trafo['vk_percent']} ")
                file.write(
                    f"%NoLoadLoss={trafo['vkr_percent']} LeadLag=Lead\n")
                file.write(
                    f"~ wdg=1 bus={trafo['hv_bus_id']}.1.2.3 conn=wye kv={trafo['hv_kv']} kva={trafo['sn_kva']}\n")
                file.write(
                    f"~ wdg=2 bus={trafo['lv_bus_id']}.2.3.1 conn=delta kv={trafo['lv_kv']} kva={trafo['sn_kva']}\n")

            for line in self.network.net['line']:
                file.write(
                    f"new line.{line['id']} bus1={line['from_bus_id']} bus2={line['to_bus_id']} length={line['length_km']} phases=3 ")
                file.write(
                    f"R1={line['r_ohm_per_km']} X1={line['x_ohm_per_km']} C1={line['c_nf_per_km']} ")
                file.write(f"Normamps={line['norm_amp']}\n")

            if self.injections:
                # mock monitor for timeseries simulation
                file.write(
                    f"new monitor.load.1 element=load.1 terminal=1\n")
                # setup timeseries simulation
                file.write(f"set mode=daily\n")
                file.write(f"set stepsize=2.4h\n")
                # number of timesteps
                file.write(
                    f"set number=10\n")

            # set bus voltages
            file.write("set voltagebases=[")
            for bus in self.network.net['bus']:
                file.write(f"{bus['vn_kv']} ")
            file.write("]\n")

            file.write(f"set datapath=\"{self.out_dir}\"\n")

    def translate_injections(self):
        """Translate injections to OpenDSS format
        """
        with open(self.net, "a") as file:
            for idx, load in self.injections['load'].items():
                file.write(
                    f"new loadshape.load.{idx+1} npts={len(self.injections['load'].index)}\n")
                file.write(f"mult={load.values.tolist()}\n")

            for idx, gen in self.injections['generator'].items():
                file.write(
                    f"new loadshape.generator.{idx+1} npts={len(self.injections['generator'].index)}\n")
                file.write(f"mult={gen.values.tolist()}\n")

    def run_power_flow(self):
        """Run power flow simulation
        """
        self.dss = py_dss_interface.DSS()  # Marko: needed for results
        self.dss.text(f"compile [{self.net}]")
        """ print(self.dss.lines.first())
        print(self.dss.lines.length) """
        self.dss.text("solve")

    def get_results(self, type):
        """Get power flow simulation results

        :param type: results to get (voltage)
        :type type: string
        :return: results
        :rtype: list
        """
        # self.dss.text("Show Voltages")
        # self.dss.text("Show Voltages LN Nodes")
        # self.dss.text("Export Monitor load.1")
        # file.write(f"plot loadshape Object=load.0\n")

        file = open(self.results, "wb")  # clear the results file
        file.close()

        with open(self.results, 'w', newline='') as myfile:

            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

            if 'bus' in type:
                wr.writerow(self.dss.circuit.buses_vmag)
            if 'nodes1' in type:
                wr.writerow(self.dss.circuit.nodes_vmag_by_phase(1))
            if 'nodes2' in type:
                wr.writerow(self.dss.circuit.nodes_vmag_by_phase(2))
            if 'nodes3' in type:
                wr.writerow(self.dss.circuit.nodes_vmag_by_phase(3))

            return self.dss.circuit.buses_vmag
