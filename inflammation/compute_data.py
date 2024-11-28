"""Module containing mechanism for calculating standard deviation between datasets.
"""

from inflammation import models, views


def analyse_data(data_source):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""

    # _, extension = os.path.splitext(infiles[0])
    # if extension == '.json':
    #     data_source = JSONDataSource(os.path.dirname(infiles[0]))
    # elif extension == '.csv':
    #     data_source = CSVDataSource(os.path.dirname(infiles[0]))
    # else:
    #     raise ValueError(f'Unsupported data file format: {extension}')
    # analyse_data(data_source)
    # data_source = CSVDataSource(data_dir)
    data = data_source.load_data()

    daily_means = models.calculate_daily_means(data)
    standard_deviation = models.calculate_standard_deviation(daily_means)
    return standard_deviation

def plot_data(standard_deviation):
    views.visualize({'standard deviation by day': standard_deviation})


