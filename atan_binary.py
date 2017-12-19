# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 20:59:44 2017

@author: Rajesh Patel
"""

import math
import numpy as np

# Calculate values for atan(2**(-i)) #
atan_table_degree = [((math.atan(2.0**(-j)))*(180/math.pi)) for j in range(1, 30)]
#print(len(atan_table_degree))

# Calculate the gain coefficients, will remove the need for multiplication in FPGA
gain = [(((math.sqrt(1+2**(-2*l))))) for l in range(1,30)]

# Accumulate gain; find X and Y values i.e. initial sine and cosine
for kk in range(len(gain)):
    gain_new = np.array(gain)
    K = np.cumprod(gain_new, axis=0)
   
# Initial value for cosine    
K_summed = (1/K[len(gain)-1])    

# Transform into binary. Note: make [14-1:0]? / remember twos comp
initial_cosine = (np.binary_repr(math.floor((K_summed)*2**(13)), width = 14))
initial_sine = (np.binary_repr(math.floor((0.0)*2**(13)), width = 14))
#print("14b'" + initial_cosine)
#print("14b'" + initial_sine)

#calculate values for atan and convert to suitable decimal value#
atan_table = [math.floor((math.atan(2.0**(-i)))*(180/math.pi)*(2**((29))/180)) for i in range(1, 30)]

my_array = np.array(atan_table)

for idx,value in enumerate(my_array):
    binary_value = np.binary_repr(value, width = 28)
    print("assign atan2i" + "[" + str(idx) + "]" +" 28b'" + binary_value +";" + " /* " + str(atan_table_degree[idx]) + u"\u00b0" + "  */")
