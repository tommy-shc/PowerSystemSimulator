import os
import pathlib
import unittest
import pandas as pd
import translators as translators
import networks.network as network


class TestOpenDSSAdapter(unittest.TestCase):
    @ classmethod  # this method is run once before all tests
    def setUpClass(cls):
        test_network1 = network.Network()

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

        times = [0, 2.4, 4.8, 7.2, 9.6, 12, 14.4, 16.8, 19.2, 21.6]

        mag_load = [[0.086794321, 0.366951104, 0.383578175],
                    [0.092492049, 0.634158432, 0.472140819],
                    [0.079156185, 0.550294247, 0.281747627],
                    [0.09792119, 0.347540235, 0.398873569],
                    [0.095376547, 0.656119491, 0.489970558],
                    [0.077146452, 0.490684693, 0.3589298],
                    [0.10462934, 0.43864901, 0.569228958],
                    [0.07386759, 0.474161804, 0.313030804],
                    [0.062817545, 0.352288159, 0.011611811],
                    [0.103289468, 0.354394112, 0.458151717]]

        mag_generator = [[0.092492049, 0.634158432, 0.72140819],
                         [0.09792119, 0.347540235, 0.398873569],
                         [0.077146452, 0.490684693, 0.3589298],
                         [0.10462934, 0.43864901, 0.569228958],
                         [0.062817545, 0.352288159, 0.011611811],
                         [0.079156185, 0.550294247, 0.281747627],
                         [0.103289468, 0.354394112, 0.458151717],
                         [0.07386759, 0.474161804, 0.313030804],
                         [0.086794321, 0.366951104, 0.383578175],
                         [0.095376547, 0.490684693, 0.489970558]]

        load_df = pd.DataFrame(mag_load,
                               index=times,
                               columns=[0, 1, 2])

        load_df.index.name = "Time"

        generator_df = pd.DataFrame(mag_generator,
                                    index=times,
                                    columns=[0, 1, 2])

        generator_df.index.name = "Time"

        injections_object = {
            "load": load_df,
            "generator": generator_df
        }

        script_path = os.path.dirname(os.path.dirname(os.path.abspath(
            __file__)))  # get path of parent directory

        if not os.path.exists("output_files"):
            os.makedirs("output_files")

        cls.out_dir = pathlib.Path(script_path).joinpath(
            "output_files")  # path to output directory

        cls.net = pathlib.Path(cls.out_dir).joinpath(
            "OpenDSS.dss")  # path to dss file

        cls.translator = translators.OpenDSSAdapter(
            test_network1, injections_object)

    def setUp(self):  # this method is run before each test
        file = open(self.net, "w")  # clear the file
        file.close()

    def test_translate_injections(self):
        """
        Test that the program can translate the injections with the OpenDSS adapter
        """

        self.translator.translate_injections()

        file = open(self.net, "r")
        result = file.readlines()
        file.close()

        correct_result = ["new loadshape.load.1 npts=10\n",
                          "mult=[0.086794321, 0.092492049, 0.079156185, 0.09792119, 0.095376547, 0.077146452, 0.10462934, 0.07386759, 0.062817545, 0.103289468]\n",
                          "new loadshape.load.2 npts=10\n",
                          "mult=[0.366951104, 0.634158432, 0.550294247, 0.347540235, 0.656119491, 0.490684693, 0.43864901, 0.474161804, 0.352288159, 0.354394112]\n",
                          "new loadshape.load.3 npts=10\n",
                          "mult=[0.383578175, 0.472140819, 0.281747627, 0.398873569, 0.489970558, 0.3589298, 0.569228958, 0.313030804, 0.011611811, 0.458151717]\n",
                          "new loadshape.generator.1 npts=10\n",
                          "mult=[0.092492049, 0.09792119, 0.077146452, 0.10462934, 0.062817545, 0.079156185, 0.103289468, 0.07386759, 0.086794321, 0.095376547]\n",
                          "new loadshape.generator.2 npts=10\n",
                          "mult=[0.634158432, 0.347540235, 0.490684693, 0.43864901, 0.352288159, 0.550294247, 0.354394112, 0.474161804, 0.366951104, 0.490684693]\n",
                          "new loadshape.generator.3 npts=10\n",
                          "mult=[0.72140819, 0.398873569, 0.3589298, 0.569228958, 0.011611811, 0.281747627, 0.458151717, 0.313030804, 0.383578175, 0.489970558]\n"]

        self.assertEqual(result, correct_result)

    def test_translate_network(self):
        """
        Test that the program can translate the network with the OpenDSS adapter
        """

        self.translator.translate_network()

        file = open(self.net, "r")
        result = file.readlines()
        file.close()

        # need the f to correct funky VS code autocolouring
        correct_result = ["new load.4 bus1=0 phases=3 kw=50.0 kvar=30.0 daily=load.4\n",
                          "new generator.4 bus1=0 phases=3 kw=60.0 kvar=20.0 daily=generator.4\n",
                          f"new transformer.4 phases=3 windings=2 %LoadLoss=6.0 %NoLoadLoss=0.5 LeadLag=Lead\n",
                          "~ wdg=1 bus=0.1.2.3 conn=wye kv=110.0 kva=1000.0\n",
                          "~ wdg=2 bus=1.2.3.1 conn=delta kv=20.0 kva=1000.0\n",
                          "new line.6 bus1=0 bus2=1 length=10.0 phases=3 R1=0.1 X1=0.2 C1=100.0 Normamps=200.0\n",
                          "new monitor.load.1 element=load.1 terminal=1\n",
                          "set mode=daily\n",
                          "set stepsize=2.4h\n",
                          "set number=10\n",
                          "set voltagebases=[110.0 110.0 ]\n",
                          f'set datapath="{self.out_dir}"\n']  # for flexiblity when test run on different machines

        self.assertEqual(result, correct_result)

    def test_get_results(self):
        """
        Test that the program can translate the network with the OpenDSS adapter
        """

        with open(self.net, "w") as file:
            file.write('Clear\nnew circuit.0\n~ basekv=110 pu=1.02 phases=3 bus1=bus1\nnew loadshape.load.0 npts=10\nmult=[0.086794321, 0.092492049, 0.079156185, 0.09792119, 0.095376547, 0.077146452, 0.10462934, 0.07386759, 0.062817545, 0.103289468]\nnew loadshape.load.1 npts=10\nmult=[0.366951104, 0.634158432, 0.550294247, 0.347540235, 0.656119491, 0.490684693, 0.43864901, 0.474161804, 0.352288159, 0.354394112]\nnew loadshape.load.2 npts=10\nmult=[0.383578175, 0.472140819, 0.281747627, 0.398873569, 0.489970558, 0.3589298, 0.569228958, 0.313030804, 0.011611811, 0.458151717]\nnew loadshape.generator.0 npts=10\nmult=[0.092492049, 0.09792119, 0.077146452, 0.10462934, 0.062817545, 0.079156185, 0.103289468, 0.07386759, 0.086794321, 0.095376547]\nnew loadshape.generator.1 npts=10\nmult=[0.634158432, 0.347540235, 0.490684693, 0.43864901, 0.352288159, 0.550294247, 0.354394112, 0.474161804, 0.366951104, 0.656119491]\nnew loadshape.generator.2 npts=10\nmult=[0.472140819, 0.398873569, 0.3589298, 0.569228958, 0.011611811, 0.281747627, 0.458151717, 0.313030804, 0.383578175, 0.489970558]\nnew load.0 bus1=Bus1 phases=3 kw=50.0 kvar=30.0 daily=load.0\nnew generator.0 bus1=Bus2 phases=3 kw=60.0 kvar=20.0 daily=generator.0\nnew transformer.0 phases=3 windings=2 %LoadLoss=6.0 %NoLoadLoss=0.5 LeadLag=Lead\n~ wdg=1 bus=Bus1.1.2.3 conn=wye kv=110.0 kva=1000.0\n~ wdg=2 bus=Bus2.2.3.1 conn=delta kv=20.0 kva=1000.0\nnew line.0 bus1=Bus1 bus2=Bus2 length=10.0 phases=3 R1=0.1 X1=0.2 C1=100.0 Normamps=200.0\nnew monitor.load.0 element=load.0 terminal=1\nset mode=daily\nset stepsize=2.4h\nset number=10\nset voltagebases=[110.0 110.0 ]\n')
            file.close()

        self.translator.run_power_flow()  # need to compile the dss file first
        result = self.translator.get_results(type="bus")[0]

        correct_result = 54440.10841596306

        # assert that the result is within 100 of the correct result b/c of floating point errors
        self.assertAlmostEqual(result, correct_result, -2)


if __name__ == '__main__':
    unittest.main()
