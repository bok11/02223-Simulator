# -*- coding: utf-8 -*-
#%%
import unittest
from app.network import Network


class testNetwork(unittest.TestCase):
    
    def setUp(self):
        '''Sets up a network of n nodes with 4 sensors'''
        self.network = Network(n_nodes=100)
        
        
    def test_n_nodes(self):
        '''Tests that network has right amount of nodes'''
        self.assertEqual(self.network.n_nodes, 100)
"""
        
        
    def test_uptimestep(self):
        '''Test network uptime over n iterations'''
        for node in self.nodes:
            iterations = 50
            for _ in range(iterations):
                node.step(sensor_values=node.sensors_read(), month=1)
            result = node.uptime
            self.assertEqual(iterations, result)
            
    def test_network_alive(self):
        
        for node in self.nodes:
            node.discharge(node.energy_left + 10)
            node.step(sensor_values=node.sensors_read(), month=1)
    def step(self):
        '''Test solar panel charging'''
        result = self.node.charge(month=3)
        expected = 0.004875
        variance = 0.0005
        self.assertTrue(result >= expected - variance and result <= expected + variance)
"""

if __name__ == '__main__':
    unittest.main()
