import numpy as np
from define_stress_and_stretch import von_mises
from get_turnover_class_density import *
from read_tav_xplt import nDoms, StateTimes

# original mass values and fractions
mC0 = 62
mE0 = 38
m_total = mC0 + mE0 
frac_C0 = 0.62
frac_E0 = 0.38

#initial homeostatic stress
vonH = np.loadtxt("saved_data/homeostatic_stress.txt", delimiter = ',')
vonS = von_mises
# initialising time 
counter = np.loadtxt("saved_data/counter.txt", delimiter = ',')
Gtime = counter[1]
print(Gtime)
tau = np.linspace(0,1,num = 21) + (Gtime - 1)

#Mass Turnover parameters:
Amax = 1800
half_h = 70 
half_u = 1
rate = np.log(2)/half_h
gain = 0.1

#Elastin Damage parameters:
Dmax = 0.5
Tdam = 40

# initialising turnover class
getMass = NewMassTurnover(gain, rate, half_h, half_u, Amax)
# initialising elastin damage class 
getDamage = ElastinDamage(Dmax,mE0)

#if counter is 1, stored values for current values need to be reset: 

if Gtime == 1.0: 
    mE = []
    for x in range(0,1064):
        x = mE0
        mE.append(x)
    np.savetxt("saved_data/mass_data/current_elastin_mass.txt", mE, delimiter = ",")
    pC = np.loadtxt("saved_data/density_data/original_collagen_density.txt", delimiter = ",")
    np.savetxt("saved_data/density_data/current_collagen_density.txt", pC, delimiter = ",")
    pE = np.loadtxt("saved_data/density_data/original_elastin_density.txt", delimiter = ",")
    np.savetxt("saved_data/density_data/current_elastin_density.txt", pE, delimiter = ",")
    ptotal = np.loadtxt("saved_data/density_data/original_overall_density.txt", delimiter = ",")
    np.savetxt("saved_data/density_data/current_overall_density.txt", ptotal, delimiter = ",")
    thick_av = np.loadtxt("saved_data/thickness/original_averaged_thickness_storage.txt", delimiter = ',')
    np.savetxt("saved_data/thickness/current_averaged_thickness_storage.txt", thick_av, delimiter = ',')
    thick_all = np.loadtxt("saved_data/thickness/original_thickness_storage.txt", delimiter = ',')
    np.savetxt("saved_data/thickness/current_thickness_storage.txt", thick_all, delimiter = ',')
    frac_C = []
    for x in range(0,1064):
        x = frac_C0
        frac_C.append(x)
    np.savetxt("saved_data/mass_fractions/current_collagen_mass_fraction.txt", frac_C, delimiter = ',')
    frac_E = []
    for x in range(0,1064):
        x = frac_E0
        frac_E.append(x)
    np.savetxt("saved_data/mass_fractions/current_elastin_mass_fraction.txt", frac_E, delimiter = ',')
else:
    pass


# load original values needed 
pC0 = np.loadtxt("saved_data/density_data/original_collagen_density.txt", delimiter = ",")
p0 = np.loadtxt("saved_data/density_data/original_overall_density.txt", delimiter = ",")
th0_av = np.loadtxt("saved_data/thickness/original_averaged_thickness_storage.txt", delimiter = ",")
th0_all = np.loadtxt("saved_data/thickness/original_thickness_storage.txt", delimiter = ",")
# load current stored values 
mES = np.loadtxt("saved_data/mass_data/current_elastin_mass.txt", delimiter = ",")
pCS= np.loadtxt("saved_data/density_data/current_collagen_density.txt", delimiter = ",")
pES = np.loadtxt("saved_data/density_data/current_elastin_density.txt", delimiter = ",")
ptotalS = np.loadtxt("saved_data/density_data/original_overall_density.txt", delimiter = ",")
thick_av = np.loadtxt("saved_data/thickness/current_averaged_thickness_storage.txt", delimiter = ',')
thick_all = np.loadtxt("saved_data/thickness/current_thickness_storage.txt", delimiter = ',')
frac_C = np.loadtxt("saved_data/mass_fractions/current_collagen_mass_fraction.txt", delimiter = ',')
frac_E = np.loadtxt("saved_data/mass_fractions/current_elastin_mass_fraction.txt", delimiter = ',')

