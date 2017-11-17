# -*- coding: utf-8 -*-
#%%

import unittest
from app.energyharvest import EnergyHarvest 

class testEnergyHarvest(unittest.TestCase):

    def setUp(self):
        self.panel = EnergyHarvest()

    def test_panel_charge(self):
        result = self.panel.charge(panel_size=0.3, efficiency=0.2, month=3)
        expected = 0.007
        variance = 0.001
        self.assertTrue(result >= expected - variance and result <= expected + variance)
        #self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()