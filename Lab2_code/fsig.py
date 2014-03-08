from math import *
import numpy as np
import pylab as plt

f_smpl = 10. #10kHz
t = np.linspace(0,2*np.pi,1000)

plt.figure()

data1 = np.load('fsig_1000.0.npz')['arr_0']

plt.subplot(521)
t1 = np.arange(0,len(data1))/f_smpl
plt.plot(t1,data1, '-o')
plt.title('Varying $f_{sig}$ to $f_{smpl}$ ratios')
sig1 = np.sin(2.*np.pi*(t+0.14))
plt.plot(t,sig1,label = '$f_{sig} = 1kHz$')
plt.xlim(0,5)
plt.ylim(-1.5,1.5)
plt.legend()

data2 = np.load('fsig_2000.0.npz')['arr_0']

plt.subplot(523)
t2 = np.arange(0,len(data2))/f_smpl
plt.plot(t2,data2,'-o')
sig2 = np.sin(2*np.pi*2.*(t+0.14))
plt.plot(t,sig2,label = '$f_{sig} = 2kHz$')
plt.xlim(0,5)
plt.ylim(-1.5,1.5)
plt.legend()

data3 = np.load('fsig_3000.0.npz')['arr_0']

plt.subplot(525)
t3 = np.arange(0,len(data3))/f_smpl
plt.plot(t3,data3,'-o')
plt.ylabel('Voltage')
sig3 = np.sin(2*np.pi*3.*t)
plt.plot(t,sig3,label = '$f_{sig} = 3kHz$')
plt.xlim(0,5)
plt.ylim(-1.5,1.5)
plt.legend()

data4 = np.load('fsig_4000.0.npz')['arr_0']

plt.subplot(527)
t4 = np.arange(0,len(data4))/f_smpl
plt.plot(t4,data4,'-o')
sig4 = np.sin(2*np.pi*4.*t)
plt.plot(t,sig4,label = '$f_{sig} = 4kHz$')
plt.xlim(0,5)
plt.ylim(-1.5,1.5)
plt.legend()

data5 = np.load('fsig_5000.0.npz')['arr_0']

plt.subplot(529)
t5 = np.arange(0,len(data5))/f_smpl
plt.plot(t5,data5, '-o')
plt.xlabel('Time [ms]')
sig5 = np.sin(2*np.pi*5.*(t+2.25))
plt.plot(t,sig5,label = '$f_{sig} = 5kHz$')
plt.xlim(0,5)
plt.ylim(-1.5,1.5)
plt.legend()

data6 = np.load('fsig_6000.0.npz')['arr_0']

plt.subplot(5,2,2)
t6 = np.arange(0,len(data6))/f_smpl
plt.plot(t6,data6, '-o')
sig6 = np.sin(2*np.pi*6.*t)
plt.plot(t,sig6,label = '$f_{sig} = 6kHz$')
plt.xlim(0,5)
plt.ylim(-1.5,1.5)
plt.legend()

data7 = np.load('fsig_7000.0.npz')['arr_0']

plt.subplot(5,2,4)
t7 = np.arange(0,len(data7))/f_smpl
plt.plot(t7,data7, '-o')
sig7 = np.sin(2*np.pi*7.*t)
plt.plot(t,sig7,label = '$f_{sig} = 7kHz$')
plt.xlim(0,5)
plt.ylim(-1.5,1.5)
plt.legend()

data8 = np.load('fsig_8000.0.npz')['arr_0']

plt.subplot(5,2,6)
t8 = np.arange(0,len(data8))/f_smpl
plt.plot(t8,data8,'-o')
sig8 = np.sin(2*np.pi*8.*t)
plt.plot(t,sig8, label = '$f_{sig} = 8kHz$')
plt.xlim(0,5)
plt.ylim(-1.5,1.5)
plt.legend()

data9 = np.load('fsig_9000.0.npz')['arr_0']

plt.subplot(5,2,8)
t9 = np.arange(0,len(data9))/f_smpl
plt.plot(t9,data9, '-o')
plt.xlabel('Time [ms]')
sig9 = np.sin(2*np.pi*9.*t)
plt.plot(t,sig9,label = '$f_{sig} = 9kHz$')
plt.xlim(0,5)
plt.ylim(-1.5,1.5)
plt.legend()

############################### FFT #################

plt.figure()
plt.subplot(521)
plt.plot(np.fft.fftfreq(len(data1),1/f_smpl),abs(np.fft.fft(data1))**2,label = '$f_{sig} = 1kHz$')
plt.title('Varying $f_{sig}$ to $f_{smpl}$ Ratios in Frequency Domain')
plt.legend()

plt.subplot(523)
plt.plot(np.fft.fftfreq(len(data2),1/f_smpl),abs(np.fft.fft(data2))**2,label = '$f_{sig} = 2kHz$')
plt.legend()

plt.subplot(525)
plt.plot(np.fft.fftfreq(len(data3),1/f_smpl),abs(np.fft.fft(data3))**2,label = '$f_{sig} = 3kHz$')
plt.ylabel('Power')
plt.legend()

plt.subplot(527)
plt.plot(np.fft.fftfreq(len(data4),1/f_smpl),abs(np.fft.fft(data4))**2,label = '$f_{sig} = 4kHz$')
plt.legend()

plt.subplot(529)
plt.plot(np.fft.fftfreq(len(data5),1/f_smpl),abs(np.fft.fft(data5))**2,label = '$f_{sig} = 5kHz$')
plt.xlabel('Frequency [$kHz$]')
plt.legend()

plt.subplot(5,2,2)
plt.plot(np.fft.fftfreq(len(data6),1/f_smpl),abs(np.fft.fft(data6))**2,label = '$f_{sig} = 6kHz$')
plt.legend()

plt.subplot(5,2,4)
plt.plot(np.fft.fftfreq(len(data7),1/f_smpl),abs(np.fft.fft(data7))**2,label = '$f_{sig} = 7kHz$')
plt.legend()

plt.subplot(5,2,6)
plt.plot(np.fft.fftfreq(len(data8),1/f_smpl),abs(np.fft.fft(data8))**2,label = '$f_{sig} = 8kHz$')
plt.legend()

plt.subplot(5,2,8)
plt.plot(np.fft.fftfreq(len(data9),1/f_smpl),abs(np.fft.fft(data9))**2,label = '$f_{sig} = 9kHz$')
plt.legend()
plt.xlabel('Frequency [$kHz$]')
