import numpy as np
from math import * 
import ephem, time

sun = ephem.Sun()
obs = ephem.Observer()

#UCB coordinates: (longitude = -122.2573 & latitude = 37.8732)
obs.lat = 37.8732*np.pi/180.
obs.long = -122.2573*np.pi/180.

obs.date = ephem.now() #set time of observation

print "date:", obs.date,"obs lat:", obs.lat,"obs long:",obs.long

sun.compute(obs)

print "Sun ra:", sun.ra, "decimal:", float(sun.ra)
print "Sun dec:", sun.dec, "decimal:", float(sun.dec)


#Equatorial coordinates:
"""
radec = np.array([sun.ra,sun.dec])

ra = [0,radec[0]]
dec = [0,radec[1]]
#z = [0,radec[2]]
"""
LST = obs.sidereal_time()
print "LST:", LST, "decimal:", float(LST)

#Conversion: RA - LST = HA
HA = sun.ra - LST
print "HA: ", HA

#Conversion
sinalt = sin(sun.dec)*sin(obs.lat)+cos(sun.dec)*cos(obs.lat)*cos(HA)
print "sin(alt):", sinalt
alt = asin(sinalt)
print "alt:", alt

az = 2*np.pi - alt
print "az:", az

print "(Sun alt:", sun.alt, "decimal:", float(sun.alt), ")"
print "(Sun az:", sun.az, "decimal:", float(sun.az), ")"


"""
angle = np.pi/4.

#rotation matrix around z-axis
Rotz = np.array([[cos(angle),-sin(angle),0],[sin(angle),cos(angle),0],[0,0,1]])

#Az and Alt coordinates:
azalt = np.dot(Rotz,radec)

az = [0,azalt[0]]
alt = [0,azalt[1]]
newz = [0,azalt[2]]
"""

