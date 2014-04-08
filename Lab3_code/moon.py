import numpy as np
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
    
#print "Observer parameters:", obs

#moon.compute(obs)
#print "moon ra:", moon.ra, "decimal:", float(moon.ra)
#print "moon dec:", moon.dec, "decimal:", float(moon.dec)

LST = obs.sidereal_time()
print "LST:", LST, "decimal:", float(LST)

HA = moon.ra - LST
print "HA: ", HA

"""
#Equatorial coordinates:
equat = np.array([cos(moon.dec)*cos(HA),cos(moon.dec)*sin(HA),sin(moon.dec)])

#Conversion
ConvEH = np.array([[sin(obs.lat),0,-cos(obs.lat)],[0,1,0],[cos(obs.lat),0,sin(obs.lat)]])

horiz = np.dot(ConvEH,equat)
cosacosA = horiz[0]
sina = horiz[2]    #sinalt = sin(moon.dec)*sin(obs.lat)+cos(moon.dec)*cos(obs.lat)*cos(HA)

alt = asin(sina) #FINAL ALTITUDE
print "alt:", alt

cosA = cosacosA/(cos(alt))
az = acos(cosA)

azimuth = 2.*np.pi - az
print "azimuth:", azimuth #FINAL AZIMUTH

print "(moon alt:", moon.alt, "decimal:", float(moon.alt), ")"
print "(moon az:", moon.az, "decimal:", float(moon.az), ")"
"""
