import numpy as np
import pylab as plt

data = np.load('3C144_03-28-2014_001926.npz')['volts']
lst = 2*np.pi/24*np.load('3C144_03-28-2014_001926.npz')['lst']
ra = 1.95548498904
hs = lst - ra
dec = 0.383665059557 #3C144 precessed declination in decimal
"""
def filter(freq,volt):
    f_filt = []
    volt_filt = []
    for i in range(len(volt)):
        if i in range(502,13894) or i in range(0,43) or i in range(14334,14378):
        #if i in range(0,2000) or i in range(8001,14378):
            volt[i] = 0
            f_filt.append(freq[i])
            volt_filt.append(volt[i])
        else:
            f_filt.append(freq[i])
            volt_filt.append(volt[i])
    return f_filt, volt_filt
          
f_filt, volt_filt = filter(np.fft.fftfreq(len(data)),np.fft.fft(data))
freqfilter = np.array(f_filt)
volt_filter = np.array(volt_filt)
inv_volt_fft = np.fft.ifft(volt_filter)
"""
inv_volt_fft = data - np.mean(data)
#normalized filtered data
"""
dr = 7369
r = 0
for r in range(0,13999,1000):
    print "r: ", r
    print "r + 999: ", r+999
    norm_filt_data = inv_volt_fft[r:r+999]/(max(inv_volt_fft[r:r+999]))
"""
norm_filt_data = inv_volt_fft/(max(inv_volt_fft))

plt.figure()
#plt.subplot(211)
plt.plot(hs, norm_filt_data)#, linewidth=3)
plt.xlabel('Hour Angle [radians]',fontsize=16)
plt.ylabel('Fringe Output [$Volts^2$]',fontsize=16)
plt.title('Crab Nebula (3C144) Observed on 3/28/2014 at $00^h19^m26s$',fontsize=18)
#plt.subplot(212)
#plt.plot(freqfilter,abs(volt_filter)**2)
#plt.xlabel('Frequency [$Hz$]')
#plt.ylabel('Power')

M = len(data)
N = 2
time = np.arange(0,M)

#initial guess for parameters:
Blmbd0 = 700 #cm    
lmbd = 2.5 #cm

Y = np.ones((M,),dtype=float)
Y[:] = norm_filt_data

Baseline = []
Xisq = []
A = []
B = []
fit = []
for i in range(501): #want to run from 7m to 12m by 1cm
    Blmbd = Blmbd0+i
    Baseline.append(Blmbd)
    Csinhs = 2*np.pi*(Blmbd)/lmbd*np.cos(dec)*np.sin(hs)

    #in python: (col,row)
    X = np.ones((2,M),dtype = float)
    X[0] = np.cos(Csinhs)
    X[1] = np.sin(Csinhs)
    X = np.transpose(X)
    
    # alpha
    XX = np.dot(np.transpose(X),X)
    # beta
    XY = np.dot(np.transpose(X),Y)
    #inverse alpha
    XXI = np.linalg.inv(XX)
    #a
    a = np.dot(XXI,XY)
    A.append(a[0])
    B.append(a[1])
    #y-bar
    YBAR = np.dot(X,a)#-Y0
    fit.append(YBAR)
    #residuals/deviations in Y
    DELY = Y - YBAR
    #sample variance of data points
    s_sq = np.sum(DELY**2)/(M-N)
    Xisq.append(s_sq) 

plt.figure()
plt.plot(Baseline,Xisq)

print "min Xisq: ", min(Xisq), "at i = ", np.argmin(Xisq)
print "best A: ", A[np.argmin(Xisq)]
print "best B: ", B[np.argmin(Xisq)]
print "Baseline: ", Baseline[np.argmin(Xisq)]/100.

plt.figure()
#plt.plot(time,inv_volt_fft,'g')
plt.plot(hs,norm_filt_data,'g')
plt.xlabel('Hour Angle')
plt.ylabel('Volt')
#plt.plot(time,YBAR,'blue')
plt.plot(hs,fit[np.argmin(Xisq)],'blue')
#eb = plt.errorbar(hs,YBAR,yerr=DELY)

"""
diag_elems = np.dot(np.identity(2),a)
vardc = s_sq*diag_elems
sigma = np.sqrt(vardc)
"""