# -*- coding: utf-8 -*-

# målet er at undersøge at tiden der mellem hver sending , er under 120 sekunder

import unittest
from app.protokol import Protokol

class TestProtokol(unittest.TestCase):
 
    def setUp(self):
        self.prot = Protokol()
    
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2,2)
        self.assertEqual(4, result)
        
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
 
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)
 
    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
        
if __name__ == '__main__':
    unittest.main()