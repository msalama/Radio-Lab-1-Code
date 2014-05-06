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

data_dir = "mag-data"
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

def removespikes(data):
    cleaned = el_boxcar(np.load(data)['spec'],5)[8192/2. - 2731:8192/2.]
    return cleaned

freqs_on = np.linspace(f_on + 150 - 6, f_on + 150 + 2, 8192-2731)[8192./2 - 2731:8192./2]
freqs_off = np.linspace(f_off + 150 - 2, f_off + 150 + 6, 8192-2731)[8192./2 - 2731:8192./2]

def get_selector(frequencies):
    return np.where(
        ( (1*(1419.5 < frequencies)) * (1*(frequencies < 1420.2)) ) |
        ((1*(1422.5 < frequencies))  * (1 * (frequencies < 1424.5)) ))

def calibrate(on_noiseoff, on_noiseon, off_noiseoff, off_noiseon):
    on_n = removespikes(on_noiseon)
    on = removespikes(on_noiseoff)
    off_n = removespikes(off_noiseon)
    off = removespikes(off_noiseoff)
    R_on = np.sum(on_n)/np.sum(on)
    R_off = np.sum(off_n)/np.sum(off)
    g = np.mean(on)/np.mean(off)
    
    T_syson = 100/(R_on - 1)
    T_sysoff = 100/(R_off - 1)
    """
    if R_on <= 1.:
        print 'R_on', R_on, 'at', np.load(off_noiseoff)['l'], np.load(off_noiseoff)['b']
        print str(on_noiseon)
    elif R_off <= 1.:
        print 'R_off', R_off, 'at', np.load(off_noiseoff)['l'], np.load(off_noiseoff)['b']
        print str(on_noiseon)
    #else:
    #    print 'yay!'
    """
    T_skyonpre = on/(g*off - 1)*T_syson
    T_skyoffpre = on/(g*off - 1)*T_sysoff
    
    selector_on = get_selector(freqs_on)
    coeffs_on = np.polyfit(np.arange(len(T_skyonpre))[selector_on], T_skyonpre[selector_on], 3)
    p = np.poly1d(coeffs_on)
    fit_on = p(np.arange(len(T_skyonpre)))
    
    selector_off = get_selector(freqs_off)
    coeffs_off = np.polyfit(np.arange(len(T_skyoffpre))[selector_off], T_skyonpre[selector_off], 3)
    p = np.poly1d(coeffs_off)
    fit_off = p(np.arange(len(T_skyoffpre)))
    
    T_skyon = T_skyonpre - p(np.arange(len(T_skyonpre)))
    T_skyoff = T_skyoffpre - p(np.arange(len(T_skyoffpre)))
    
    T_sky = (T_skyon + T_skyoff)/2
    
    #T_skypre = (T_skyonpre + T_skyoffpre)/2
    
    #fit = (fit_on + fit_off)/2
    
    lpt = np.load(on_noiseoff)['l']
    bpt = np.load(on_noiseoff)['b']
    return T_sky, lpt, bpt#, T_skyoffpre, fit_off, lpt, bpt

#T_sky, T_skypre, fit = calibrate(on, on_n, off, off_n)

def allspectra(number = len(array_files)):
    T_sky = []
    for files in range(number):            
        datafile = array_files[files]
        T_sky1, lpt, bpt= calibrate(datafile[1], datafile[3], datafile[0], datafile[2])
        T_sky.append(T_sky1)
    return T_sky

def allpointings(number = len(array_files)):
    lpt = []
    bpt = []
    for files in range(number):            
        datafile = array_files[files]
        lpt1, bpt1= calibrate(datafile[1], datafile[3], datafile[0], datafile[2])
        lpt.append(lpt1)
        bpt.append(bpt1)
    return lpt, bpt

def newlist(x, y, z):  
    D = defaultdict(list)
    for i,item in enumerate(x):
        D[item].append(i)
    D = {k:v for k,v in D.items() if len(v)>1}
    E = defaultdict(list)
    for i,item in enumerate(y):
        E[item].append(i)
    E = {k:v for k,v in E.items() if len(v)>1}
    for key in D.keys():
        for key1 in E.keys():
            ind = []
            for i in range(len(D[key])):
                for j in range(len(E[key1])):
                    if D[key][i] == E[key1][j]:
                        ind.append(D[key][i])
                        if ind[0] != ind[(len(ind)-1)]:
                            z[ind[0]] = np.array(z[ind[0]]) + np.array(z[ind[len(ind)-1]])
    return z

allfreqs = np.linspace(f_off + 150 - 2, f_off + 150 + 6, 8192)
uncut = np.load('lo-1269.6_05-02-2014_093559.npz')['spec']
uncut2 = np.load('lo-1273.6_05-02-2014_093233.npz')['spec']
data = np.load('lo-1269.6_05-02-2014_093559.npz')['spec'][8192/2. - 2731:8192/2.]
data2 = np.load('lo-1273.6_05-02-2014_093233.npz')['spec'][8192/2. - 2731:8192/2.]
datanew = removespikes('lo-1269.6_05-02-2014_093559.npz')
datanew2 = removespikes('lo-1273.6_05-02-2014_093233.npz')
Nss = np.load('lo-1269.6_05-02-2014_093559.npz')['N']

longitude = np.load('lo-1269.6_05-02-2014_093559.npz')['l']
latitude = np.load('lo-1269.6_05-02-2014_093559.npz')['b']
print longitude, latitude
ticks1 = np.arange(1417,1426,1)
ticks = np.arange(1419.5,1424.5,0.5)

plt.figure()
plt.subplot(211)
plt.plot(allfreqs,uncut)
plt.plot(allfreqs,uncut2)
plt.xlabel('Frequencies [$MHz$]')
plt.ylabel('Count')
plt.xticks(ticks1,ticks1)
plt.title('(58.808, -76.0) Observed on 5/2/2014 at 9:35:59')
plt.subplot(212)
plt.plot(freqs_off, data)
plt.plot(freqs_off, data2)
plt.plot(freqs_off, datanew, color = 'red')
plt.plot(freqs_off, datanew2, color = 'red')
plt.xlabel('Frequencies [$MHz$]')
plt.ylabel('Count')
plt.xticks(ticks,ticks)
plt.title

