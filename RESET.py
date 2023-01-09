import numpy as np

'''
This script resets the counter when you want to reset the whole simulation
'''

# reset counter
counter = np.loadtxt("saved_data/counter.txt", delimiter = ",")
counter[1] = 1 #starts at 1 since we run the first feb file first and the end of this is taken as day 1. 
np.savetxt("saved_data/counter.txt", counter, delimiter = ",")







