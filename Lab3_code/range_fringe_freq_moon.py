import numpy as np
import pylab as plt
from math import * 
import ephem, time

moon = ephem.Moon()
obs = ephem.Observer()

#UCB coordinates: (longitude = -122.2573 & latitude = 37.8732)
obs.lat = 37.8732*np.pi/180.
obs.long = -122.2573*np.pi/180.

obs.date = ephem.date('2014/04/06 03:34:44') #set time of observation
i = 0
dec = []
ra = []
for i in range(14365):
    obs.date = obs.date + i
    moon.compute(obs)
    moon.dec
    dec.append(moon.dec)
    moon.ra
    ra.append(moon.ra)
    
data = np.load('moon_04-06-2014_033444.npz')['volts']
lst = np.load('moon_04-06-2014_033444.npz')['lst']
#ra = np.load('moon_04-06-2014_033444.npz')['ra']
#dec = np.load('moon_04-06-2014_033444.npz')['dec']
dec = 0.303832019147
hs = ra - lst
#hs = 1.80334876012 - lst

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
