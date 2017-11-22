#%%
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from app.node import Node


class Network(object):
    n_nodes = 0
    nodes = []
    clusters = []
    cluster_masters = []
    nodes_alive = 0
    graphs = ""
#    status = pd.DataFrame([])

    def __init__(self, n_nodes, handicap, random_max):
        '''Sets up a network of n nodes with m sensors, random: handicap, auto id from 1'''
        self.n_nodes = n_nodes
        self.nodes_alive = n_nodes

        for i in range(self.n_nodes):
            self.nodes.append(Node(n_sensors=4, handicap=handicap - random.uniform(0, random_max), node_id=i+1))

    def show_alive(self):
        '''Returns Histogram over alive nodes'''
        pd.DataFrame([node.alive for node in self.nodes]).hist()

    def show_energy(self):
        pd.DataFrame([node.energy_left for node in self.nodes]).hist()

    def cluster_nodes(self, n_clusters):
        '''[node group][node number in group]'''
        cluster_size = int(self.n_nodes / n_clusters)        
#        picklist = np.arange(self.n_nodes)
        picklist = np.array(self.nodes)
        np.random.shuffle(picklist)
        picklist = picklist.reshape((n_clusters, cluster_size))
        self.clusters = picklist

    def calculate_sender(self):
        '''Selects the unit with most power available for sending'''
        self.cluster_masters = []
        for i in range(len(self.clusters)):
            energy_levels = [node.energy_left for node in self.clusters[i]]
#            print("Cluster: {}\tMax: {}\tIndex in cluster: {}"
#                  .format(i, max(energy_levels), energy_levels.index(max(energy_levels))))
            self.cluster_masters.append(energy_levels.index(max(energy_levels)))

    def show_cluster_energy_left(self):
        data = [[sum(node.energy_left.tolist()) for node in nodes] for nodes in self.clusters] # Ugly hack


#        pd.DataFrame(data).hist(figsize=(10,9.5))
        sns.heatmap(data).set(xlabel='Node Index', ylabel='Cluster Index', title='Energy left in nodes')
        plt.show()

    def show_cluster_alive(self):
        data = [[node.alive for node in nodes] for nodes in self.clusters] # Ugly hack
        sns.heatmap(data).set(xlabel='Node Index', ylabel='Cluster Index', title='Node alive')
        plt.show()
        
    def show_cluster_uptime(self):
        data = [[node.uptime for node in nodes] for nodes in self.clusters] # Ugly hack
        sns.heatmap(data, annot=True).set(xlabel='Node Index', ylabel='Cluster Index', title='Node uptime')
        plt.show()
    
    def show_cluster_status(self, filename):
        fig, ax = plt.subplots(1,2, figsize=(10,4))
        fig.suptitle('Iteration: {}'.format(filename))
        data_energy = [[float(node.energy_left) for node in nodes] for nodes in self.clusters]
        data_alive = [[node.alive for node in nodes] for nodes in self.clusters]
        alive = [node_alive for nodes in data_alive for node_alive in nodes].count(1)
        sns.heatmap(data_energy, ax=ax[0]).set(xlabel='Node Index', ylabel='Cluster Index', title='Energy left in nodes')
        sns.heatmap(data_alive, ax=ax[1]).set(xlabel='Node Index', ylabel='Cluster Index', title='Nodes alive: {}/{} ({}%)'.format(alive, self.n_nodes, round(alive/self.n_nodes*100, 2)))
        self.graphs = self.graphs + '''<center><img src="{}.png" /></center>'''.format(filename, filename)
        plt.savefig("{}.png".format(filename))        
        plt.show()
    
#        print("Nodes alive: {}".format([node_alive for nodes in data_alive for node_alive in nodes].count(1)))
        
    def step(self, month):
        '''System gets all sensor values and send all values, subtracts energy'''

        # Function to read sensor values
        
        # Discharge all masters - THIS IS JUST FOR DEBUGGING AND TESTING!!!
        for cluster_index, node_index in enumerate(self.cluster_masters):
            self.clusters[cluster_index][node_index].discharge(2)
#            print(cluster_index, node_index)

        # Step all nodes (and update alive status)
        [[node.step([0,0,0,0], month) for node in nodes] for nodes in self.clusters]
        
    def write(self):
        '''Generates full html report for dataset'''
        with open(f"simulation_report.html", 'w') as file:
            file.write('''
<html>
    <head>
        <title>Simulation Report</title>
    </head>
        <body>
        <center><h1>Something</h1></center>
        This is an auto-generated dataset report!
        <h2>Something report</h2>
        {}
        </body>
</html>
                       '''.format(self.graphs))

if __name__ == '__main__':
    '''Init'''
    myNet = Network(n_nodes=225, handicap=0.01, random_max=0.005)
    myNet.cluster_nodes(n_clusters=15)

    '''Simulation runs'''
    for iteration in range(5):
        myNet.calculate_sender()
        myNet.show_cluster_status(iteration)
        for timestep in range(1440):    # 1440 minutes in a day
            myNet.step(5)
        myNet.write()
#    myNet.show_cluster_uptime()

