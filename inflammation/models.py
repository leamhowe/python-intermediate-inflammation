"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
import json
import glob
import os

def load_csv(filename):  
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array."""
    return np.min(data, axis=0)


def load_json(filename):
    """Read a JSON file and return its contents as a Python object."""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
    

class CSVDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir

        # self.data = self.load_data()
        # self.daily_means = self.calculate_daily_means()
        # self.standard_deviation = self.calculate_standard_deviation()

    def load_data(self):
        """ Load data from given list of file paths. """
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.csv'))

        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation CSV files found in path {self.data_dir}")
        data = map(load_csv, data_file_paths)
        return list(data)


class JSONDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_data(self):
        """ Load data from given list of file paths. """
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'inflammation*.json'))

        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation JSON files found in path {self.data_dir}")
        data = map(load_json, data_file_paths)
        return list(data)
    

def calculate_daily_means(data):
    """ Calculate daily mean values for loaded data. """
    means_by_day = map(daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    return means_by_day_matrix

def calculate_standard_deviation(daily_means):
    """ Calculate the standard deviation of daily mean values. """
    means_matrix = np.stack(daily_means)
    return np.std(means_matrix, axis=0)