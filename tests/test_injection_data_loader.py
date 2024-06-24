import os
import pathlib
import unittest
import pandas as pd
import injections.injections as injections


class TestInjection(unittest.TestCase):
    @ classmethod  # this method is run once before all tests
    def setUpClass(cls):
        cls.injection_object = injections.Injection(
            0, [0.5, 1.0, 1.5], [0.75, 0.55, 0.25])

    def test_get_location(self):
        """
        Test that the program can get the location of an injection
        """
        result = self.injection_object.get_location()

        correct_result = 0

        self.assertEqual(result, correct_result)

    def test_get_times(self):
        """
        Test that the program can get the times of an injection
        """
        result = self.injection_object.get_times()

        correct_result = [0.5, 1.0, 1.5]

        self.assertEqual(result, correct_result)

    def test_get_magnitudes(self):
        """
        Test that the program can get the magnitudes of an injection
        """
        result = self.injection_object.get_magnitudes()

        correct_result = [0.75, 0.55, 0.25]

        self.assertEqual(result, correct_result)


class TestDataLoaderFactory(unittest.TestCase):
    @ classmethod  # this method is run once before all tests
    def setUpClass(cls):
        times = [0, 2.4]

        mag_load = [[0.086794321, 0.366951104, 0.383578175],
                    [0.092492049, 0.634158432, 0.472140819]]

        cls.load_df = pd.DataFrame(mag_load,
                                   index=times,
                                   columns=[0, 1, 2])

        cls.load_df.index.name = "Time"

        os.makedirs("test_input_files")

        cls.load_df.to_csv("test_input_files/load_injections.csv")

    def test_get_data_loader(self):
        """
        Test that the program can get a data loader
        """
        data_loader_factory = injections._DataLoaderFactory()

        result = data_loader_factory._get_data_loader(
            "csv", "test_input_files/load_injections.csv")

        correct_result = injections._CSVDataLoader(
        )._load_data("test_input_files/load_injections.csv")

        self.assertEqual(result, correct_result)

    def test_get_data_loader_error(self):
        """
        Test that the program can raise an error when an unsupported data loader is requested
        """
        data_loader_factory = injections._DataLoaderFactory()

        self.assertRaises(ValueError, data_loader_factory._get_data_loader,
                          "jpeg", "test_input_files/load_injections.csv")

    @ classmethod
    def tearDownClass(cls):  # this method is run once after all tests
        os.remove("test_input_files/load_injections.csv")
        os.rmdir("test_input_files")


class TestCSVDataLoader(unittest.TestCase):
    @ classmethod  # this method is run once before all tests
    def setUpClass(cls):
        times = [0, 2.4]

        mag_load = [[0.086794321, 0.366951104, 0.383578175],
                    [0.092492049, 0.634158432, 0.472140819]]

        cls.load_df = pd.DataFrame(mag_load,
                                   index=times,
                                   columns=[0, 1, 2])

        cls.load_df.index.name = "Time"

        os.makedirs("test_input_files")

        cls.load_df.to_csv("test_input_files/load_injections.csv")

    def test_set_data_path(self):
        """
        Test that the program can set the data path
        """
        data_loader = injections._CSVDataLoader()

        data_loader._set_data_path("test_input_files/load_injections.csv")

        result = data_loader.data_path

        correct_result = pathlib.Path(os.path.abspath(
            "test_input_files/load_injections.csv"))

        self.assertEqual(result, correct_result)

    def test_load_data(self):
        """
        Test that the program can load data
        """
        data_loader = injections._CSVDataLoader()

        result = data_loader._load_data(
            "test_input_files/load_injections.csv")

        correct_result = [injections.Injection(0, [0, 2.4], [0.086794321, 0.092492049]),
                          injections.Injection(
                              1, [0, 2.4], [0.366951104, 0.634158432]),
                          injections.Injection(
                              2, [0, 2.4], [0.383578175, 0.472140819])]

        self.assertEqual(result, correct_result)

    def test_add_injection(self):
        """
        Test that the program can add an injection
        """
        data_loader = injections._CSVDataLoader()

        data_loader._add_injection(
            injections.Injection(0, [0.5, 1.0, 1.5], [0.75, 0.55, 0.25]))

        result = data_loader.injections

        correct_result = [injections.Injection(
            0, [0.5, 1.0, 1.5], [0.75, 0.55, 0.25])]

        self.assertEqual(result, correct_result)

    @ classmethod
    def tearDownClass(cls):
        os.remove("test_input_files/load_injections.csv")
        os.rmdir("test_input_files")

if __name__ == '__main__':
    unittest.main()
