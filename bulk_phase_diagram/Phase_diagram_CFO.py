### EXP
import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.integrate import quad

####
fig=plt.figure(figsize=(6.6, 10.2))
ax=fig.add_subplot(111, label="1")
ax.xaxis.tick_top()
ax.yaxis.tick_right()
plt.subplots_adjust(top=0.82) 
plt.subplots_adjust(right=0.85) 
ax.tick_params(axis = 'both', which = 'major', labelsize = 20, width=3)
ax.spines['top'].set_linewidth(3)
ax.spines['right'].set_linewidth(3)

CoO=-2.474
Co3O4=-9.266
FeO=-2.829
Fe2O3=-8.572
Fe3O4=-11.631
CoFe2O4=-11.853

Co_lim=CoFe2O4
Fe_lim=CoFe2O4/2
#print(Co_lim,Fe_lim)
mu_Co=np.arange(0.0,Co_lim,-0.01)
mu_Fe=np.arange(0.0,Fe_lim,-0.01)
plt.ylim(Co_lim,0)
plt.xlim(Fe_lim,0)

ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.xaxis.set_label_position('top') 
ax.yaxis.set_label_position('right') 
ax.set_ylabel("$\Delta\mu_{Co}$ (eV)", size=22, color="blue",rotation='vertical',labelpad=1)
ax.set_xlabel("$\Delta\mu_{Fe}$ (eV)", size=22, labelpad=15, color="red")
#ax.set_title("Phase diagram of CoFe$_2$O$_4$ (Exp.)", pad=10, size=18)
ax.set_title("Using experimental values of E$_f$", pad=20, size=22)
# equation: y=(-y0/x0)*(x-x0)
slope=-Co_lim/Fe_lim
theta=m.degrees(m.atan(slope))
mu_Co=slope*(mu_Fe - Fe_lim)

#print(slope,theta)
###################### mu_O 
ax.plot(mu_Fe,mu_Co,color='black',linewidth=3)
plt.text((Fe_lim-2.75)/2, (Co_lim-2.75)/2,'O-rich ($\mu_O = 0$)', size=22, color='C0',rotation=-56)
#print(mu_Co)
x0_muO=Fe_lim
y0_muO=0
x1_muO=0
y1_muO=Co_lim

###################### CoO: 
y0_CoO=CoO
x0_CoO=(y0_CoO - Co_lim)/slope
x1_CoO=-((4*CoO) - CoFe2O4)/2
y1_CoO=0
slope_CoO=(y1_CoO-y0_CoO)/(x1_CoO-x0_CoO)
print("CoO",  x0_CoO,y0_CoO,x1_CoO,y1_CoO,slope_CoO)
point1=[x0_CoO,x1_CoO]
point2=[y0_CoO,y1_CoO]
ax.plot(point1,point2, color="blue",linewidth=4)
plot_CoO=slope_CoO*(mu_Fe - x1_CoO)

###################### Co3O4: 
y0_Co3O4 =Co3O4/3
x0_Co3O4 =(y0_Co3O4 - Co_lim)/slope
x1_Co3O4 =-(Co3O4 - CoFe2O4)/2
y1_Co3O4 =0
slope_Co3O4 =(y1_Co3O4-y0_Co3O4)/(x1_Co3O4-x0_Co3O4)
print("Co3O4",  x0_Co3O4,y0_Co3O4,x1_Co3O4,y1_Co3O4,slope_Co3O4)
point1 =[x0_Co3O4,x1_Co3O4]
point2 =[y0_Co3O4,y1_Co3O4]
ax.plot(point1,point2, color="blue",linewidth=3)
plot_Co3O4 =slope_Co3O4*(mu_Fe - x1_Co3O4)

###################### FeO: 
x0_FeO=FeO
y0_FeO=slope*x0_FeO + Co_lim
y1_FeO=-(4*FeO - CoFe2O4)
x1_FeO=0
slope_FeO=(y1_FeO-y0_FeO)/(x1_FeO-x0_FeO)
print("FeO" ,x0_FeO, y0_FeO, x1_FeO, y1_FeO, slope_FeO)
point1=[x0_FeO, x1_FeO]
point2=[y0_FeO, y1_FeO]
ax.plot(point1,point2, color="red",linewidth=3)
plot_FeO=slope_FeO*mu_Fe + y1_FeO

###################### Fe2O3: 
x0_Fe2O3=Fe2O3/2
y0_Fe2O3=slope*x0_Fe2O3 + Co_lim
y1_Fe2O3=-((4/3)*Fe2O3 - CoFe2O4)
x1_Fe2O3=0
slope_Fe2O3=(y1_Fe2O3-y0_Fe2O3)/(x1_Fe2O3-x0_Fe2O3)
print("Fe2O3",  x0_Fe2O3,y0_Fe2O3,x1_Fe2O3,y1_Fe2O3,slope_Fe2O3)
point1=[x0_Fe2O3,x1_Fe2O3]
point2=[y0_Fe2O3,y1_Fe2O3]
ax.plot(point1,point2, color="red",linewidth=3)
plot_Fe2O3= slope_Fe2O3*mu_Fe + y1_Fe2O3

###################### Fe3O4: 
x0_Fe3O4=Fe3O4/3
y0_Fe3O4=slope*x0_Fe3O4 + Co_lim
y1_Fe3O4=-(Fe3O4 - CoFe2O4)
x1_Fe3O4=0
slope_Fe3O4=(y1_Fe3O4-y0_Fe3O4)/(x1_Fe3O4-x0_Fe3O4)
print("Fe3O4",  x0_Fe3O4,y0_Fe3O4,x1_Fe3O4,y1_Fe3O4,slope_Fe3O4)
point1=[x0_Fe3O4, x1_Fe3O4]
point2=[y0_Fe3O4, y1_Fe3O4]
ax.plot(point1,point2, color="red",linewidth=3)
plot_Fe3O4= slope_Fe3O4*mu_Fe + y1_Fe3O4

#######################  Plot ##########
###########   CoO #######
plt.text(-3.85, -1.7,'CoO', size=18, color='blue',rotation=22)

###########   Co3O4 #######
plt.text(-4.5, -2.9,'Co$_3$O$_4$', size=16, color='blue',rotation=35)

###########   FeO  #######
plt.text(-2.1, -4.9,'FeO', size=18, color='red',rotation=53)

###########   Fe2O3  #######
plt.text(-3.4, -3.0,'Fe$_2$O$_3$', size=16, color='red',rotation=24)

###########   Fe3O4  #######
y3=np.minimum(plot_Fe2O3, plot_Fe3O4)
y4=np.maximum(plot_FeO, mu_Co)
plt.text(-2.6, -3.1,'Fe$_3$O$_4$', size=18, color='red',rotation=32)


################
y3=np.minimum(plot_CoO, plot_Co3O4)
y5=np.maximum(plot_Fe2O3, plot_Fe3O4)
ax.fill_between(mu_Fe, y3, y5, where=( mu_Fe >= x0_Co3O4), color='black', alpha=0.3)

ax.scatter(-1.98, -1.31,s=100,marker='+',color='black',linewidths=3)

#plt.text(-6, -3.9,'CoFe$_2$O$_4$', size=20, color='Black')
#plt.arrow(-5.1,-3.4,2.2,1.4,color="red", head_length = 0.1, head_width = 0.1, length_includes_head=True)

plt.savefig("phase_CFO_EXP.pdf")
plt.show()
