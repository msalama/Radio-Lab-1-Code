import numpy as np
import pylab as plt

data = np.load('sun_04-02-2014_153105.npz')['volts']
lst = np.load('sun_04-02-2014_153105.npz')['lst']
ra = np.load('sun_04-02-2014_153105.npz')['ra']
dec = np.load('sun_04-02-2014_153105.npz')['dec']
hs = ra - lst

Blmbd0 = 700 #cm
lmbd = 2.5 #cm
dBlmbd = 1 #cm

for i in range(501):
    Blmbd = Blmbd0 + i
    f_f = Blmbd/lmbd*np.cos(dec)*np.cos(hs)

plt.figure()
plt.plot(hs,f_f*2*np.pi/24./3600.)
plt.ylabel("Fringe frequency range [Hz]")
plt.xlabel("Hour angle")

f_f_min = Blmbd/lmbd*np.cos(max(dec))*np.cos(max(hs))*2*np.pi/24./3600.

print "Range of fringe frequencies: ", min(f_f*2*np.pi/24./3600.), "to ", max(f_f*2*np.pi/24./3600.)
print "max hour angle: ", max(hs), "max declination", max(dec)
print "min fringe freq: ", f_f_min
