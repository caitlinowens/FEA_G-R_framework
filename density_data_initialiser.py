import numpy as np

# mass
mC0 = 62
mE0 = 38

# original thickness 
thick = np.loadtxt("saved_data/thickness/original_thickness_storage.txt", delimiter = ',')
th0 = []
for x in thick: 
    a = np.mean(x)
    th0.append(a)
np.savetxt("saved_data/thickness/original_averaged_thickness_storage.txt", th0, delimiter = ',')

pC0 = []
for x in th0:
    a = mC0/x
    pC0.append(a)
np.savetxt("saved_data/density_data/original_collagen_density.txt", pC0, delimiter ="," )

pE0 = []
for x in th0:
    a = mE0/x
    pE0.append(a)
np.savetxt("saved_data/density_data/original_elastin_density.txt", pE0, delimiter ="," )

p_total0 = []
for x in th0: 
    a = (mC0/x) + (mE0/x)
    p_total0.append(a)
np.savetxt("saved_data/density_data/original_overall_density.txt", p_total0, delimiter =",")