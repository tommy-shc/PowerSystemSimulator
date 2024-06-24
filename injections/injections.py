"""A module to model injections in power systems.
"""

import pathlib
import os
from abc import ABC, abstractmethod  # import abstract base class
import pandas as pd
from dataclasses import dataclass


class _DataLoaderFactory:
    def _get_data_loader(self, data_loader_name, data_path):

        if data_loader_name == 'csv':
            data_loader = _CSVDataLoader()

        else:
            raise ValueError(f"Data loader {data_loader_name} not supported")

        injections = data_loader._load_data(data_path)
        return injections


@dataclass  # one way to generate a method to test the equality of object values
class Injections(_DataLoaderFactory):
    """Set of injection objects

    :param load_injections: List of load injection objects to represent loads, defaults to None
    :type load_injections: List, optional
    :param generator_injections: List of injection objects to represent generators, defaults to None
    :type generator_injections: List, optional
    """

    def __init__(self, load_injections=None, generator_injections=None):
        self.injections = {
            "load": load_injections,
            "generator": generator_injections
        }

    def load(self, data_loader_name, directory):
        """Loads the injection data using the specified data_loader_name from the specified directory

        :param data_loader_name: File type to load the data from (csv)
        :type data_loader_name: string
        :param directory: relative path (from the folder where the code is run) to the directory containing the injection data
        :type directory: string
        """
        data_loader_factory = _DataLoaderFactory()

        self.injections["load"] = data_loader_factory._get_data_loader(
            data_loader_name, f"{directory}/load_injections.csv")

        self.injections["generator"] = data_loader_factory._get_data_loader(
            data_loader_name, f"{directory}/generator_injections.csv")

    # custom because need a different dataframe structure than the Injection class would imply
    def to_dataframe(self):
        """Converts the injections to a pandas dataframe

        :return: Injection data as a dictionary of pandas dataframes named "load" and "generator"
        :rtype: Dictionary of pandas dataframes
        """
        load_df = pd.DataFrame()

        load_df.index.name = "Time"

        for injection in self.injections["load"]:
            for time, magnitude in zip(injection.get_times(), injection.get_magnitudes()):
                load_df.at[time, injection.get_location()] = magnitude

        generator_df = pd.DataFrame()

        generator_df.index.name = "Time"

        for injection in self.injections["generator"]:
            for time, magnitude in zip(injection.get_times(), injection.get_magnitudes()):
                generator_df.at[time, injection.get_location()] = magnitude

        return {
            "load": load_df,
            "generator": generator_df
        }


# To-do: discuss whether this is necessary or if just the dataframe is enough
@dataclass  # one way to generate a method to test the equality of object values
class Injection:
    """Class for injections at a single location
    """

    def __init__(self, location, times, magnitudes):
        """Creates an injection object

        :param location: Location of the injection
        :type location: int
        :param times: List of times for the injection
        :type times: list
        :param magnitudes: List of magnitudes for the injection
        :type magnitudes: list
        """
        self.location = location
        self.times = times
        self.magnitudes = magnitudes

    def get_location(self):
        """Returns the location of the injection

        :return: Location
        :rtype: int
        """
        return self.location

    def get_times(self):
        """Returns the times of the injection

        :return: Times
        :rtype: list
        """
        return self.times

    def get_magnitudes(self):
        """Returns the magnitudes of the injection

        :return: Magnitudes
        :rtype: list
        """
        return self.magnitudes


@ dataclass
class _DataLoader(ABC):
    @ abstractmethod
    def __init__(self):
        self.injections = []  # list of injection objects
        self.data_path = None

    @ abstractmethod
    def _set_data_path(self, data_path):
        script_path = os.path.dirname(os.path.dirname(os.path.abspath(
            __file__)))  # get path of parent directory

        data_folder_name, data_file_name = data_path.split("/")

        self.data_path = pathlib.Path(script_path).joinpath(
            data_folder_name, data_file_name)  # path to injections folder

    @ abstractmethod
    def _load_data(self):
        pass

    @ abstractmethod
    def _add_injection(self, injection):
        self.injections.append(injection)


class _CSVDataLoader(_DataLoader):
    def __init__(self):
        super().__init__()

    def _set_data_path(self, data_path):
        super()._set_data_path(data_path)

    def _load_data(self, data_path):
        self._set_data_path(data_path)
        injections_df = pd.read_csv(self.data_path)

        for _, col in injections_df.items():
            if col.name == 'Time':
                times = injections_df['Time']
            else:
                # location, times, magnitudes
                injection = Injection(
                    int(_), times.to_list(), col.to_list())
                self._add_injection(injection)

        return self.injections

    def _add_injection(self, injection):
        super()._add_injection(injection)
