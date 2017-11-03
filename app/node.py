class Node(object):
    '''Assumes 1 minute timesteps'''
    alive = True
    n_sensors = 0
    uptime = 0 # in minutes
    sensor_voltage = 5
    sensor_current = 0.002 # in amps
    sensor_power_usage = sensor_voltage * sensor_current * 60 # 60 seconds in a timestep
    energy_left = 0 # in Joule
    panel_size = 0.25
    panel_effeciency = 0.25
    
    
    def __init__(self, n_sensors, handicap):
        self.n_sensors = n_sensors
          
        battery_size = 2500 # in mAh
        self.energy_left = battery_size * self.sensor_voltage * 3.6 * handicap
        
    def step(self, sensor_values, charge_factor):
        '''Does a single time step'''
        self.uptime += 1
        used = 0
        used += self.calculate_power_sensors(sensor_values)
        used += self.calculate_power_send_data()
        used += self.calculate_power_send_data()
        charge = 0
        charge += self.charge(charge_factor)      
        
        self.energy_left -= used
        self.energy_left += charge
        
        # Energy check
        if self.energy_left < 0:
            print("No energy left!")
            self.alive = False
        
        #print("Charge: {}\tLoss: {}\tRemaining: {}".format(charge, used, self.energy_left))
        
        return charge, used, self.energy_left
    
    def charge(self, charge_factor):
        baseline = 1000 # 1000 W baseline max per square meter 
        #factor = 0.5 # 0.5 for northern hemosphere
        
        energy = charge_factor * self.panel_size * self.panel_effeciency * 60
        
        return energy
        
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
