import numpy as np
import matplotlib.pyplot as plt
from math import *

V_in = 5. # Volts
L = 1.*10**(-6) # Henrys
C = 30.*10**(-9) # Farads
R = 27. # Ohms

f = np.arange(0.1, 3, 0.01);

Zc = 1/(1j*2.*pi*f*10**6*C)
ZL = 1j*2.*pi*f*10**6*L

ratio_V = 1/(1/Zc + 1/ZL)/(R + 1/(1/Zc + 1/ZL))

plt.figure(1)
plt.plot(f, ratio_V)
plt.title('LC filter')
plt.xlabel('Frequency [MHz]', fontsize = 15)
plt.ylabel('$V_{out}$/$V_{in}$', fontsize = 15)
plt.savefig('LC_filter.png')



V_in2 = 1. #Volt
R_2 = 1.*10**3 #Ohms
C_2 = 1.*10**(-9) #Farads

#f_2 = np.arange(0.05, 200, 0.1);
f_2 = np.arange(0.1, 500, 0.1);

Zc2 = 1/(1j*2.*pi*f_2*10**3*C_2)

ratio_V_2 = Zc2/(R_2 + Zc2)

plt.figure(2)
plt.plot(f_2, abs(ratio_V_2))
plt.title('Low Pass Filter')
plt.xlabel('Frequency [kHz]', fontsize = 15)
plt.ylabel('$V_{out}$/$V_{in}$', fontsize = 15)
plt.savefig('Low-pass filter.png')