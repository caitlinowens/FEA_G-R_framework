import numpy as np
from read_tav_xplt import stress, nStates, nDoms

counter = np.loadtxt("saved_data/counter.txt", delimiter = ',')
t = counter[1]

# Need to Calculate Von Mises Stress
all_von_data = []

n = 0
while n < len(stress.T): 
    von_data = []
    i = 0 
    while i < nStates : 
        a = float((stress[i,n]-stress[i,n+1])**2 + (stress[i,n+1]-stress[i,n+2])**2 + (stress[i,n+2]-stress[i,n])**2)
        b = (stress[i,n+3])**2 + (stress[i,n+4])**2 + (stress[i,n+5])**2
        v = (0.5*a) + (float(3)*b)
        von = np.sqrt(v)
        von_data.append(von)
        i = i + 1
    all_von_data.append(von_data) 
    n = n + 6  
von_mises = np.array(all_von_data) 
#print(von_mises.shape, von_mises)

# Need to define vonH -> should only be calculated and saved on first run 

if t == 1: 
    vonH = []
    i = 0 
    while i < nDoms: 
        x = np.mean(von_mises[i])
        vonH.append(x) 
        i = i + 1
    vonH = np.asarray(vonH)
    np.savetxt("saved_data/homeostatic_stress.txt", vonH, delimiter = ',')
    print("homeostatic stress reset")
else: 
    print("homeostatic stress not reset")
    pass





