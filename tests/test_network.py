import os
import pandas as pd
import unittest
from networks.network import Network
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

class TestNetwork(unittest.TestCase):

    maxDiff = None

    @classmethod  # this method is run once before all tests
    def setUpClass(cls):

        cls.testnet = Network()

        bus1 = Bus("Bus1", 110.0, "b", "Zone1", 1.05, 0.95, True)
        bus2 = Bus("Bus2", 110.0, "b", "Zone2", 1.05, 0.95, True)
        bus3 = Bus("Bus3", 110.0, "b", "Zone2", 1.05, 0.95, True)
        cls.testnet.net["bus"].append(bus1.to_dict())
        cls.testnet.net["bus"].append(bus2.to_dict())
        cls.testnet.net["bus"].append(bus3.to_dict())

        line1 = Line("Line1", 1, 2, 10.0, 80.0, 0.1, 0.2, 100.0, 0.1, 0.2, 100.0, 200.0, 250.0, 1, 0.9, 3,"ol")
        line2 = Line("Line2", 2, 3, 10.0, 80.0, 0.1, 0.2, 100.0, 0.1, 0.2, 100.0, 200.0, 250.0, 1, 0.9, 3,"ol")
        cls.testnet.net["line"].append(line1.to_dict())
        cls.testnet.net["line"].append(line2.to_dict())

        load1 = Load("Load1", 2, 50.0, 30.0, 0.4, 50.0, 0.0, 0.0, True, 55.0, 45.0, 35.0, 25.0)
        cls.testnet.net["load"].append(load1.to_dict())

        switch1 = Switch("Switch1", 1, "CB", True, 80.0, 45.0)
        cls.testnet.net["switch"].append(switch1.to_dict())

        transformer1 = Transformer("Transformer1", 1, 2, 110.0, 20.0, 1000.0, 6.0, 0.5, 1.0, 2.0, -2, 0, 2, 1.25, 0.01, 0.02, 0.01)
        cls.testnet.net["transformer"].append(transformer1.to_dict())

        generator1 = Generator("Gen1", 2, 60.0, 20.0, 0.4, 60.0, 1.0, True, 65.0, 55.0, 25.0, 15.0, 3, 0.02)
        cls.testnet.net["generator"].append(generator1.to_dict())

        storage1 = Storage("Storage1", 1, 3.4, 2.0, 4.0, 1.0, 2.3, 5.0, 3.0, 5.0, 0.5)
        cls.testnet.net["storage"].append(storage1.to_dict())
        
        impedence1 = Impedence("Impedence1", 2, 3, 4.0, 3.5, 8.0, 2.3)
        cls.testnet.net["impedence"].append(impedence1.to_dict())

        threewindingtransformer1 = ThreeWindingTransformer(name="TWTransformer1", hv_bus_id=101, mv_bus_id=102, lv_bus_id=103, hv_kv=110.0, mv_kv=33.0, lv_kv=11.0, sn_hv_kva=10000.0, sn_mv_kva=8000.0, sn_lv_kva=5000.0, vk_hv_percent=10.5, vk_mv_percent=11.0, vk_lv_percent=12.0, vkr_hv_percent=1.2, vkr_mv_percent=1.5, vkr_lv_percent=1.8, pfe_kw=50.0, i0_percent=0.5, tap_min=-10, tap_neutral=0, tap_max=10, tap_step_percent=1.25, rh=0.01, rm=0.015, rl=0.02, xh=0.05, xm=0.07, xl=0.09)
        cls.testnet.net["threewindingtransformer"].append(threewindingtransformer1.to_dict())


        cls.bus_df = pd.DataFrame(cls.testnet.net["bus"])
        cls.line_df = pd.DataFrame(cls.testnet.net["line"])
        cls.load_df = pd.DataFrame(cls.testnet.net["load"])
        cls.transformer_df = pd.DataFrame(cls.testnet.net["transformer"])
        cls.generator_df = pd.DataFrame(cls.testnet.net["generator"])
        cls.impedence_df = pd.DataFrame(cls.testnet.net["impedence"])
        cls.storage_df = pd.DataFrame(cls.testnet.net["storage"])
        cls.switch_df = pd.DataFrame(cls.testnet.net["switch"])
        cls.threewindingtransformer_df = pd.DataFrame(cls.testnet.net["threewindingtransformer"])


        os.makedirs("network_data")

        cls.bus_df.to_csv("network_data/bus.csv")
        cls.line_df.to_csv("network_data/line.csv")
        cls.load_df.to_csv("network_data/load.csv")
        cls.transformer_df.to_csv("network_data/transformer.csv")
        cls.generator_df.to_csv("network_data/generator.csv")
        cls.impedence_df.to_csv("network_data/impedence.csv")
        cls.storage_df.to_csv("network_data/storage.csv")
        cls.switch_df.to_csv("network_data/switch.csv")
        cls.threewindingtransformer_df.to_csv("network_data/threewindingtransformer.csv")


    def test_add_bus(self):
        """tests if a bus can be added to a network
        """
        result = Network()
        bus = Bus("Bus", 110.0, "b", "Zone1", 1.05, 0.95, True)
        result.add_bus(bus)

        expected_result = {"bus": [{'name': 'Bus', 'id': 4, 'vn_kv': 110.0, 'type': 'b', 'zone': 'Zone1', 'max_vm_pu': 1.05, 'min_vm_pu': 0.95, 'in_service': True}],
                            "line": [],
                            "load": [],
                            "transformer": [],
                            "generator": [],
                            "impedence": [],
                            "storage": [],
                            "switch": [],
                            "threewindingtransformer": []}

        self.assertEqual(result.net, expected_result)
    
    def test_add_line(self):
        """tests if a line can be added to a network
        """
        result = Network()
        line = Line("Line", 1, 2, 10.0, 80.0, 0.1, 0.2, 100.0, 0.1, 0.2, 100.0, 200.0, 250.0, 1, 0.9, 3)
        result.add_line(line)

        expected_result = {"bus": [],
                            "line": [{'name': 'Line', 'id': 3, 'from_bus_id': 1, 'to_bus_id': 2, 'length_km': 10.0, 'max_loading_percent': 80.0, 'r_ohm_per_km': 0.1, 'x_ohm_per_km': 0.2, 'c_nf_per_km': 100.0, 'r0_ohm_per_km': 0.1, 'x0_ohm_per_km': 0.2, 'c0_nf_per_km': 100.0, 'norm_amp': 200.0, 'max_amp': 250.0, 'num_parallel': 1, 'derating_factor': 0.9, 'phases': 3}],
                            "load": [],
                            "transformer": [],
                            "generator": [],
                            "impedence": [],
                            "storage": [],
                            "switch": [],
                            "threewindingtransformer": []}

        self.assertEqual(result.net, expected_result)
    
    def test_add_load(self):
        """tests if a load can be added to a network
        """
        result = Network()
        load = Load("Load", 2, 50.0, 30.0, 0.4, 50.0, 0.0, 0.0, True, 55.0, 45.0, 35.0, 25.0)
        result.add_load(load)

        expected_result = {"bus": [],
                            "line": [],
                            "load": [{'name': 'Load', 'id': 2, 'bus_id': 2, 'p_kw': 50.0, 'q_kvar': 30.0, 'kv': 0.4, 'kva': 50.0, 'const_z_percent': 0.0, 'const_i_percent': 0.0, 'fixed': True, 'max_p_kw': 55.0, 'min_p_kw': 45.0, 'max_q_kvar': 35.0, 'min_q_kvar': 25.0}],
                            "transformer": [],
                            "generator": [],
                            "impedence": [],
                            "storage": [],
                            "switch": [],
                            "threewindingtransformer": []}

        self.assertEqual(result.net, expected_result)
    
    def test_add_transformer(self):
        """tests if a transformer can be added to a network
        """
        result = Network()
        transformer = Transformer("Transformer", 1, 2, 110.0, 20.0, 1000.0, 6.0, 0.5, 1.0, 2.0, -2, 0, 2, 1.25, 0.01, 0.02, 0.01)
        result.add_transformer(transformer)

        expected_result = {"bus": [],
                            "line": [],
                            "load": [],
                            "transformer": [{'name': 'Transformer', 'id': 2, 'hv_bus_id': 1, 'lv_bus_id': 2, 'hv_kv': 110.0, 'lv_kv': 20.0, 'sn_kva': 1000.0, 'vk_percent': 6.0, 'vkr_percent': 0.5, 'pfe_kw': 1.0, 'i0_percent': 2.0, 'tap_min': -2, 'tap_neutral': 0, 'tap_max': 2, 'tap_step_percent': 1.25, 'rh': 0.01, 'rl': 0.02, 'x': 0.01}],
                            "generator": [],
                            "impedence": [],
                            "storage": [],
                            "switch": [],
                            "threewindingtransformer": []}

        self.assertEqual(result.net, expected_result)
    
    def test_add_generator(self):
        """tests if a generator can be added to a network
        """
        result = Network()
        generator = Generator("Generator", 2, 60.0, 20.0, 0.4, 60.0, 1.0, True, 65.0, 55.0, 25.0, 15.0, 3, 0.02)
        result.add_generator(generator)

        expected_result = {"bus": [],
                            "line": [],
                            "load": [],
                            "transformer": [],
                            "generator": [{'name': 'Generator', 'id': 2, 'bus_id': 2, 'p_kw': 60.0, 'q_kvar': 20.0, 'kv': 0.4, 'kva': 60.0, 'pvfactor': 1.0, 'fixed': True, 'max_p_kw': 65.0, 'min_p_kw': 55.0, 'max_q_kvar': 25.0, 'min_q_kvar': 15.0, 'phases': 3, 'subtrans_react_pu': 0.02}],
                            "impedence": [],
                            "storage": [],
                            "switch": [],
                            "threewindingtransformer": []}

        self.assertEqual(result.net, expected_result)

    def test_add_impedence(self):
        """tests if an impedence can be added to a network
        """
        result = Network()
        impedence = Impedence("Impedence", 2, 3, 4.0, 3.5, 8.0, 2.3)
        result.add_impedence(impedence)

        expected_result = {"bus": [],
                            "line": [],
                            "load": [],
                            "transformer": [],
                            "generator": [],
                            "impedence": [{'name': 'Impedence', 'id': 2, 'from_bus_id': 2, 'to_bus_id': 3, 'r_pu': 4.0, 'x_pu': 3.5, 'kv': 8.0, 'kvar': 2.3}],
                            "storage": [],
                            "switch": [],
                            "threewindingtransformer": []}

        self.assertEqual(result.net, expected_result)
    
    def test_add_storage(self):
        """tests if a storage can be added to a network
        """
        result = Network()
        storage = Storage("Storage", 1, 3.4, 2.0, 4.0, 1.0, 2.3, 5.0, 3.0, 5.0, 0.5)
        result.add_storage(storage)

        expected_result = {"bus": [],
                            "line": [],
                            "load": [],
                            "transformer": [],
                            "generator": [],
                            "impedence": [],
                            "storage": [{'name': 'Storage', 'id': 2, 'bus_id': 1, 'p_kw': 3.4, 'p_kvar': 2.0, 'max_e_kwh': 4.0, 'min_e_kwh': 1.0, 'soc_percent': 2.3, 'max_p_mv': 5.0, 'min_p_kw': 3.0, 'max_q_mvar': 5.0, 'min_q_kvar': 0.5}],
                            "switch": [],
                            "threewindingtransformer": []}

        self.assertEqual(result.net, expected_result)

    def test_add_switch(self):
        """tests if a switch can be added to a network
        """
        result = Network()
        switch = Switch("Switch", 1, "CB", True, 80.0, 45.0)
        result.add_switch(switch)

        expected_result = {"bus": [],
                            "line": [],
                            "load": [],
                            "transformer": [],
                            "generator": [],
                            "impedence": [],
                            "storage": [],
                            "switch": [{'name': 'Switch', 'id': 2, 'bus_id': 1, 'type': 'CB', 'closed': True, 'base_freq': 80.0, 'max_ka': 45.0}],
                            "threewindingtransformer": []}

        self.assertEqual(result.net, expected_result)

    def test_add_threewindingtransformer(self):
        """tests if a threewindingtransformer can be added to a network
        """
        result = Network()
        threewindingtransformer = ThreeWindingTransformer(name="TWTransformer", hv_bus_id=101, mv_bus_id=102, lv_bus_id=103, hv_kv=110.0, mv_kv=33.0, lv_kv=11.0, sn_hv_kva=10000.0, sn_mv_kva=8000.0, sn_lv_kva=5000.0, vk_hv_percent=10.5, vk_mv_percent=11.0, vk_lv_percent=12.0, vkr_hv_percent=1.2, vkr_mv_percent=1.5, vkr_lv_percent=1.8, pfe_kw=50.0, i0_percent=0.5, tap_min=-10, tap_neutral=0, tap_max=10, tap_step_percent=1.25, rh=0.01, rm=0.015, rl=0.02, xh=0.05, xm=0.07, xl=0.09)
        result.add_threewindingtransformer(threewindingtransformer)

        expected_result = {"bus": [],
                            "line": [],
                            "load": [],
                            "transformer": [],
                            "generator": [],
                            "impedence": [],
                            "storage": [],
                            "switch": [],
                            "threewindingtransformer": [{'name': 'TWTransformer', 'id': 2, 'hv_bus_id': 101, 'mv_bus_id': 102, 'lv_bus_id': 103, 'hv_kv': 110.0, 'mv_kv': 33.0, 'lv_kv': 11.0, 'sn_hv_kva': 10000.0, 'sn_mv_kva': 8000.0, 'sn_lv_kva': 5000.0, 'vk_hv_percent': 10.5, 'vk_mv_percent': 11.0, 'vk_lv_percent': 12.0, 'vkr_hv_percent': 1.2, 'vkr_mv_percent': 1.5, 'vkr_lv_percent': 1.8, 'pfe_kw': 50.0, 'i0_percent': 0.5, 'tap_min': -10, 'tap_neutral': 0, 'tap_max': 10, 'tap_step_percent': 1.25, 'rh': 0.01, 'rm': 0.015, 'rl': 0.02, 'xh': 0.05, 'xm': 0.07, 'xl': 0.09}]}

        self.assertEqual(result.net, expected_result)
    
    def test_bus_to_dataframe(self):
        """tests if the program can convert the network buses to a pandas dataframe
        """
        result = self.testnet.to_dataframe()["bus"]

        expected_result = self.bus_df
        
        pd.testing.assert_frame_equal(result, expected_result)

    def test_line_to_dataframe(self):
        """tests if the program can convert the network lines to a pandas dataframe
        """
        result = self.testnet.to_dataframe()["line"]

        expected_result = self.line_df
        
        pd.testing.assert_frame_equal(result, expected_result)

    def test_load_to_dataframe(self):
        """tests if the program can convert the network loads to a pandas dataframe
        """
        result = self.testnet.to_dataframe()["load"]

        expected_result = self.load_df
        
        pd.testing.assert_frame_equal(result, expected_result)
    
    def test_transformer_to_dataframe(self):
        """tests if the program can convert the network transformers to a pandas dataframe
        """
        result = self.testnet.to_dataframe()["transformer"]

        expected_result = self.transformer_df
        
        pd.testing.assert_frame_equal(result, expected_result)

    def test_generator_to_dataframe(self):
        """tests if the program can convert the network generators to a pandas dataframe
        """
        result = self.testnet.to_dataframe()["generator"]

        expected_result = self.generator_df
        
        pd.testing.assert_frame_equal(result, expected_result)
    
    def test_impedence_to_dataframe(self):
        """tests if the program can convert the network impedences to a pandas dataframe
        """
        result = self.testnet.to_dataframe()["impedence"]

        expected_result = self.impedence_df
        
        pd.testing.assert_frame_equal(result, expected_result)

    def test_storage_to_dataframe(self):
        """tests if the program can convert the network storages to a pandas dataframe
        """
        result = self.testnet.to_dataframe()["storage"]

        expected_result = self.storage_df
        
        pd.testing.assert_frame_equal(result, expected_result)

    def test_switch_to_dataframe(self):
        """tests if the program can convert the network switches to a pandas dataframe
        """
        result = self.testnet.to_dataframe()["switch"]

        expected_result = self.switch_df
        
        pd.testing.assert_frame_equal(result, expected_result)
     
    def test_threewindingtransformer_to_dataframe(self):
        """tests if the program can convert the network lines to a pandas dataframe
        """
        result = self.testnet.to_dataframe()["threewindingtransformer"]

        expected_result = self.threewindingtransformer_df
        
        pd.testing.assert_frame_equal(result, expected_result)

    def test_save_to_csv(self):
        """test if the network data can be exported to csv files
        """
        self.testnet.save_to_csv(directory="test_network_data1")

        for element in self.testnet.net.keys():
            result_file_path = os.path.join("test_network_data1", f"{element}.csv")
            self.assertTrue(os.path.isfile(result_file_path)) # Check if each file was created

            # load the CSV file and compare it with the original element DataFrame
            result_df = pd.read_csv(result_file_path)
            expected_df = pd.DataFrame(self.testnet.net[element])
            pd.testing.assert_frame_equal(result_df, expected_df)

    def test_load_from_csv(self):
        """
        test if the program can load in network data
        """
        self.testnet.save_to_csv(directory="test_network_data2")

        result = Network()
        result.load_from_csv(directory = "test_network_data2")
    
        # convert network dictionaries to DataFrames, excluding "id" column because each new element created generates a new id
        result_dfs = {f"{key}": pd.DataFrame(result.net[f"{key}"]).drop(columns=["id"]) for key in result.net.keys()}
        expected_dfs = {f"{key}": pd.DataFrame(self.testnet.net[f"{key}"]).drop(columns=['id']) for key in self.testnet.net.keys()}

        # check that the loaded network matches the original network
        for key in self.testnet.net.keys():
            pd.testing.assert_frame_equal(result_dfs[f"{key}"], expected_dfs[f"{key}"])
        
        
    @classmethod  # this method is run once after all tests
    def tearDownClass(cls):
        os.remove("network_data/switch.csv")
        os.remove("network_data/bus.csv")
        os.remove("network_data/line.csv")
        os.remove("network_data/load.csv")
        os.remove("network_data/transformer.csv")
        os.remove("network_data/generator.csv")
        os.remove("network_data/impedence.csv")
        os.remove("network_data/storage.csv")
        os.remove("network_data/threewindingtransformer.csv")
        os.rmdir("network_data")

        os.remove("test_network_data1/switch.csv")
        os.remove("test_network_data1/bus.csv")
        os.remove("test_network_data1/line.csv")
        os.remove("test_network_data1/load.csv")
        os.remove("test_network_data1/transformer.csv")
        os.remove("test_network_data1/generator.csv")
        os.remove("test_network_data1/impedence.csv")
        os.remove("test_network_data1/storage.csv")
        os.remove("test_network_data1/threewindingtransformer.csv")
        os.rmdir("test_network_data1")

        os.remove("test_network_data2/switch.csv")
        os.remove("test_network_data2/bus.csv")
        os.remove("test_network_data2/line.csv")
        os.remove("test_network_data2/load.csv")
        os.remove("test_network_data2/transformer.csv")
        os.remove("test_network_data2/generator.csv")
        os.remove("test_network_data2/impedence.csv")
        os.remove("test_network_data2/storage.csv")
        os.remove("test_network_data2/threewindingtransformer.csv")
        os.rmdir("test_network_data2")




if __name__ == '__main__': 
    unittest.main() #in order to run tests through terminal