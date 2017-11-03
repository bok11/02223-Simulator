# -*- coding: utf-8 -*-

import unittest
from app.node import Node

class testNode(unittest.TestCase):
 
    def setUp(self):
        self.node = Node(1,1)
    
    def test_timestep(self):
        self.node.step({1},1)
        result = self.node.uptime
        self.assertEqual(1, result)
    
    def test_charge(self):
        result = self.node.charge(4)
        self.assertEqual(15,result)
    
    def test_calc_power_usage(self):
        result = self.node.calculate_power_sensors({1})
        self.assertEqual(0.6,result)
        
    def test_calculate_power_send_data(self):
        result = self.node.calculate_power_send_data()
        self.assertEqual(0.0001855, result)

if __name__ == '__main__':
    unittest.main()
