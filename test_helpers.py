# test_helpers.py

import unittest
from unittest.mock import patch, mock_open
from helpers import get_rate_area, get_second_lowest_silver_plan

class TestHelpers(unittest.TestCase):

    # Testing get_rate_area function -------------------------------------------------------------------------------
    
    # Simulating reading from zips.csv with one rate area for ZIP code 64148
    @patch('builtins.open', mock_open(read_data="zipcode,rate_area\n64148,1\n67118,2\n"))
    def test_get_rate_area_single_rate_area(self):
        result = get_rate_area('64148', './data/zips.csv')
        self.assertEqual(result, '1')

     # Simulating reading from zips.csv with multiple rate areas for ZIP code 64148
    @patch('builtins.open', mock_open(read_data="zipcode,rate_area\n64148,1\n64148,2\n"))
    def test_get_rate_area_multiple_rate_areas(self):
        result = get_rate_area('64148', './data/zips.csv')
        self.assertIsNone(result)  # Should return None for multiple rate areas
    
    # Simulating reading from zips.csv with no data
    @patch('builtins.open', mock_open(read_data="zipcode,rate_area\n"))
    def test_get_rate_area_no_rate_area(self):
        result = get_rate_area('64148', './data/zips.csv')
        self.assertIsNone(result)  # Should return None when no rate area is found

    # Test get_second_lowest_silver_plan function ----------------------------------------------------------------------
    
    # Simulating reading from plans.csv with two silver plans in rate_area 1
    @patch('builtins.open', mock_open(read_data="rate_area,metal_level,rate\n1,Silver,200.00\n1,Silver,150.00\n"))
    def test_get_second_lowest_silver_plan_valid(self):
        result = get_second_lowest_silver_plan('1', './data/plans.csv')
        self.assertEqual(result, 200.00)  # Second lowest plan is 200.00

    # Simulating reading from plans.csv with only one silver plan in rate_area 1
    @patch('builtins.open', mock_open(read_data="rate_area,metal_level,rate\n1,Silver,200.00\n"))
    def test_get_second_lowest_silver_plan_not_enough_plans(self):
        result = get_second_lowest_silver_plan('1', './data/plans.csv')
        self.assertIsNone(result)  # Should return None for not enough silver plans
    
    # Simulating reading from plans.csv with no silver plans
    @patch('builtins.open', mock_open(read_data="rate_area,metal_level,rate\n"))
    def test_get_second_lowest_silver_plan_no_silver_plans(self):
        result = get_second_lowest_silver_plan('1', './data/plans.csv')
        self.assertIsNone(result)  # Should return None if no silver plans are available

if __name__ == '__main__':
    unittest.main()
