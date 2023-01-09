import subprocess
import numpy as np

#choose overall GTime
t = 3650

i = 0
while i <= t:
    # run feb 
    subprocess.run(['/Applications/FEBioStudio/FEBioStudio.app/Contents/MacOS/febio3', '-i', './jobs/FEBIO' + 'tav' + str(i) + '.feb'])

    # run turnover 
    subprocess.run(['python', 'density_turnover.py'])

    # check there wasn't an error termination on previous step
    a = np.loadtxt("saved_data/stress_data/current_von_mises.txt", delimiter = ',')

    if all (x == 0 for x in a): 
        print("error at day:", i)
        print("simulation stopped")
        i = t
    else: 
        pass

    # run parser 
    subprocess.run(['python', 'Parser.py'])

    i = i + 1

