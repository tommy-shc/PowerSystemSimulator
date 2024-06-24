import unittest
import pandas as pd
import pandapower as pp
from translators import PandaPowerAdapter
import networks.network as network

class TestPandaPowerAdapter(unittest.TestCase):
    
    def test_translate_network(self):
        #Tests for common network translation into PandaPower Network
        
        self.test_net = network.Network()

        # add elements
        bus1 = network.Bus("Bus1", 110.0, "b", "Zone1", 1.05, 0.95, True)
        bus2 = network.Bus("Bus2", 110.0, "b", "Zone2", 1.05, 0.95, True)
        self.test_net.add_bus(bus1)
        self.test_net.add_bus(bus2)

        line1 = network.Line("Line1", 0, 1, 10.0, 80.0, 0.1, 0.2,100.0, 0.1, 0.2, 100.0, 200.0, 250.0, 1, 0.9, 3,"ol")
        self.test_net.add_line(line1)

        load1 = network.Load("Load1", 0, 50.0, 30.0, 0.4, 50.0,
                            0.0, 0.0, True, 55.0, 45.0, 35.0, 25.0)
        self.test_net.add_load(load1)

        transformer1 = network.Transformer("Transformer1", 0, 1, 110.0, 20.0,
                                        1000.0, 6.0, 0.5, 1.0, 2.0, -2, 0, 2, 1.25, 0.01, 0.02, 0.01)
        self.test_net.add_transformer(transformer1)

        generator1 = network.Generator("Gen1", 0, 60.0, 20.0, 0.4,
                                    60.0, 1.0, True, 65.0, 55.0, 25.0, 15.0, 3, 0.02)
        self.test_net.add_generator(generator1)
            
        #TODO Add Injections
    
        ptrans = PandaPowerAdapter(self.test_net, None)
        ptrans.translate_network()
        
        condition = True
        
        result =  pp.create_empty_network()
        
        pp.create_bus(result,name="Bus1",vn_kv=110.0, type="b", zone ="Zone1",in_service=True)
        pp.create_bus(result,name="Bus2",vn_kv=110.0, type="b", zone ="Zone2",in_service=True)
        
        pp.create_line_from_parameters(result, from_bus=0, to_bus=1, length_km=10, name="Line1",index=2,r_ohm_per_km=0.1,x_ohm_per_km=0.2,c_nf_per_km=100,max_i_ka=250)
        
        pp.create_load(result,name="Load1", bus=0,p_mw= 50000)
        
        pp.create_transformer_from_parameters(result, hv_bus=0, lv_bus=1, name="Transformer1", sn_mva=1, vn_hv_kv=110, vn_lv_kv=20, vk_percent=6, vkr_percent=0.5, pfe_kw=1, i0_percent=2)
        
        pp.create.create_gen(result,name="Gen1", bus=0, p_mw= 60)
        
        print(result.bus)
        print(result.line)
        print(result.load)
        print(result.trafo)
        print(result.gen)
        
        condition = pp.nets_equal(ptrans.net,result)

        self.assertTrue(condition)
        
if __name__ == '__main__':
    unittest.main()