# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

class GenerateTest(object):
	
	def generateTest(self, p_one, n):
		'''
		Generates suitable test data for a single node
		'''
		p_zero = 1.0 - p_one
	
		return pd.Series(np.random.choice([0, 1], size=n, replace=True, p=[p_zero, p_one]))

