'''
This is an intial script to define the mass turnover as a class that can be used in the tube inflation testing, with function .mass() returning current mass density of collagen.

These functions are based on equations given in Wilson et al 2012.

Main function is to return the current modulus of collagen. -> example "".mass()[2]
Can also return basal production rate, mass production rate, survival, overall new mass deposited left and old mass deposited left. 

'''

import numpy as np 
import math as m 
from scipy import integrate 

class MassTurnover: 
    def __init__(self,Amax,rate,gain,half_h,half_u):
        self.Amax = Amax 
        self.rate = rate 
        self.gain = gain 
        self.half_h = half_h 
        self.half_u = half_u 
        

    def basal(self, pC0): 
        def g(x): 
            return m.exp(-self.rate * x)
        a = integrate.quad(g,0,self.Amax) 
        basal = pC0 / a[0]
        return basal

    def mrate(self, pC0, pCS, von, vonH): 
        return pCS/pC0 * self.basal() * (self.gain * ((von-vonH)/vonH) + 1)
         
    
    def survival(self, von, vonH, Gtime, tau): 
        surv_new = []
        if von >= vonH: 
            K = self.rate
            choice = "kcq"
        else: 
            Delta = ((von-vonH)/vonH)**2
            w = (self.half_h/self.half_u)- 1
            K = self.rate + (self.rate*w*(Delta))
            choice = "Kk"
        for x in tau: 
            q = np.exp(-K * (Gtime - x))
            surv_new.append(q)
        Q = np.exp(-K * 1)
        return surv_new, Q, K, choice



    def mass(self, Gtime, tau, pC0, pCS, von, vonH): 
        new_dep = []
        K = self.survival(von, vonH, Gtime, tau) 
        M = self.mrate(pC0,pCS,von,vonH)
        for surv in K[0]:
            a = surv * M
            new_dep.append(a)
        total_new = np.trapz(new_dep,tau)
        total_old = K[1] * pCS
        current = total_new + total_old
        return total_new, total_old, current, M, K[2]

