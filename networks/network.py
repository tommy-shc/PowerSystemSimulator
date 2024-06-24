import pandas as pd
import os


from networks.Element import Element
from networks.Bus import Bus
from networks.Line import Line
from networks.Load import Load
from networks.Transformer import Transformer
from networks.Generator import Generator
from networks.Impedence import Impedence
from networks.Storage import Storage
from networks.Switch import Switch
from networks.ThreeWindingTransformer import ThreeWindingTransformer


# Marko: IDs are currently unique across all networks (eg. if network 1 has lines
# with IDs 1, 2, 3, network 2's lines would start numbering at 4). Is this useful
# so that elements can be easily moved between networks, or should each network
# have IDs starting at 1 for each element type?
class Network:
    """
    A class to represent a network of power system elements.
    """
    def __init__(self):
        """
        Initialize the network as a dictionary composed of empty lists for each type of element.
        """
        self.net = {
            "bus": [],
            "line": [],
            "load": [],
            "transformer": [],
            "generator": [],
            "impedence": [],
            "storage": [],
            "switch": [],
            "threewindingtransformer": []
        }
    def add_bus(self, Bus):
        """Add a Bus element to the network.

        :param Bus: an instance of the Bus class
        :type Bus: Bus
        """
        self.net["bus"].append(Bus.to_dict())

    def add_line(self, Line):
        """Add a Line element to the network.

        :param Line: an instance of the Line class
        :type Line: Line
        """
        self.net["line"].append(Line.to_dict())

    def add_load(self, Load):
        """Add a Load element to the network.

        :param Load: an instance of the Load class
        :type Load: Load
        """
        self.net["load"].append(Load.to_dict())

    def add_transformer(self, Transformer):
        """Add a Transformer element to the network.

        :param Transformer: an instance of the Transformer class
        :type Transformer: Transformer
        """
        self.net["transformer"].append(Transformer.to_dict())

    def add_generator(self, Generator):
        """Add a Generator element to the network.

        :param Generator: an instance of the Generator class
        :type Generator: Generator
        """
        self.net["generator"].append(Generator.to_dict())

    def add_impedence(self, Impedence):
        """Add a Impedence element to the network.

        :param Impedence: an instance of the Impedence class
        :type Impedence: Impedence
        """
        self.net["impedence"].append(Impedence.to_dict())

    def add_storage(self, Storage):
        """Add a Storage element to the network.

        :param Storage: an instance of the Storage class
        :type Storage: Storage
        """
        self.net["storage"].append(Storage.to_dict())

    def add_switch(self, Switch):
        """Add a Switch element to the network.

        :param Switch: an instance of the Switch class
        :type Switch: Switch
        """
        self.net["switch"].append(Switch.to_dict())

    def add_threewindingtransformer(self, ThreeWindingTransformer):
        """Add a ThreeWindingTransformerh element to the network.

        :param ThreeWindingTransformer: an instance of the ThreeWindingTransformer class
        :type ThreeWindingTransformer: ThreeWindingTransformer
        """
        self.net["threewindingtransformer"].append(ThreeWindingTransformer.to_dict())

    # NEXT STEPS: remove_element functions

    def to_dataframe(self):
        
        """Convert each element list in the network to a pandas DataFrame.

        :return: A dictionary of pandas DataFrames where the keys are element 
            types and the values are the corresponding DataFrames.
        :rtype: dict
        """
        
        # Convert each element list to a pandas DataFrame
        bus_df = pd.DataFrame(self.net["bus"])
        line_df = pd.DataFrame(self.net["line"])
        load_df = pd.DataFrame(self.net["load"])
        transformer_df = pd.DataFrame(self.net["transformer"])
        generator_df = pd.DataFrame(self.net["generator"])
        impedence_df = pd.DataFrame(self.net["impedence"])
        storage_df = pd.DataFrame(self.net["storage"])
        switch_df = pd.DataFrame(self.net["switch"])
        threewindingtransformer_df = pd.DataFrame(self.net["threewindingtransformer"])

        #dictionary of element DataFrames
        return { 
            "bus": bus_df,
            "line": line_df,
            "load": load_df,
            "transformer": transformer_df,
            "generator": generator_df,
            "impedence": impedence_df,
            "storage": storage_df,
            "switch": switch_df,
            "threewindingtransformer": threewindingtransformer_df,
        }

    def save_to_csv(self, directory=os.path.expanduser("~/Desktop/network_data")):
        
        """Save the network data to CSV files in the specified directory.

        This method creates the specified directory if it does not exist, and 
        saves each element of the network as a separate CSV file.

        :param directory: The directory where the CSV files will be saved, 
            defaults to "~/Desktop/network_data"
        :type directory: str, optional
        """
        
        #create directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        #save each element DataFrame to a CSV file
        dfs = self.to_dataframe()
        for key, df in dfs.items():
            df.to_csv(f"{directory}/{key}.csv", index=False)

    def load_from_csv(self, directory=os.path.expanduser("~/Desktop/network_data")):
        
        """Load the network data from CSV files in the specified directory.

        This method expects specific CSV files to be present in the directory. If a 
        file is empty or does not exist, it will be skipped with a corresponding 
        message. The loaded data will be added to the network as appropriate objects.

        :param directory: The directory from which the CSV files will be loaded, 
            defaults to "~/Desktop/network_data"
        :type directory: str, optional
        """
        
        #expected CSV files
        files = ["bus.csv", "line.csv", "load.csv", "transformer.csv", "generator.csv", "impedence.csv", "storage.csv", "switch.csv", "threewindingtransformer.csv"]
        dataframes = {}

        # check which files exists and if the file is empty
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                try:
                    df = pd.read_csv(file_path)
                    if df.empty:
                        print(f"File {file} is empty. Skipping...")
                    else:
                        dataframes[file.split('.')[0] + '_df'] = df
                except pd.errors.EmptyDataError:
                    print(f"File {file} is empty or has no columns to parse. Skipping...")
            else:
                print(f"File {file} not found in directory {directory}. Skipping...")

        # Add each element from the DataFrames to the network
        if 'bus_df' in dataframes:
            for _, row in dataframes['bus_df'].iterrows():
                bus = Bus(row['name'], row['vn_kv'], row['type'], row['zone'], row['max_vm_pu'], row['min_vm_pu'], row['in_service'])
                self.add_bus(bus)

        if 'line_df' in dataframes:
            for _, row in dataframes['line_df'].iterrows():
                line = Line(row['name'], row['from_bus_id'], row['to_bus_id'], row['length_km'], row['max_loading_percent'], row['r_ohm_per_km'], row['x_ohm_per_km'],
                            row['c_nf_per_km'], row['r0_ohm_per_km'], row['x0_ohm_per_km'], row['c0_nf_per_km'], row['norm_amp'], row['max_amp'], row['num_parallel'], row['derating_factor'], row['phases'])
                self.add_line(line)

        if 'load_df' in dataframes:
            for _, row in dataframes['load_df'].iterrows():
                load = Load(row['name'], row['bus_id'], row['p_kw'], row['q_kvar'], row['kv'], row['kva'], row['const_z_percent'], row['const_i_percent'],
                            row['fixed'], row['max_p_kw'], row['min_p_kw'], row['max_q_kvar'], row['min_q_kvar'])
                self.add_load(load)

        if 'transformer_df' in dataframes:
            for _, row in dataframes['transformer_df'].iterrows():
                transformer = Transformer(row['name'], row['hv_bus_id'], row['lv_bus_id'], row['hv_kv'], row['lv_kv'], row['sn_kva'], row['vk_percent'], row['vkr_percent'],
                                        row['pfe_kw'], row['i0_percent'], row['tap_min'], row['tap_neutral'], row['tap_max'], row['tap_step_percent'], row['rh'], row['rl'], row['x'])
                self.add_transformer(transformer)

        if 'generator_df' in dataframes:
            for _, row in dataframes['generator_df'].iterrows():
                generator = Generator(row['name'], row['bus_id'], row['p_kw'], row['q_kvar'], row['kv'], row['kva'], row['pvfactor'], row['fixed'], row['max_p_kw'],
                                    row['min_p_kw'], row['max_q_kvar'], row['min_q_kvar'], row['phases'], row['subtrans_react_pu'])
                self.add_generator(generator)

        if 'impedence_df' in dataframes:
            for _, row in dataframes['impedence_df'].iterrows():
                impedence = Impedence(row['name'], row['from_bus_id'], row['to_bus_id'], row['r_pu'], row['x_pu'], row['kv'], row['kvar'])
                self.add_impedence(impedence)

        if 'storage_df' in dataframes:
            for _, row in dataframes['storage_df'].iterrows():
                storage = Storage(row['name'], row['bus_id'], row['p_kw'], row['p_kvar'], row['max_e_kwh'], row['min_e_kwh'], row['soc_percent'], row['max_p_mv'],
                                row['min_p_kw'], row['max_q_mvar'], row['min_q_kvar'])
                self.add_storage(storage)

        if 'switch_df' in dataframes:
            for _, row in dataframes['switch_df'].iterrows():
                switch = Switch(row['name'], row['bus_id'], row['type'], row['closed'], row['base_freq'], row['max_ka'])
                self.add_switch(switch)

        if 'threewindingtransformer_df' in dataframes:
            for _, row in dataframes['threewindingtransformer_df'].iterrows():
                threewindingtransformer = ThreeWindingTransformer(row['name'], row['hv_bus_id'], row['mv_bus_id'], row['lv_bus_id'], row['hv_kv'], row['mv_kv'], row['lv_kv'], row['sn_hv_kva'],
                                                                row['sn_mv_kva'], row['sn_lv_kva'], row['vk_hv_percent'], row['vk_mv_percent'], row['vk_lv_percent'], row['vkr_hv_percent'], row['vkr_mv_percent'],
                                                                row['vkr_lv_percent'], row['pfe_kw'], row['i0_percent'], row['tap_min'], row['tap_neutral'], row['tap_max'], row['tap_step_percent'], row['rh'], row['rm'], row['rl'], row['xh'], row['xm'], row['xl'])
                self.add_threewindingtransformer(threewindingtransformer)

