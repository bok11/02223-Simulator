import pdb

class Calculator(object):
 
    def add(self, x, y):
        
        number_types = (int, float, complex)
        
        if isinstance(x,number_types) and isinstance(y,number_types):
            #insert breakpoint for variabel exploration
            #pdb.set_trace()
            return x+y
        else:
            raise ValueError