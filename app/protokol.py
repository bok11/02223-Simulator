# -*- coding: utf-8 -*-

class Protokol(object):
    
    def calcBits(self,n_nodes,n_sensors):
        
        if n_nodes is 1:
            base = 52
            result = base+n_sensors
            
        
        else:
            base = 52
            result = base+n_sensors
            
            for nodes in range(n_nodes-1):
                base = 8
                result += base+n_sensors
            
        return result