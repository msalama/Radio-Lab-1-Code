import numpy as np
from math import * 
import ephem, time

obs = ephem.Observer()

#UCB coordinates: (longitude = -122.2573 & latitude = 37.8732)
obs.lat = 37.8732*np.pi/180.
obs.long = -122.2573*np.pi/180.

obs.date = "2014/03/28 00:19:26"

print "Observer parameters:", obs

ra = np.deg2rad(05*15 + 34/4. + 31.95/240.)
dec = np.deg2rad(22 + 52.1/3600.)

print "ra: 05:34:31.95", "radians:", ra
print "dec: 22:00:52.1", "radians:", dec

src = ephem.FixedBody()
src._ra = ra
src._dec = dec

src._epoch = ephem.J2000
src.compute(obs)

print "precessed ra:", src.ra, "radians:", float(src.ra)
print "precessed dec:", src.dec, "radians:", float(src.dec)

LST = obs.sidereal_time()
print "LST:", LST, "radians:", float(LST)

#Conversion: RA - LST = HA
HA = LST - src.ra
print "HA: ", HA

#Equatorial coordinates:
equat = np.array([cos(src.dec)*cos(HA),cos(src.dec)*sin(HA),sin(src.dec)])

#Conversion
ConvEH = np.array([[sin(obs.lat),0,-cos(obs.lat)],[0,1,0],[cos(obs.lat),0,sin(obs.lat)]])

horiz = np.dot(ConvEH,equat)
cosacosA = horiz[0]
sina = horiz[2]    #sinalt = sin(sun.dec)*sin(obs.lat)+cos(sun.dec)*cos(obs.lat)*cos(HA)

alt = asin(sina) #FINAL ALTITUDE
print "alt:", alt, "in degrees: ", alt*180/np.pi

cosA = cosacosA/(cos(alt))
az = acos(cosA)

azimuth = 2.*np.pi - az
print "azimuth:", azimuth, "in degrees: ", azimuth*180/np.pi #FINAL AZIMUTH
