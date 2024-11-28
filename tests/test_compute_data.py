from unittest.mock import Mock
import numpy.testing as npt
import math

def test_compute_data_mock_source():
  from inflammation.compute_data import analyse_data
  data_source = Mock()

  # TODO: configure data_source mock
  data_source.load_data.return_value = [[[0, 2, 0]], 
                                        [[0, 1, 0]]]

  result = analyse_data(data_source)

  # TODO: add assert on the contents of result
  npt.assert_array_equal(result, [0, math.sqrt(0.25), 0])

# def test_analyse_data():
#     """Test that analyse_data works for a set of data."""
#     from inflammation.compute_data import analyse_data

#     data_dir = 'data'
#     analyse_da
  
  