import xml.etree.ElementTree as ET
import numpy as np

#loading counter
counter = np.loadtxt("saved_data/counter.txt", delimiter =',')
a = int(counter[1]) - 1

#using original values 
frac_C0 = 0.62
frac_E0 = 0.38
modC0 = 999.9999739967385
modE0 = 3.255543709422793

#loading new mass fractions
frac_C = np.loadtxt("saved_data/mass_fractions/current_collagen_mass_fraction.txt", delimiter = ',')
frac_E = np.loadtxt("saved_data/mass_fractions/current_elastin_mass_fraction.txt", delimiter = ',')

# importing febio file from previous time step
tree = ET.parse('jobs/FEBIO' + 'tav' + str(a) + '.feb') 
root = tree.getroot()

# updating the modulus values 
for material in root.iter('material'):
    id = material.get('id')
    k1 = material.find('k1')
    k1.text = str((modC0/frac_C0) * frac_C[int(id) - 1])
    c = material.find('c')
    c.text = str((modE0/frac_E0)* frac_E[int(id) - 1])

# updating the thickness 
Th0 = []
if counter[1] == 0:
    for ElementData in root.iter('ElementData'):
        part = ElementData.get('elem_set')
        e = ElementData.find('e')
        num = e.text
        numbers = [float(x) for x in num.split(",")]
        Th0.append(numbers)
    np.savetxt("saved_data/thickness/original_thickness_storage.txt", Th0, delimiter = ',')
else: 
    thS = np.loadtxt("saved_data/thickness/current_thickness_storage.txt", delimiter = ',')
    for ElementData in root.iter('ElementData'): 
        part = ElementData.get('elem_set')
        id = int(part[4:])
        e = ElementData.find('e') 
        array = thS[id - 1]
        string = ",".join(map(str, array))
        e.text = string
        #print(e.text)

# saving new tree
b = int(counter[1]) # saving feb file of current increment
tree.write('jobs/FEBIO' + 'tav' + str(b) + '.feb', encoding = 'ISO-8859-1')

# updating counter for next increment
counter[1] = counter[1] + 1 
np.savetxt("saved_data/counter.txt", counter, delimiter =',')

