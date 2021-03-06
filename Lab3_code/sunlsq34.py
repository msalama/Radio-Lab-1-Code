import numpy as np
import pylab as plt
from scipy import signal

data = np.load('sun_04-02-2014_153105.npz')['volts']
lst = 2*np.pi/24*np.load('sun_04-02-2014_153105.npz')['lst']
ra = 2*np.pi/24*np.load('sun_04-02-2014_153105.npz')['ra']
dec = np.deg2rad(np.load('sun_04-02-2014_153105.npz')['dec'])
hs = lst - ra

filt_data = data - np.mean(data)
cut_data1 = filt_data[3000:7000]
cut_data = cut_data1/max(cut_data1)
cut_hs = hs[3000:7000]
cut_dec = dec[3000:7000]

#envelope:
# #coeff, cutoff freq, nyquist
sig = signal.firwin(150, 0.01)#, f = 1)
env1 = signal.fftconvolve(sig, abs(cut_data))
env = env1[:len(cut_data)]

#initial guess for parameters:
phi0 = 0 #cm    
Blmbd = 1000 #cm
lmbd = 2.5 #cm

M = len(env)
N = 3
time = np.arange(0,M)

Y1 = np.ones((M,),dtype=float)
Y1[:] = cut_data

phase = []
Xisq = []
fit1 = []
for i in range(0,100): #phi from 0 to pi
    phi = phi0+i*np.pi/100.
    phase.append(phi)
    F = np.cos(2*np.pi*Blmbd/lmbd*np.cos(cut_dec)*np.sin(cut_hs)+phi)
    #in python: (col,row)
    X1 = np.ones((N,M),dtype = float)
    X1[0] = F
    X1[1] = cut_hs*F
    X1[2] = cut_hs**2*F
    X1 = np.transpose(X1)
    # alpha
    XX1 = np.dot(np.transpose(X1),X1)
    # beta
    XY1 = np.dot(np.transpose(X1),Y1)
    #inverse alpha
    XXI1 = np.linalg.inv(XX1)
    #a: matrix of coefficients
    a1 = np.dot(XXI1,XY1)
    #y-bar
    YBAR1 = np.dot(X1,a1)
    fit1.append(YBAR1)
    #residuals/deviations in Y
    DELY1 = Y1 - YBAR1
    #sample variance of data points
    s_sq1 = np.sum(DELY1**2)/(M-N)
    Xisq.append(s_sq1)

print "phi", phase[np.argmin(Xisq)]
plt.figure(1)
plt.plot(phase,Xisq,'k')
plt.xlabel('Phase guess [$radians$]',fontsize=16)
plt.ylabel('$\chi^2$',fontsize=16)
plt.title('Finding minimized $\chi^2$',fontsize=18)

#def lsq(env):
Y = np.ones((M,),dtype=float)
Y[:] = env
#in python: (col,row)
X = np.ones((N,M),dtype = float)
X[0] = 1
X[1] = cut_hs
X[2] = cut_hs**2
X = np.transpose(X)
# alpha
XX = np.dot(np.transpose(X),X)
# beta
XY = np.dot(np.transpose(X),Y)
#inverse alpha
XXI = np.linalg.inv(XX)
#a: matrix of coefficients
a = np.dot(XXI,XY)
A = a[0]
B = a[1]
C = a[2]
#y-bar
YBAR = np.dot(X,a)
#residuals/deviations in Y
DELY = Y - YBAR
#sample variance of data points
s_sq = np.sum(DELY**2)/(M-N)

print "best A = ", A#[np.argmin(Xisq)]
print "best B = ", B#[np.argmin(Xisq)]
print "best C = ", C#[np.argmin(Xisq)]   

plt.figure(2)
plt.plot(cut_hs,cut_data+0.35)
plt.plot(cut_hs,env, linewidth = 1.5, color = 'magenta',label='envelope')
plt.plot(cut_hs,YBAR,linewidth = 1.5,color = 'orange',label='lsq')
plt.xlabel('Hour Angle [$radians$]',fontsize = 16)
plt.ylabel('Fringe Output [$Volts^2$]',fontsize = 16)
plt.title('Sun Horizon to Horizon Observation on 4/2/2014',fontsize = 18)

#absfit = abs(fit[np.argmin(Xisq)])
#plt.plot(cut_hs,absfit,linewidth = 1.5,color = 'red',label='absolute value of lsq')
#eb = plt.errorbar(x,YBAR,yerr=DELY)

fitsig = signal.firwin(150, 0.01)#, f = 1)
fitenv1 = signal.fftconvolve(fitsig, abs(YBAR))
fitenv = fitenv1[:len(abs(YBAR))]
plt.plot(cut_hs, fitenv,linewidth = 1.5,color='green',label='envelope of lsq fit')
plt.legend()

#index = np.argmin(fitenv[:])
index = np.argmin(YBAR[:])
print "i = ",index
ha = cut_hs[index]
print "min ha", ha
declination = cut_dec[index]
print "corresponding dec", declination

plt.plot([ha, ha], [-1.5,1.5], "r--", linewidth = "2")

###### MF THEORETICAL ######
fR = np.linspace(-4,4,10000)
MF = np.zeros(10000)
N = 1000.
for n in np.arange(-N,N+1):
    MF += np.sqrt(1-(n/N)**2)*np.cos(2*np.pi*fR*n/N)

plt.figure(3)
plt.plot(fR,MF,'k')
plt.plot([0.61, 0.61], [-500,2000], "k--", linewidth = "1.5")
plt.plot([1.12, 1.12], [-500,2000], "k--", linewidth = "1.5")
plt.plot([1.62, 1.62], [-500,2000], "k--", linewidth = "1.5")
plt.plot([-4,4], [0,0], "k--", linewidth = "1.5")
plt.xlabel('$f_fR$', fontsize=16)
plt.ylabel('$MF_{theory}$', fontsize=16)
plt.title('Theoretical Modulating Function', fontsize=18)

#### SUN RADIUS ######

Rsun1 = 0.61/(Blmbd/lmbd*np.cos(declination)*np.cos(ha))
Rsun2 = 1.12/(Blmbd/lmbd*np.cos(declination)*np.cos(ha))
Rsun3 = 1.62/(Blmbd/lmbd*np.cos(declination)*np.cos(ha))
Rsun4 = 1.12/(Blmbd/lmbd*np.cos(declination)*np.cos(5.35))

print "1st Rsun = ", np.rad2deg(Rsun1)
print "2nd Rsun = ", np.rad2deg(Rsun2)
print "3rd Rsun = ", np.rad2deg(Rsun3)
print "Rsun compare =", np.rad2deg(Rsun4)

"""
diag_elems = np.dot(np.identity(N),a)
vardc = s_sq*diag_elems
sigma = np.sqrt(vardc)
"""