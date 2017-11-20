# -*- coding: utf-8 -*-
#%%
import unittest
import numpy as np
from app.network import Network


class testNetwork(unittest.TestCase):
    '''Main test cases for non random network'''

    def setUp(self):
        '''Sets up a network of n nodes with 4 sensors'''
        self.network = Network(n_nodes=100, random=0)


    def test_n_nodes(self):
        '''Tests that network has right amount of nodes'''
        self.assertEqual(self.network.n_nodes, 100)

    def test_alive(self):
        '''Test initialized network has n alive nodes out of n nodes'''
        n_alive = [node.alive for node in self.network.nodes]
        self.assertEqual(n_alive.count(1), self.network.n_nodes)

        """
        CLUSTERING TESTED IN OTHER TEST CASE: POSSIBLY DEPRECATED
    def test_clustering(self):
        '''Test if nodes are put into clusters'''
        self.network.cluster_nodes(n_clusters=10)
        self.assertEqual(np.array(self.network.clusters).shape, (10,10))
        """

    def test_calculate_sender(self):
        '''Test if system can find a master for every cluster'''
        self.network.cluster_nodes(n_clusters=10)
        self.network.calculate_sender()
        self.assertEqual(np.array(self.network.clusters).shape, (10,10))
        self.assertEqual(len(self.network.cluster_masters), 10)


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
