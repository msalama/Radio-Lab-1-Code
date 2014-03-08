import numpy as np
import pylab as plt

#Analog DSB collected with Pulsar

f_smpl = 10. # 10MHz
f_LO = 2e6 # 2 MHz - carrier wave
df = 0.1e6 # 0.1MHz
f_sigm = 1.9e6 # 1.9MHz
f_sigp = 2.1e6 # 2.1MHz

data_m = np.load('thurs_sig_1900000.0.npz')['arr_0']
data_p = np.load('thurs_sig_2100000.0.npz')['arr_0']

plt.figure(1)

plt.subplot(211)
t = np.arange(0,len(data_p))/f_smpl
plt.plot(t,data_p, 'b',label='$f_{sig+}$')
t2 = np.arange(0,len(data_m))/f_smpl
plt.plot(t2,data_m,'magenta',label='$f_{sig-}$')
plt.xlabel('Time [$\mu s$]')
plt.ylabel('Voltage')
plt.title('Analog Mixer DSB')
plt.xlim(0,50)
plt.legend()

# minus df
plt.subplot(212)
plt.plot(np.fft.fftfreq(len(data_m),1./f_smpl),abs(np.fft.fft(data_m))**2, 'magenta', linewidth = 3)
#peaks at +/- 0.1 MHz (Lower sideband) and +/- 3.9MHz (Upper sideband)

# plus df
plt.plot(np.fft.fftfreq(len(data_p),1./f_smpl),abs(np.fft.fft(data_p))**2,'b', linewidth = 1)
plt.xlabel('Frequency [$MHz$]')
plt.ylabel('Power')
plt.xlim(-5,5,0.1)

#plt.text(-3,700000,'Lower sideband')
#plt.text(1,700000,'Upper sideband')
#peaks at +/- 0.1 MHz and +/- 4.1MHz
#plt.legend()

#Fourier filtering
#remove sum frequency component

"""
def filter(freq,power):
    f_filt = []
    power_filt = []
    for i in range(len(power)):
        if abs(freq[i]) != 4.1e6:
            f_filt.append(freq[i])
            power_filt.append(power[i])
    return f_filt, power_filt#, prenorm   

plt.figure()         
"""         
def filter(freq,power):
    f_filt = []
    power_filt = []
    for i in range(len(power)):
        if i in range(6715,6721) or i in range(9664,9669):
            power[i] = 0
            f_filt.append(freq[i])
            power_filt.append(power[i])
        else:
            f_filt.append(freq[i])
            power_filt.append(power[i])
    return f_filt, power_filt
          
f_filt, power_filt = filter(np.fft.fftfreq(len(data_p),1./f_smpl),abs(np.fft.fft(data_p))**2)
freqfilter = np.array(f_filt)
power_filter = np.array(power_filt)
inv_power_fft = np.fft.ifft(power_filter)

plt.figure(2)
plt.subplot(212)
plt.plot(freqfilter,power_filter)
plt.xlim(-5,5)
plt.xlabel('Frequency [$MHz$]')
plt.ylabel('Power')

plt.subplot(211)
plt.plot(t,inv_power_fft)
plt.xlim(0,50)
plt.xlabel('Time [$\mu s$]')
plt.ylabel('Voltage')
plt.title('Analog Mixer DSB after Fourier Filtering')



"""
plt.figure()
t = np.arange(0,len(data_p))/f_smpl
plt.plot(t,abs(data_p)**2)
plt.title('Waveform')
plt.xlabel('Time [s]')
plt.ylabel('Power')
"""