#creating arrays to track values of one element. i.e element 1
if Gtime == 1.0: 
    von_track1 = [vonH[7]]
    np.savetxt("saved_data/trackers/von1.txt", von_track1, delimiter = ',')
    c_density_track1 = [pC0[7]]
    np.savetxt("saved_data/trackers/c_density1.txt", c_density_track1, delimiter=",")
    e_density_track1 = [pES[7]]
    np.savetxt("saved_data/trackers/e_density1.txt", e_density_track1, delimiter = ",")
    thick_av_track1 = [thick_av[7]]
    np.savetxt("saved_data/trackers/thick_av1.txt", thick_av_track1, delimiter = ",")
    data_track1 = [pC0[7], 0, 0, 0, pC0[7]]
    np.savetxt("saved_data/trackers/density_production_track1.txt", data_track1, delimiter = ",")
    
    von_track2 = [vonH[712]]
    np.savetxt("saved_data/trackers/von2.txt", von_track2, delimiter = ',')
    c_density_track2 = [pC0[712]]
    np.savetxt("saved_data/trackers/c_density2.txt", c_density_track2, delimiter=",")
    e_density_track2= [pES[712]]
    np.savetxt("saved_data/trackers/e_density2.txt", e_density_track2, delimiter = ",")
    thick_av_track2 = [thick_av[712]]
    np.savetxt("saved_data/trackers/thick_av2.txt", thick_av_track2, delimiter = ",")
    data_track2 = [pC0[712], 0, 0, 0, pC0[712]]
    np.savetxt("saved_data/trackers/density_production_track2.txt", data_track2, delimiter = ",")

    von_track3 = [vonH[857]]
    np.savetxt("saved_data/trackers/von3.txt", von_track3, delimiter = ',')
    c_density_track3 = [pC0[857]]
    np.savetxt("saved_data/trackers/c_density3.txt", c_density_track3, delimiter=",")
    e_density_track3= [pES[857]]
    np.savetxt("saved_data/trackers/e_density3.txt", e_density_track3, delimiter = ",")
    thick_av_track3 = [thick_av[857]]
    np.savetxt("saved_data/trackers/thick_av3.txt", thick_av_track3, delimiter = ",")
    data_track3 = [pC0[857], 0, 0, 0, pC0[857]]
    np.savetxt("saved_data/trackers/density_production_track3.txt", data_track3, delimiter = ",")
   
else:
    von_track1 =  np.loadtxt("saved_data/trackers/von1.txt", delimiter = ',')
    c_density_track1 = np.loadtxt("saved_data/trackers/c_density1.txt", delimiter=",")
    e_density_track1 = np.loadtxt("saved_data/trackers/e_density1.txt", delimiter = ",")
    thick_av_track1 = np.loadtxt("saved_data/trackers/thick_av1.txt", delimiter = ",")
    data_track1 = np.loadtxt("saved_data/trackers/density_production_track1.txt", delimiter = ",")

    von_track2 =  np.loadtxt("saved_data/trackers/von2.txt", delimiter = ',')
    c_density_track2 = np.loadtxt("saved_data/trackers/c_density2.txt", delimiter=",")
    e_density_track2 = np.loadtxt("saved_data/trackers/e_density2.txt", delimiter = ",")
    thick_av_track2 = np.loadtxt("saved_data/trackers/thick_av2.txt", delimiter = ",")
    data_track2 = np.loadtxt("saved_data/trackers/density_production_track2.txt", delimiter = ",")

    von_track3 =  np.loadtxt("saved_data/trackers/von3.txt", delimiter = ',')
    c_density_track3 = np.loadtxt("saved_data/trackers/c_density3.txt", delimiter=",")
    e_density_track3 = np.loadtxt("saved_data/trackers/e_density3.txt", delimiter = ",")
    thick_av_track3 = np.loadtxt("saved_data/trackers/thick_av3.txt", delimiter = ",")
    data_track3 = np.loadtxt("saved_data/trackers/density_production_track3.txt", delimiter = ",")
    #survival_choice_track = np.loadtxt("saved_data/trackers/K_track.txt", delimiter = ",")

# finidng evolution
stress =[]

i = 0
while i < nDoms: 
    element = i
    # stress
    von = np.mean(vonS[i])
    stress.append(von)
    # new collagen density
    c = getMass.newMass(pC0[i], pCS[i], von, vonH[i], Gtime, tau, element)
    pC_delta = c[0]
    #degraded = c[2]
    #print(degraded)
    #saving collagen density data
    if i == 7: 
        data1 = [c[0], c[1], c[2], c[3], c[4]]
    if i == 712:
        data2 = [c[0], c[1], c[2], c[3], c[4]]
        print("survival tag:", getMass.chooseSurvivalRate(von, vonH[i])[1])
        print("current Mrate:", getMass.currentMrate(pC0[i], pCS[i], von, vonH[i]))
    if i == 857:
        data3 = [c[0], c[1], c[2], c[3], c[4]]
    # new elastin density 
    pE_delta = pCS[i] + pES[i] - pC_delta
    p_total = pE_delta + pC_delta
    # adding a end condition if elastin completely reduced ao it doesn't get a negative modulus
    if pE_delta < 0.00001:
        pE_delta = 0.00001
        pC_delta = p0[i] - pE_delta
        p_total = pE_delta + pC_delta
    if pC_delta < 0.00001:
        pC_delta = 0.00001
        pE_delta = p0[i] - pC_delta
        p_total = pE_delta + pC_delta
    # reset stored values
    pCS[i] = pC_delta
    pES[i] = pE_delta
    ptotalS[i] = p_total
    # get new elastin mass
    e = getDamage.damage(Gtime,Tdam)
    mES[i] = e
    # calculate new thickness 
    th = e/pE_delta
    thick_av[i] = th
    change = th/th0_av[i]
    thick_all[i] = th0_all[i] * change
    # calculate mass fractions 
    frac_C[i] = pC_delta/p_total
    frac_E[i] = pE_delta/p_total
    #if i == 7:
        #print("stress difference:", (von-vonH[i]))
        #print("new collagen density:", pC_delta)
        #print("new elastin density:", pE_delta)
        #print#("new elastin mass:", e)
        #print("new thickness:", th)
        #print("change in thickness:", change)
        #print("original thickness:", th0_all[i])
        #print("new thickness:", thick_all[i])
        #print("mass fraction of C:", frac_C[i])
        #print("mass fraction of E:", frac_E[i])
    i = i + 1

