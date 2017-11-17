# -*- coding: utf-8 -*-
#%%
import unittest
import numpy as np
from app.node import Node

class testNode(unittest.TestCase):
    
    def setUp(self):
        self.node = Node(n_sensors=1, handicap=1)

    def test_panel_charge(self):
        '''Test solar panel charging'''
        result = self.node.charge(month=3)
        expected = 0.004875
        variance = 0.0005
        self.assertTrue(result >= expected - variance and result <= expected + variance)

    def test_uptimestep(self):
        '''Test system uptime over n iterations'''
        iterations = 50
        for _ in range(iterations):
            self.node.step(sensor_values=[1], month=1)
        result = self.node.uptime
        self.assertEqual(iterations, result)

    def test_energy_depletion(self):
        '''At every timestep, energy level should change'''
        self.node.step(sensor_values=[1], month=1)
        first = self.node.energy_left
        self.node.step(sensor_values=[1], month=1)
        second = self.node.energy_left        
        diff = first - second
        self.assertNotEqual(0, diff)
    
    def test_sensor_readings(self):
        '''Tests that sensor_read() returns values of correct length'''
        values = self.node.sensors_read()
        n_val = len(values)
        self.assertEqual(n_val, self.node.n_sensors)
    
    def test_not_alive(self):
        '''Tests that nodes can lose their alive state'''
        self.node.discharge(self.node.energy_left + 10)
        self.node.step(sensor_values=[1], month=1)
        self.assertEqual(self.node.alive, 0)
    
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
