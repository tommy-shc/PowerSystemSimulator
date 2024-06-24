import os
import unittest
import pandas as pd
import injections.injections as injections


class TestInjections(unittest.TestCase):
    @classmethod  # this method is run once before all tests
    def setUpClass(cls):
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

        cls.injections_object = injections.Injections([injections.Injection(
            0, times, [row[0] for row in mag_load]),
            injections.Injection(
            1, times, [row[1] for row in mag_load]),
            injections.Injection(
            2, times, [row[2] for row in mag_load])],
            [injections.Injection(
                0, times, [row[0] for row in mag_generator]),
             injections.Injection(
                1, times, [row[1] for row in mag_generator]),
             injections.Injection(
                2, times, [row[2] for row in mag_generator])])

        cls.load_df = pd.DataFrame(mag_load,
                                   index=[0.0, 2.4, 4.8, 7.2, 9.6,
                                          12.0, 14.4, 16.8, 19.2, 21.6],
                                   columns=[0, 1, 2])

        cls.load_df.index.name = "Time"

        cls.generator_df = pd.DataFrame(mag_generator,
                                        index=[0.0, 2.4, 4.8, 7.2, 9.6,
                                               12.0, 14.4, 16.8, 19.2, 21.6],
                                        columns=[0, 1, 2])

        cls.generator_df.index.name = "Time"

        os.makedirs("test_input_files")

        cls.load_df.to_csv("test_input_files/load_injections.csv")
        cls.generator_df.to_csv("test_input_files/generator_injections.csv")

    def test_load(self):
        """
        Test that the program can load in data
        """
        result = injections.Injections()

        result.load("csv", "test_input_files")

        correct_result = injections.Injections(load_injections=injections._DataLoaderFactory()._get_data_loader(
            'csv', "test_input_files/load_injections.csv"),
            generator_injections=injections._DataLoaderFactory()._get_data_loader('csv', "test_input_files/load_injections.csv"))

        self.assertEqual(result, correct_result)

    def test_loads_to_dataframe(self):
        """
        Test that the program can convert load injections to a dataframe
        """
        result = self.injections_object.to_dataframe()["load"]

        correct_result = self.load_df

        pd.testing.assert_frame_equal(result, correct_result)

    def test_generators_to_dataframe(self):
        """
        Test that the program can convert generator injections to a dataframe
        """
        result = self.injections_object.to_dataframe()["generator"]

        correct_result = self.generator_df

        pd.testing.assert_frame_equal(result, correct_result)

    @ classmethod
    def tearDownClass(cls):  # this method is run once after all tests
        os.remove("test_input_files/load_injections.csv")
        os.remove("test_input_files/generator_injections.csv")
        os.rmdir("test_input_files")


if __name__ == '__main__':
    unittest.main()
