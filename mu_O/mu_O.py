## Calculate mu_O for a given T and P 
#################################################
import matplotlib.pyplot as plt
import numpy as np

###  D_mu_O2 = [H0 + cp(T-T0) - TS0 + TCp ln(T/T0) + kb T ln(p/p0)]/2
T0=298
kb=1.38E-23
mole=6.022E23
atm=1.0E5


H0=8700/mole
Cp=3.5*kb
S0=205/mole
p0=1.0*atm  # in Pa

p=50   # in Pa
T=673 #in K


eV=1.602E-19

print((H0 + Cp*(T-T0) - T*S0 - T*Cp*np.log(T/T0) + kb*T*np.log(p/p0))/(2*eV)) 
