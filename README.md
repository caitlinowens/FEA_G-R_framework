# FEA_G-R_framework

This repository aims to simulate the growth and remodelling of FEA models of aortic roots following a constrained mixture theory approach. 

The main files required: 

get_turnover_class.py -> involves the functions required to find the stress dependant collagen density. 

density_turnover.py -> takes the collagen density and finds adaptions in elastin density and wall thickness. 

Parser.py -> imports the adaptions calculated and edits the FEBio XML tree accordingly, creating a new .feb file

READ_XPLTfuncs.py -> not created by me (see pbmor repositorys) -> allows extraction of stress from febio xplt file

Run_main_density.py -> runs the original febio file, initiates READ_XPLTfuncs.py and density_turnover.py, then initiates the Parser to create a new.feb, this can be run in a loop. 

Adaptations required: 

- updates to make the fea model being used easily inserted. Need to import the value of nDoms into all scripts. 
- find a better way to initialise the original thickness and density values. 
- use a new incremental counter system.

