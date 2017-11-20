#%%
import numpy as np
import pandas as pd
from app.node import Node

class Network(object):
    n_nodes = 0
    nodes = []
    status = pd.DataFrame([])
    
    def __init__(self, n_nodes):
        '''Sets up a network of n nodes with 4 sensors'''
        self.n_nodes = n_nodes

        for _ in range(self.n_nodes):
            self.nodes.append(Node(n_sensors=4, handicap=1))

    def step(self):
        for node in 


