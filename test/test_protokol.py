# -*- coding: utf-8 -*-

# målet er at undersøge at tiden der mellem hver sending , er under 120 sekunder

import unittest
from app.protokol import Protokol

class TestProtokol(unittest.TestCase):
 
    def setUp(self):
        self.prot = Protokol()
    
    def test_bits_1node4sensors(self):
        n_nodes =  1
        n_sensors = 4
        result = self.prot.calcBits(n_nodes,n_sensors)
        expected = 56
        self.assertEqual(expected, result)
        
        
    def test_bits_3node4sensors(self):
        n_nodes =  3
        n_sensors = 4
        result = self.prot.calcBits(n_nodes,n_sensors)
        expected = 80
        self.assertEqual(expected, result)
        

    def test_bits_12node1sensors(self):
        n_nodes =  12
        n_sensors = 1
        result = self.prot.calcBits(n_nodes,n_sensors)
        expected = 152
        self.assertEqual(expected, result)
        
if __name__ == '__main__':
    unittest.main()