np.savetxt("saved_data/mass_data/current_elastin_mass.txt", mES, delimiter = ",")
np.savetxt("saved_data/density_data/current_collagen_density.txt", pCS, delimiter = ",")
np.savetxt("saved_data/density_data/current_elastin_density.txt", pES, delimiter = ",")
np.savetxt("saved_data/density_data/original_overall_density.txt", ptotalS, delimiter = ",")
np.savetxt("saved_data/thickness/current_averaged_thickness_storage.txt", thick_av, delimiter = ',')
np.savetxt("saved_data/thickness/current_thickness_storage.txt", thick_all, delimiter = ',')
np.savetxt("saved_data/mass_fractions/current_collagen_mass_fraction.txt", frac_C, delimiter = ',')
np.savetxt("saved_data/mass_fractions/current_elastin_mass_fraction.txt", frac_E, delimiter = ',')
np.savetxt("saved_data/stress_data/current_von_mises.txt", stress , delimiter = ',')

#updating trackers

von_track1 = np.append(von_track1, np.mean(vonS[7]))
np.savetxt("saved_data/trackers/von1.txt", von_track1, delimiter = ',')
c_density_track1 = np.append(c_density_track1, pCS[7]) 
np.savetxt("saved_data/trackers/c_density1.txt", c_density_track1, delimiter=",")
e_density_track1 = np.append(e_density_track1, pES[7])
np.savetxt("saved_data/trackers/e_density1.txt", e_density_track1, delimiter = ",")
thick_av_track1 = np.append(thick_av_track1, thick_av[7])
np.savetxt("saved_data/trackers/thick_av1.txt", thick_av_track1, delimiter = ",")
data_track1 = np.vstack((data_track1, data1))
np.savetxt("saved_data/trackers/density_production_track1.txt", data_track1, delimiter = ",")
#survival_choice_track = np.append(survival_choice_track, a)
#np.savetxt("saved_data/trackers/K_track.txt", survival_choice_track, delimiter = ",")

von_track2 = np.append(von_track2, np.mean(vonS[712]))
np.savetxt("saved_data/trackers/von2.txt", von_track2, delimiter = ',')
c_density_track2 = np.append(c_density_track2, pCS[712]) 
np.savetxt("saved_data/trackers/c_density2.txt", c_density_track2, delimiter=",")
e_density_track2 = np.append(e_density_track2, pES[712])
np.savetxt("saved_data/trackers/e_density2.txt", e_density_track2, delimiter = ",")
thick_av_track2 = np.append(thick_av_track2, thick_av[712])
np.savetxt("saved_data/trackers/thick_av2.txt", thick_av_track2, delimiter = ",")
data_track2 = np.vstack((data_track2, data2))
np.savetxt("saved_data/trackers/density_production_track2.txt", data_track2, delimiter = ",")

von_track3 = np.append(von_track3, np.mean(vonS[857]))
np.savetxt("saved_data/trackers/von3.txt", von_track3, delimiter = ',')
c_density_track3 = np.append(c_density_track3, pCS[857]) 
np.savetxt("saved_data/trackers/c_density3.txt", c_density_track3, delimiter=",")
e_density_track3 = np.append(e_density_track3, pES[857])
np.savetxt("saved_data/trackers/e_density3.txt", e_density_track3, delimiter = ",")
thick_av_track3 = np.append(thick_av_track3, thick_av[857])
np.savetxt("saved_data/trackers/thick_av3.txt", thick_av_track3, delimiter = ",")
data_track3 = np.vstack((data_track3, data3))
np.savetxt("saved_data/trackers/density_production_track3.txt", data_track3, delimiter = ",")