import numpy as np
import pylab as plt

print "Main sources:"
print "sun: sun_04-02-2014_153105.npz"
print "C144: 3C144_03-28-2014_001926.npz"
print "moon: moon_04-06-2014_033444.npz"
print "Other sources:"
print "moon1: moon_03-27-2014_132449.npz"
print "moon2: moon_03-28-2014_132255.npz"
print "m17 : m17_03-28-2014_091203.npz"
print "orion : orion_03-27-2014_092354.npz"

source = str(raw_input("Source observing: "))

if source == 'sun':    
    data = np.load('sun_04-02-2014_153105.npz')['volts']
    title = "Horizon-to-Horizon Sun Observed on 4/2/2014"
elif source == 'C144':
    data = np.load('3C144_03-28-2014_001926.npz')['volts']
    title = "3C144 (Crab Nebula) Observed on 3/28/2014"
elif source == 'moon1':
    data = np.load('moon_03-27-2014_132449.npz')['volts']
    title = "Moon observed on 3/27/2014"
elif source == 'moon2':
    data = np.load('moon_03-28-2014_132255.npz')['volts']
    title = "Moon observed on 3/28/2014"
elif source == 'm17':
    data = np.load('m17_03-28-2014_091203.npz')['volts']
    title = "M17 observed on 3/28/2014"
elif source == 'orion':
    data = np.load('orion_03-27-2014_092354.npz')['volts']
    title = "Orion observed on 3/27/2014"
elif source == 'moon':
    data = np.load('moon_04-06-2014_033444.npz')['volts']
    title = "Moon observed on 4/6/2014"
else:
    print "Not a source"
    
plt.figure()
plt.subplot(211)
plt.plot(data)
plt.xlabel('Time [s]')
plt.ylabel('$Voltage^2$')
plt.title(title)
plt.subplot(212)
#plt.plot(np.fft.fftshift(abs(np.fft.fft(data))))
fft_freq = np.fft.fftfreq(len(data))
fft_power = abs(np.fft.fft(data))**2
plt.plot(fft_freq,fft_power)
plt.ylabel('Power')
plt.xlabel('Frequency [Hz]')

"""
plt.subplot(212)
#theta = np.arange(0,len(data)/3600.*2*np.pi/24.,1./len(data))
#time = np.arange(0,len(data)/3600.*2*np.pi/24.,1/3600.*2*np.pi/24.)
theta = np.arange(0,len(data)/3600.*15*np.pi/180.,1/3600.*2*np.pi/24.)
plt.plot(theta, data)
plt.xlabel('Radians')
plt.ylabel('Voltage')
"""



