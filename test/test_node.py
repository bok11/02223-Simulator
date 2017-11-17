# -*- coding: utf-8 -*-
#%%
import unittest
import numpy as np
from app.node import Node

class testNode(unittest.TestCase):

    def setUp(self):
        self.node = Node(n_sensors=1, handicap=1)

    def test_panel_charge(self):
        result = self.node.charge(month=3)
        expected = 0.004875
        variance = 0.0005
        self.assertTrue(result >= expected - variance and result <= expected + variance)

    def test_timestep(self):
        self.node.step(sensor_values=[1], month=1)
        result = self.node.uptime
        self.assertEqual(1, result)
    
    """
    def test_calc_power_usage(self):
        result = self.node.calculate_power_sensors({1})
        self.assertEqual(0.6,result)
    
    def test_calculate_power_send_data(self):
        result = self.node.calculate_power_send_data()
        self.assertEqual(0.0001855, result)
    """
if __name__ == '__main__':
    unittest.main()
