import numpy as np
import pylab as plt

data = np.load('3C144_03-28-2014_001926.npz')['volts']
lst = np.load('3C144_03-28-2014_001926.npz')['lst']
hs = lst - 1.95548498904

Blmbd0 = 700 #cm
lmbd = 2.5 #cm
dec = 0.383665059557 #3C144 precessed declination in decimal
dBlmbd = 1 #cm

for i in range(501):
    Blmbd = Blmbd0 + i
    f_f = Blmbd/lmbd*np.cos(dec)*np.cos(hs)

plt.figure()
plt.plot(hs,f_f*2*np.pi/24./3600.)
plt.ylabel("Fringe frequency range [Hz]")
plt.xlabel("Hour angle")

#f_f_min = Blmbd/lmbd*np.cos(max(dec))*np.cos(max(hs))*2*np.pi/24./3600.
f_f_min = Blmbd/lmbd*np.cos(dec)*np.cos(max(hs))*2*np.pi/24./3600.

print "Range of fringe frequencies: ", min(f_f*2*np.pi/24./3600.), "to ", max(f_f*2*np.pi/24./3600.)
print "max hour angle: ", max(hs)#, "max declination", max(dec)
print "min fringe freq: ", f_f_min
