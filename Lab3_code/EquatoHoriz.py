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

LST = obs.sidereal_time()
print "LST:", LST, "decimal:", float(LST)

#Conversion: RA - LST = HA
HA = sun.ra - LST
print "HA: ", HA

#Equatorial coordinates:
equat = np.array([cos(sun.dec)*cos(HA),cos(sun.dec)*sin(HA),sin(sun.dec)])
print "equatorial vector:", equat
"""
ra = [0,radec[0]]
dec = [0,radec[1]]
#z = [0,radec[2]]
"""

#Conversion
ConvEH = np.array([[sin(obs.lat),0,-cos(obs.lat)],[0,1,0],[cos(obs.lat),0,sin(obs.lat)]])
print "Conversion matrix:", ConvEH

horiz = np.dot(ConvEH,equat)
print "horizontal vector:", horiz
cosacosA = horiz[0]
sina = horiz[2]    #sinalt = sin(sun.dec)*sin(obs.lat)+cos(sun.dec)*cos(obs.lat)*cos(HA)
print "sin(alt):", sina

#
alt = asin(sina) #FINAL ALTITUDE
print "alt:", alt
#

cosA = cosacosA/(cos(alt))
print "cos(az):", cosA
az = acos(cosA)
#print "az:", az

#
azimuth = 2.*np.pi - az
print "azimuth:", azimuth #FINAL AZIMUTH
#

print "(Sun alt:", sun.alt, "decimal:", float(sun.alt), ")"
print "(Sun az:", sun.az, "decimal:", float(sun.az), ")"

