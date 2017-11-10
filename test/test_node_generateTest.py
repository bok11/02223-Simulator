# -*- coding: utf-8 -*-
    
import unittest
from app.node_generateTest import GenerateTest 

class testGenerateTest(unittest.TestCase):
    
    def setUp(self):
        self.generate = GenerateTest()
    
    def test_generator_shape(self):
        distfactor = 0.5
        n_rows = 1000
        result = self.generate.generateTest(distfactor,n_rows).shape[0]
        expected = 1000
        self.assertEqual(expected, result)
    
    def test_generator_distribution(self):
        distfactor = 0.5
        n_rows = 10000
        result = round(float(self.generate.generateTest(distfactor,n_rows).
                             value_counts(normalize=True)[0],2))
        expected = distfactor
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()