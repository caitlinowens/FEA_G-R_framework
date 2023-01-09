import numpy as np 
from Read_XPLTfuncs import * 

counter = np.loadtxt("saved_data/counter.txt", delimiter =',')
a = int(counter[1]) - 1

xpltname = './jobs/FEBIO'+ 'tav' + str(a) + '.xplt'
nDoms = 1064

#Run GetFeb, using .xplt filename, the number of domains and your to output the data tress using True or False 
feb, _,nStates, _= GetFEB(xpltname,nDoms,False)
Nodes, nElems, nVar, StateTimes, VarNames, VarType = GetMeshInfo(feb)


displacement = GetData(feb,'displacement',nStates,nVar)
stress = GetData(feb,'stress',nStates,nVar)

displacement = np.array(displacement)
stress = np.array(stress)
