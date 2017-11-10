# -*- coding: utf-8 -*-
import numpy as np

class EnergyHarvest(object):
    '''
    Information about solar 
    '''

    days_in_month = np.array([31,28,31,30,31,30,31,31,30,31,30,31])
    daily_solar_radiation = np.array([0.4,1.04,2.32,3.9,5.05,6.07,5.31,4.48,2.88,1.48,0.63,0.35])
    PR = 0.75 # performance ratio, coefficient for losses

    def charge(self, panel_size, efficiency, month):
        kWh = panel_size * efficiency * self.daily_solar_radiation[month] * self.PR
        E = kWh * 1000 * 3.6 / (3600 * 24)

        return E # per second
                
#%%
#panel = EnergyHarvest()

#for _ in range(12):
#    print("Daily energi in KJ: {0:2f}".format(panel.charge(, 0.2, _)*60*60*24))
