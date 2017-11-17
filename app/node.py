import numpy as np

class Node(object):
    '''Assumes 1 minute timesteps'''
    alive = True
    n_sensors = 0
    uptime = 0 # in minutes
    #sensor_voltage = 5
    #sensor_current = 0.002 # in amps
    #sensor_power_usage = sensor_voltage * sensor_current * 60 # 60 seconds in a timestep
    energy_left = 0 # in Joule
    
    days_in_month = np.array([31,28,31,30,31,30,31,31,30,31,30,31])
    daily_solar_radiation = np.array([0.4,1.04,2.32,3.9,5.05,6.07,5.31,4.48,2.88,1.48,0.63,0.35])
    PR = 0.75 # performance ratio, coefficient for losses
    panel_efficiency = 0.2 # 20 % effeciency
    panel_size = 0.2 # in m^2
    
    def __init__(self, n_sensors, handicap):
        self.n_sensors = n_sensors
        battery_size = 2500         # in mAha
        #self.energy_left = battery_size * self.sensor_voltage * 3.6 * handicap
        self.energy_left = battery_size * 5 * 3.6 * handicap
        
    def charge(self, month):
        '''How much energy charged in one second, depending on the month'''
        kWh = self.panel_size * self.panel_efficiency * self.daily_solar_radiation[month] * self.PR
        E = kWh * 1000 * 3.6 / (3600 * 24)

        return E # per second

    def step(self, sensor_values, month):
        '''Does a single time step'''
        self.uptime += 1
        used = 0
        #used += self.calculate_power_sensors(sensor_values)
        #used += self.calculate_power_send_data()
        charge = 0
        charge += self.charge(month=month)
        
        self.energy_left -= used
        self.energy_left += charge
        
        # Energy check
        if self.energy_left < 0:
            print("No energy left!")
            self.alive = False
        
        #print("Charge: {}\tLoss: {}\tRemaining: {}".format(charge, used, self.energy_left))
        
        return charge, used, self.energy_left
"""    
        
    def calculate_power_sensors(self, sensor_values):
        '''Explicit for loop to catch wrong test value length'''
        total = 0
        
        if len(sensor_values) == self.n_sensors:
            return sum([value * self.sensor_power_usage for value in sensor_values])
        else:
            raise ValueError("n_sensors does not match sensor_values length")

    def calculate_power_send_data(self):
        '''https://www.digikey.com/en/articles/techzone/2011/aug/comparing-low-power-wireless-technologies'''
        protocol = {'BluetoothLE' : 0.000000153,     # In joyle/bit
                    'ZigBee' : 0.0001855,
                    'Wi-fi' : 0.00000000525
                   }
        data_size = self.n_sensors      # Theoretical minimum
        
        return data_size * protocol['ZigBee']
"""