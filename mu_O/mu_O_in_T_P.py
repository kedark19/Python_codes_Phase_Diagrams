##  mu_O (in eV) expressed in terms of T and P 
########################################
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(8, 7))
ax=fig.add_subplot(111, label="1")
###  D_mu_O2 = [H0 + cp(T-T0) - TS0 + TCp ln(T/T0) + kb T ln(p/p0)]/2

T0=298
kb=1.38E-23
mole=6.022E23
atm=1.0E5

H0=8700/mole
Cp=3.5*kb
S0=205/mole
p0=1.0*atm

p1=1.0E-10*atm
p2=1.0E-06*atm
p3=1.0E-02*atm
p4=1.0E02*atm
p5=1.0E06*atm

T=np.arange(10,2000,10)
eV=1.602E-19

mu_1=(H0 + Cp*(T-T0) - T*S0 - T*Cp*np.log(T/T0) + kb*T*np.log(p1/p0))/(2*eV)
mu_2=(H0 + Cp*(T-T0) - T*S0 - T*Cp*np.log(T/T0) + kb*T*np.log(p2/p0))/(2*eV)
mu_3=(H0 + Cp*(T-T0) - T*S0 - T*Cp*np.log(T/T0) + kb*T*np.log(p3/p0))/(2*eV)
mu_4=(H0 + Cp*(T-T0) - T*S0 - T*Cp*np.log(T/T0) + kb*T*np.log(p4/p0))/(2*eV)
mu_5=(H0 + Cp*(T-T0) - T*S0 - T*Cp*np.log(T/T0) + kb*T*np.log(p5/p0))/(2*eV)


plt.setp(ax.spines.values(), linewidth=2)  ## for border 
plt.subplots_adjust(left=0.17, bottom=0.15, right=0.95, top=0.95, wspace=0, hspace=0)
plt.xlabel("Temperature (K)", size=22)
plt.ylabel("$\Delta$$\mu_{O}$ (eV)",color='blue', size=22)
plt.xlim(0,2000)
plt.ylim(-3.6,0)
plt.grid(True)
plt.tick_params(axis = 'both', which = 'major', labelsize = 22, width=3)
plt.plot(T,mu_1,label="p=1",color="blue",linewidth=2.5)
plt.text(1200, -3.3,'p=10$^{-10}$ atm', size=18, color='blue',rotation=-49)
plt.plot(T,mu_2,label="p=1",color="blue",linewidth=2.5)
plt.text(1250, -2.75,'p=10$^{-6}$ atm', size=18, color='blue',rotation=-43)
plt.plot(T,mu_3,label="p=1",color="blue",linewidth=2.5)
plt.text(1270, -2.2,'p=10$^{-2}$ atm', size=18, color='blue',rotation=-40)
plt.plot(T,mu_4,label="p=1",color="blue",linewidth=2.5)
plt.text(1300, -1.6,'p=10$^{2}$ atm', size=18, color='blue',rotation=-30)
plt.plot(T,mu_5,label="p=1",color="blue",linewidth=2.5)
plt.text(1300, -0.9,'p=10$^{6}$ atm', size=18, color='blue',rotation=-20)

plt.savefig("mu_O.pdf")
