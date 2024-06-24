import networks.network as network
import injections.injections as injections
from translators import PandaPowerAdapter
from translators import OpenDSSAdapter
import translators as p



class Main():  #Do we need a specific main class to specify these methods?
    def __init__(self):
        self.networks = []
        self.injections = []

    def load_network(self):
        new_network = network.Network()
        self.networks.append(new_network)
        return new_network

    def load_injections(self):
        new_injections = injections.Injections()
        self.injections.append(new_injections)
        return new_injections


def main():
    power_system_sim = Main()
    # Test network with manual input
    # --------------------------------------------------------
    test_network1 = power_system_sim.load_network()

    # add elements
    bus1 = network.Bus("Bus1", 110.0, "b", "Zone1", 1.05, 0.95, True)
    bus2 = network.Bus("Bus2", 110.0, "b", "Zone2", 1.05, 0.95, True)
    test_network1.add_bus(bus1)
    test_network1.add_bus(bus2)

    line1 = network.Line("Line1", 0, 1, 10.0, 80.0, 0.1, 0.2,
                         100.0, 0.1, 0.2, 100.0, 200.0, 250.0, 1, 0.9, 3,"ol")
    test_network1.add_line(line1)

    load1 = network.Load("Load1", 0, 50.0, 30.0, 0.4, 50.0,
                         0.0, 0.0, True, 55.0, 45.0, 35.0, 25.0)
    test_network1.add_load(load1)

    transformer1 = network.Transformer("Transformer1", 0, 1, 110.0, 20.0,
                                       1000.0, 6.0, 0.5, 1.0, 2.0, -2, 0, 2, 1.25, 0.01, 0.02, 0.01)
    test_network1.add_transformer(transformer1)

    generator1 = network.Generator("Gen1", 0, 60.0, 20.0, 0.4,
                                   60.0, 1.0, True, 65.0, 55.0, 25.0, 15.0, 3, 0.02)
    test_network1.add_generator(generator1)

    '''

    # Convert to pandas dataframes
    dfs1 = test_network1.to_dataframe()

    #display dataframe results 
    for df_name, df in dfs1.items():
        print(f"{df_name} :")
        print(df)

    test_network1.save_to_csv()


    print("\n\n\n\n")



    # Test network with csv file input
    # --------------------------------------------------------
    test_network2 = power_system_sim.load_network()

    test_network2.load_from_csv()

    # Convert to pandas dataframes
    dfs2 = test_network2.to_dataframe()

    # display dataframe results
    
    for df_name, df in dfs2.items():
        print(f"{df_name} :")
        print(df)


    new_injections = None  # power_system_sim.load_injections()

    #sim = p.PowerflowSimulator(dfs, new_injections)
    #sim.run_power_flow(type='unbalanced')
    #sim.get_results(type='unbalanced')

    # Test translators
    # ---------------------------
    
    '''
    
    new_injections = None

    ptrans = PandaPowerAdapter(test_network1, new_injections)

    #otrans = OpenDSSAdapter(test_network1,new_injections)

    ptrans.translate_network()

    #otrans.translate_network()
    
    condition = True
        

    print("Hello World")




main()
