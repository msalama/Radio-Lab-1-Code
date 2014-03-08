import numpy as np
import pylab as plt

#f_sample = 200 MHz

data1 = np.fromfile('lomix1_cos_bram','>i')
data2 = np.fromfile('lomix1_sin_bram','>i')

full = data1 + 1j*data2
plt.figure(1)
plt.plot(full)
plt.figure(2)
plt.plot(np.fft.fftfreq(len(full),1./200),abs(np.fft.fft(full))**2)
plt.xlabel('Frequency [MHz]')
plt.ylabel('Power')

#plt.plot(np.fft.fftfreq(len(data1),1/200e6),abs(np.fft.fft(data1))**2,'-kx')


"""
plt.figure(1)
plt.subplot(211)
plt.plot(data1)
plt.title('cosine $f_{LO} = 1$')
plt.xlabel('N')
plt.ylabel('Power')
plt.subplot(212)
plt.plot(np.fft.fftfreq(len(data1),1/200e6),abs(np.fft.fft(data1)),'-kx')
plt.xlabel('Frequency [MHz]')
plt.ylabel('Power')


plt.figure(2)
plt.subplot(211)
plt.title('sine $f_{LO} = 1 sine$')
plt.xlabel('N')
plt.ylabel('Power')
plt.plot(data2)
plt.subplot(212)
plt.plot(np.fft.fftfreq(len(data2),1/200e6),abs(np.fft.fft(data2)),'-kx')
plt.xlabel('Frequency [MHz]')
plt.ylabel('Power')
"""