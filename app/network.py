#%%
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
#    status = pd.DataFrame([])

    def __init__(self, n_nodes, random):
        '''Sets up a network of n nodes with m sensors, random: handicap, auto id from 1'''
        self.n_nodes = n_nodes

        if random == True:
            for i in range(self.n_nodes):
                self.nodes.append(Node(n_sensors=4, handicap=np.random.rand(1), node_id=i+1))

        else:
            for i in range(self.n_nodes):
                self.nodes.append(Node(n_sensors=4, handicap=1, node_id=i+1))

    def show_alive(self):
        '''Returns Histogram over alive nodes'''
        pd.DataFrame([node.alive for node in self.nodes]).hist()

    def show_energy(self):
        pd.DataFrame([node.energy_left for node in self.nodes]).hist()

    def cluster_nodes(self, n_clusters):
        '''[node group][node number in group]'''

        for _ in range(n_clusters):
            cluster_size = int(self.n_nodes / n_clusters)
            self.clusters.append(np.random.choice(self.nodes, size=cluster_size, replace=False))

    def calculate_sender(self):
        '''Selects the unit with most power available for sending'''
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

    def show_cluster_status(self):
        fig, ax = plt.subplots(1,2, figsize=(10,4))
        data_energy = [[sum(node.energy_left.tolist()) for node in nodes] for nodes in self.clusters] # Ugly hack
        data_alive = [[node.alive for node in nodes] for nodes in self.clusters] # Ugly hack
        sns.heatmap(data_energy, ax=ax[0]).set(xlabel='Node Index', ylabel='Cluster Index', title='Energy left in nodes')
        sns.heatmap(data_alive, ax=ax[1]).set(xlabel='Node Index', ylabel='Cluster Index', title='Node alive')
        plt.show()

    def step(self):
        '''System gets all sensor values and send all values, subtracts energy'''

        # Function to read sensor values

        # Discharge all masters - THIS IS JUST FOR DEBUGGING AND TESTING!!!
        for cluster_index, node_index in enumerate(self.cluster_masters):
            self.clusters[cluster_index][node_index].discharge(0)
#            print(i,value)

        # Step all nodes (and update alive status)
        for nodes in self.clusters:
            for node in nodes:
                node.step([0,0,0,0],0)




#        pass


if __name__ == '__main__':
    '''Init'''
    myNet = Network(n_nodes=100, random=1)
#    myNet.show_alive()
    print("Initial")
#    myNet.show_energy()
    myNet.cluster_nodes(n_clusters=10)
    myNet.calculate_sender()
#    myNet.show_cluster_energy_left()
#    myNet.show_cluster_alive()
    myNet.show_cluster_status()
    '''Runs'''
    for _ in range(10000):
        myNet.step()
    print("After runs")
    myNet.show_cluster_status()
#    myNet.show_cluster_energy_left()
#    myNet.show_cluster_alive()



