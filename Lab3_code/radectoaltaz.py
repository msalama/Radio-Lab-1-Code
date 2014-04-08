import numpy as np
from math import * 
import ephem, time

obs = ephem.Observer()

#UCB coordinates: (longitude = -122.2573 & latitude = 37.8732)
obs.lat = 37.8732*np.pi/180.
obs.long = -122.2573*np.pi/180.

obs.date = ephem.now() #set time of observation
#obs.date = 41724.465428240743

print "Observer parameters:", obs

#source: Orion
HH = 05
MM = 35
SS = 17.3
ra = HH*15 + MM/4. + SS/240.

#ra = 83.6292 # 05:34:31.95
SIGN = -1
DEG = 05
ARCMIN = 23
ARCSEC = 28

#dec = -5.3911 # -05deg23'28''
dec = SIGN*(DEG + ARCMIN/60. + ARCSEC/3600.)

print "Orion ra: 05:34:31.95", "decimal:", ra
print "Orion dec: -05:23:28", "decimal:", dec

src = ephem.FixedBody()
src._ra = ra
src._dec = dec

src._epoch = ephem.J2000
src.compute(obs)

print "Orion precessed ra:", src.ra, "decimal:", float(src.ra)
print "Orion prescessed dec:", src.dec, "decimal:", float(src.dec)

LST = obs.sidereal_time()
print "LST:", LST, "decimal:", float(LST)

#Conversion: RA - LST = HA
HA = src.ra - LST
print "HA: ", HA

#Equatorial coordinates:
equat = np.array([cos(src.dec)*cos(HA),cos(src.dec)*sin(HA),sin(src.dec)])
#print "equatorial vector:", equat

"""
ra = [0,radec[0]]
dec = [0,radec[1]]
#z = [0,radec[2]]
"""

#Conversion
ConvEH = np.array([[sin(obs.lat),0,-cos(obs.lat)],[0,1,0],[cos(obs.lat),0,sin(obs.lat)]])
#print "Conversion matrix:", ConvEH

horiz = np.dot(ConvEH,equat)
#print "horizontal vector:", horiz
cosacosA = horiz[0]
sina = horiz[2]    #sinalt = sin(sun.dec)*sin(obs.lat)+cos(sun.dec)*cos(obs.lat)*cos(HA)
#print "sin(alt):", sina

#
alt = asin(sina) #FINAL ALTITUDE
print "alt:", alt
#

cosA = cosacosA/(cos(alt))
#print "cos(az):", cosA
az = acos(cosA)
#print "az:", az

#
azimuth = 2.*np.pi - az
print "azimuth:", azimuth #FINAL AZIMUTH
#

#print "(Sun alt:", sun.alt, "decimal:", float(sun.alt), ")"
#print "(Sun az:", sun.az, "decimal:", float(sun.az), ")"

