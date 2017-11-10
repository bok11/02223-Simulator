# -*- coding: utf-8 -*-
import math

class Protokol(object):
    
    def calcBits(self,n_nodes,n_sensors):
        
        # if only one node
        if n_nodes is 1:
            # overhead
            base = 52
            
            # overhead + sensor data
            result = base+n_sensors
            
            return result
            
        
        # if more nodes
        else:
            
            # first node
            base = 52
            result = base+n_sensors
            
            # next nodes
            for nodes in range(n_nodes-1):
                base = 8
                result += base+n_sensors
            
            return result
        
    
    def ToffAir(self,n_nodes,n_sensors):
        
        # parameters
        BW = 125*10**3
        SF = 12
        PL = self.calcBits(n_nodes,n_sensors)
        H = 1
        DE = 0
        CR = 1
        duty = 0.01
    
        # calculate
        Tsym = (2**SF)/BW
        payloadsymNB = 8 + math.ceil(((PL-4*SF+28+16-20*H)/(4*(SF-2*DE))))*(CR+4)
        
        Ton = payloadsymNB*Tsym
        
        Toff = Ton*((1/duty)-1)
        
        return round(Toff,1)
    
    
    def checkOK(self,n_nodes,n_sensors):
        
        ToffAir = self.ToffAir(n_nodes,n_sensors)
        
        # checks if the time off is in range of the EU directive
        if (ToffAir > 120):
            return False
        
        else:
            return True
        
        