'''
Using the second mass turnover equations, using an incremental approach that was tested on the tube test
'''
class NewMassTurnover: 
    def __init__(self, gain, rate, half_h, half_u, Amax):
        self.gain = gain
        self.rate = rate
        self.half_h = half_h
        self.half_u = half_u
        self.Amax = Amax


    def basalrate(self, pC0): 
        def g(x): 
            return m.exp(-self.rate * x)
        a = integrate.quad(g,0,self.Amax) 
        basal = pC0 / a[0]
        return basal
    
    def currentMrate(self, pC0, pCS, von, vonH):
        return pCS/pC0 * self.basalrate(pC0) * ((self.gain * ((von-vonH)/vonH)) + 1)

    def chooseSurvivalRate(self, von, vonH): 
        if von >= vonH: 
            K = self.rate
            tag = 1
        else: 
            Delta = ((von-vonH)/vonH)**2
            w = (self.half_h/self.half_u)- 1
            K = self.rate + (self.rate*w*(Delta))
            tag = 2
        return K, tag


    def oldMassSurvival(self, pC0, von, vonH, Gtime, element):
        if Gtime <= 1 and element < 1:
            history_array = np.ones(1064)
            a = np.exp(-self.chooseSurvivalRate(von, vonH)[0] * Gtime)
            b = np.exp(-self.chooseSurvivalRate(von, vonH)[0] * 0)
            old = pC0 * (a - b)
            history_array[element] = a
            np.savetxt("saved_data/Q_history.txt", history_array, delimiter = ',')
            #trying to save the past time here, i.e a becomes the new b in else statement
        elif Gtime <= 1: 
            a = np.exp(-self.chooseSurvivalRate(von, vonH)[0] * Gtime)
            b = np.exp(-self.chooseSurvivalRate(von, vonH)[0] * 0)
            old = pC0 * (a - b)
            history_array = np.loadtxt("saved_data/Q_history.txt", delimiter = ',')
            history_array[element] = a
            np.savetxt("saved_data/Q_history.txt", history_array, delimiter = ',')
        else:
            a = np.exp(-self.chooseSurvivalRate(von, vonH)[0] * Gtime)
            history_array = np.loadtxt("saved_data/Q_history.txt", delimiter = ',')
            b = history_array[element]
            old = pC0 * (a - b)
            history_array[element] = a
            np.savetxt("saved_data/Q_history.txt", history_array, delimiter = ',')
        return old, a , b 

   # attempting a different set up for the old mass degraded calc:

    def oldMassSurival2(self, pC0, von, vonH, Gtime): 
        a = np.exp(-self.chooseSurvivalRate(von, vonH)[0] * Gtime)
        b = np.exp(-self.chooseSurvivalRate(von, vonH)[0] * (Gtime - 1))
        old = pC0 * (a - b)
        return old


    def int_S_to_DeltaS(self, pC0, pCS, von, vonH, Gtime, tau): 
        new_dep = []
        q_history = []
        for x in tau: 
            q = np.exp(- self.chooseSurvivalRate(von, vonH)[0] * (Gtime - x))
            q_history.append(q)
            dep = q * self.currentMrate(pC0, pCS, von, vonH)
            new_dep.append(dep)
        total_new = np.trapz(new_dep,tau)
        percent_change = ((q_history[0]- q_history[20])/ q_history[20]) * 100
        return total_new, percent_change
    
    def int_0_to_S(self, pC0, pCS, von, vonH, Gtime, tau, element):
        if Gtime == 1 and element == 0: 
            dep_array = np.ones(1064)
            degraded = 0 
            left = 0
            added = self.int_S_to_DeltaS(pC0, pCS, von, vonH, Gtime, tau)[0]
            history = added + left
            dep_array[element] = history
            np.savetxt("saved_data/dep_history.txt", dep_array, delimiter = ' ')
        elif Gtime == 1 and element > 0: 
            #print(element)
            dep_array = np.loadtxt("saved_data/dep_history.txt", delimiter = ' ')
            degraded = 0
            left = 0 
            added = self.int_S_to_DeltaS(pC0, pCS, von, vonH, Gtime, tau)[0]
            history = added + left 
            dep_array[element] = history
            np.savetxt("saved_data/dep_history.txt", dep_array, delimiter = ' ')
        else: 
            dep_array = np.loadtxt("saved_data/dep_history.txt", delimiter = ' ')
            a = dep_array[element]
            percent_change = self.int_S_to_DeltaS(pC0, pCS, von, vonH, Gtime, tau)[1]
            degraded = ((a/100) * percent_change)
            left = a + degraded
            added = self.int_S_to_DeltaS(pC0, pCS, von, vonH, Gtime, tau)[0]
            dep_history = added + left
            dep_array[element] = dep_history
            np.savetxt("saved_data/dep_history.txt", dep_array, delimiter = ' ')
        return degraded


    def newMass(self, pC0, pCS, von, vonH, Gtime, tau, element): 
        old = self.oldMassSurival2(pC0, von, vonH, Gtime)
        new_old = self.int_0_to_S( pC0, pCS, von, vonH, Gtime, tau, element)
        new_new = self.int_S_to_DeltaS(pC0, pCS, von, vonH, Gtime, tau)[0]
        total = old + new_old + new_new + pCS
        if total < 0: 
            total = 0.0 
        return total, old, new_old, new_new, pCS
'''
Now defining the elastin damage class. 

Class takes arguments: Dmax = maximum damage, tdam = saturation factor, e0 = original elastin modulus

Damage function takes extra argument: Gtime = G&R time 

Damage function returns: eS = current elastin modulus at Gtime

This will need to be updated for the FEA framework to include the regional change paraemters: 
focal point, axial position and spread. 

'''

class ElastinDamage: 
    def __init__(self, Dmax, e0): 
        self.Dmax = Dmax 
        self.e0 = e0

    def damage(self,Gtime,tdam): 
        a = self.Dmax*(1-(m.exp(-Gtime/tdam)))
        eS =  self.e0 * (1 - a)
        return eS




    



    
