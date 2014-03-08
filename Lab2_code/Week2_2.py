import numpy as np
import pylab as plt

#Digital DSB

f_smpl = 200e6 # 200 MHz
f_LO = 2e6# 2 MHz
df = 0.1e6 # 0.1 MHz
f_sigm = 2.1e6 # 2.1 MHz
f_sigp = 1.9e6 # 1.9 MHz

#peaks at 0.1, 3.9, 4.1MHz
"""
data1 = np.fromfile('adc_bram','>i')

#plt.figure(1)
#plt.subplot(211)
t1 = np.arange(0,len(data1))/f_smpl
#plt.plot(t1,data1)
plt.title('Single input')
plt.xlabel('Time [s]')
plt.ylabel('Voltage')

#plt.subplot(212)
#plt.plot(np.fft.fftfreq(len(data1),1/f_smpl),abs(np.fft.fft(data1))**2,'-kx')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power')

### analog mixing
data2 = np.fromfile('adc_bram_mixm','>i')

#plt.figure(2)
#plt.subplot(211)
t2 = np.arange(0,len(data2))/f_smpl
#plt.plot(t2,data2)
plt.title('Analog Mixing minus DSB Mixer')
plt.xlabel('Time [s]')
plt.ylabel('Voltage')

#plt.subplot(212)
#plt.plot(np.fft.fftfreq(len(data2),1/f_smpl),abs(np.fft.fft(data2))**2)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power')


data3 = np.fromfile('adc_bram_mixp','>i')

#plt.figure()
#plt.subplot(211)
t3 = np.arange(0,len(data3))/f_smpl
#plt.plot(t3,data3)
plt.title('Analog Mixing plus DSB Mixer')
plt.xlabel('Time [s]')
plt.ylabel('Voltage')

#plt.subplot(212)
#plt.plot(np.fft.fftfreq(len(data3),1/f_smpl),abs(np.fft.fft(data3))**2)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power')
"""
#### digital mixing
data4 = np.fromfile('mix_bram_m','>i')

print "length data4", len(data4)
plt.figure()
plt.subplot(211)
t4 = np.arange(0,len(data4))/f_smpl
plt.plot(t4,data4, label="$f_{sig-}$")
plt.title('Digitally Mixed DSB')
plt.xlabel('Time [s]')
plt.ylabel('Voltage')
plt.legend()

plt.subplot(212)
plt.plot(np.fft.fftfreq(len(data4),1./200),abs(np.fft.fft(data4))**2,'-o')
plt.xlabel('Frequency [MHz]')
plt.ylabel('Power')
plt.xlim([-5,5])
plt.plot([-4.1, -4.1], [0,3e12], "b--", linewidth = "2")
plt.plot([4.1, 4.1], [0,3e12], "b--", linewidth = "2")
plt.plot([-3.9, -3.9], [0,3e12], "b--", linewidth = "2")
plt.plot([3.9, 3.9], [0,3e12], "b--", linewidth = "2")
plt.plot([-0.1, -0.1], [0,3e12], "b--", linewidth = "2")
plt.plot([0.1, 0.1], [0,3e12], "b--", linewidth = "2")


data5 = np.fromfile('mix_bram_p','>i')
#plt.figure(5)
plt.subplot(211)
t5 = np.arange(0,len(data5))/f_smpl
plt.plot(t5, data5, label = '$f_{sig+}$')
#plt.title('Digital Mixing plus DSB Mixer')
#plt.xlabel('Time [s]')
#plt.ylabel('Voltage')
plt.legend()

plt.subplot(212)
plt.plot(np.fft.fftfreq(len(data5),1./200),abs(np.fft.fft(data5))**2,'-o')
#plt.xlabel('Frequency [MHz]')
#plt.ylabel('Power')
