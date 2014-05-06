import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import glob
import os
#from scipy import signal

f_off = 1269.6 #MHz
f_on = 1273.6 #MHz
#tau = 2min
T_noise = 100 #K

data_dir = "../../mag-stream/data"
point_dirs = glob.glob(os.path.join(data_dir, "*"))

array_files = []
for point_dir in point_dirs:
    array_file = glob.glob(os.path.join(point_dir, "*.npz"))
    array_files.append(array_file)

def el_boxcar(x, width):
    medianed = np.zeros(len(x))
    x = list(x)
    for i in range(len(x)):
        boxcar = x[max(0, i-width/2):i+width/2]
        medianed[i] = np.median(boxcar)
    return medianed   
    
on_noiseon = []
on_noiseoff = []
off_noiseon = []
off_noiseoff = []
lpt = []
bpt = []
#for files in range(len(array_files)/14):
#for files in range(10,15):
for files in range(len(array_files)):
    datafile = array_files[files]
    boxed0 = el_boxcar(np.load(datafile[0])['spec'],5)
    off_noiseoff.append(boxed0[8192/2. - 2731:8192/2.])
    boxed1 = el_boxcar(np.load(datafile[1])['spec'],5)
    on_noiseoff.append(boxed1[8192/2. - 2731:8192/2.])
    boxed2 = el_boxcar(np.load(datafile[2])['spec'],5)
    off_noiseon.append(boxed2[8192/2. - 2731:8192/2.])
    boxed3 = el_boxcar(np.load(datafile[3])['spec'],5)
    on_noiseon.append(boxed3[8192/2. - 2731:8192/2.])
    lpt.append(np.load(datafile[0])['l'])
    bpt.append(np.load(datafile[0])['b'])

freqsall = np.linspace(f_on + 150 - 6, f_on + 150 + 2, 8192 - 2731)
freqs = freqsall[8192/2 - 2731:8192/2]

T_sky = []
for i in range(len(on_noiseon)):
    on = np.mean(on_noiseon[i])/np.mean(on_noiseoff[i])
    off = np.mean(off_noiseon[i])/np.mean(off_noiseoff[i])
    
    g_on = on_noiseon[i] - on_noiseoff[i]
    g_off = off_noiseon[i] - off_noiseoff[i]
    R_g = g_on/g_off
    g = np.mean(R_g)
    
    T_syson = T_noise/(on - 1)
    T_sysoff = T_noise/(off -1)
    if T_sysoff < 0:
        print lpt[i], bpt[i]    
    T_sky1 = (on_noiseoff[i]/(g*off_noiseoff[i])-1)*T_sysoff
    #if max(T_sky1) < 0:
    #    print 'alert!',lpt[i], bpt[i] 
    T_sky.append(T_sky1)

for i in range(len(T_sky)):  
    plt.plot(freqs, T_sky[i],label = (str(lpt[i]),str(bpt[i])))
    plt.ylabel('$T_{antHI}(/nu) [K]$')
    plt.xlabel('Frequency [$MHz$]')
    plt.legend()
"""    
    M = len(T_sky)
    N = 2
    repeats = 50
    Y = np.ones((M,),dtype=float)
    Y[:] = T_sky #[Mx1]: y values    
    
    #initial guess for parameters:
    A0 = 5. #amplitude
    B0 = 0.6 #frequency
    Y0 = np.sin(A0*freqs) + B0*freqs
    dA = 0
    dB = 0
    
    #i = 0
    #for i in range(repeats):
    #print "i: ", i
    A0new = A0 + dA
    B0new = B0 + dB
    #print "new A: ", A
    #in python: (col,row)
    X = np.ones((2,M),dtype = float)
    X[1,:] = freqs
    X[0] = freqs*np.cos(A0new*freqs)
    X = np.transpose(X) #[MxN]: s values in col1 and t values in col2
    #print "new X", X
    # alpha: [NxN]: normal equation
    XX = np.dot(np.transpose(X),X)
    # beta: [Nx1]: y values multiplied by s(row1) and t(row2) values
    XY = np.dot(np.transpose(X),Y)
    #inverse alpha
    XXI = np.linalg.inv(XX)
    #a: [Nx1]: parameter values
    a = np.dot(XXI,XY)
    #print "new a", a
    dA = a[0]
    dB = a[1]
    #print "new dA", dA
    #print "dA/A0 = ", dA/A0
    #print "dA/A = ", dA/A0new

    #y-bar: new y values
    YBAR = np.dot(X,a)-Y0
    #print "new YBAR", YBAR

    #plt.figure()
    #plt.plot(x,y,'g')
    plt.xlabel('freqs')
    plt.ylabel('T_sky')
    plt.plot(freqs,YBAR,'blue')#,linewidth=3)
"""  
#plt.show()
