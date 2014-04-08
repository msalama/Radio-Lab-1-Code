import numpy as np
from math import * 
import ephem, time

obs = ephem.Observer()

#UCB coordinates: (longitude = -122.2573 & latitude = 37.8732)
obs.lat = 37.8732*np.pi/180.
obs.long = -122.2573*np.pi/180.

Date = str(raw_input("Observation date?"))
obs.date = Date
#obs.date = ephem.now() #set time of observation
#obs.date = 41724.465428240743

print "Observer parameters:", obs

Source = raw_input("What object are you observing? ")

HH = float(raw_input("HH: "))
MM = float(raw_input("MM: "))
SS = float(raw_input("SS: "))
ra = HH*15 + MM/4. + SS/240.

SIGN = float(raw_input("If West enter '-1': "))
DEG = float(raw_input("DEG: "))
ARCMIN = float(raw_input("ARCMIN: "))
ARCSEC = float(raw_input("ARCSEC: "))

#dec = -5.3911 # -05deg23'28''
dec = np.deg2rad(SIGN*(DEG + ARCMIN/60. + ARCSEC/3600.))

print Source
#print "ra: 05:34:31.95", "decimal:", ra
print "ra: ",HH,":",MM,":",SS,":", "decimal:", ra
print "dec: ",SIGN,":",DEG,":",ARCMIN,":",ARCSEC, "decimal:", dec

src = ephem.FixedBody()
src._ra = ra
src._dec = dec

src._epoch = ephem.J2000
src.compute(obs)

print "precessed ra:", src.ra, "decimal:", float(src.ra)
print "precessed dec:", src.dec, "decimal:", float(src.dec)

LST = obs.sidereal_time()
print "LST:", LST, "decimal:", float(LST)

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
