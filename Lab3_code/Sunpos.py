import ephem, time
import numpy as np

sun = ephem.Sun()
obs = ephem.Observer()

#UCB coordinates: (longitude = -122.2573 & latitude = 37.8732)
obs.lat = 37.8732*np.pi/180.
obs.long = -122.2573*np.pi/180.

#time.time() #UTC (seconds since 1970)
#ephem.now() #current time in England
obs.date = ephem.now() #set time of observation

print "date:", obs.date,"obs lat:", obs.lat,"obs long:",obs.long

sun.compute(obs)

print "Sun ra:", sun.ra
print "Sun dec:", sun.dec
print "Sun az:", sun.az
print "Sun alt:", sun.alt