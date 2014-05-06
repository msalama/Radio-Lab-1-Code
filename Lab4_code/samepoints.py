import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import glob
import os
from collections import Counter
from collections import defaultdict

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
    
on_noiseon = []
on_noiseoff = []
off_noiseon = []
off_noiseoff = []
lpt = []
bpt = []
for files in range(len(array_files)/14):
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

for i in range(len(on_noiseon)):
    on = np.mean(on_noiseon[i])/np.mean(on_noiseoff[i])
    off = np.mean(off_noiseon[i])/np.mean(off_noiseoff[i])
    
    g_on = on_noiseon[i] - on_noiseoff[i]
    g_off = off_noiseon[i] - off_noiseoff[i]
    R_g = g_on/g_off
    g = np.mean(R_g)
    
    T_syson = T_noise/(on - 1)
    T_sysoff = T_noise/(off -1)
        
    T_sky = (on_noiseoff[i]/(g*off_noiseoff[i])-1)*T_sysoff

mylist = [20,30, 25, 20, 30, 20, 30, 20,30]
mylist2 = [1,2, 3, 1, 4, 7, 2, 1,2]
#mylist3 = [23, 45, 11, 29, 15, 60, 5, 3,11]
mylist3 = [[23,1,2], [45,2,3], [11,5,5], [29,9,8], [15,1,1], [60,1,4], [5,3,2], [3,1,7],[11,1,9]]
rep = [k for k,v in Counter(mylist).items() if v>1]
rep2 = [k for k,v in Counter(mylist2).items() if v>1]
"""
def newlist(x, y, z):  
    D = defaultdict(list)
    for i,item in enumerate(x):
        D[item].append(i)
    D = {k:v for k,v in D.items() if len(v)>1}
    E = defaultdict(list)
    for i,item in enumerate(y):
        E[item].append(i)
    E = {k:v for k,v in E.items() if len(v)>1}
    #ind = []
    for key in D.keys():
        for key1 in E.keys():
            print 'lpt: ', key, D[key]
            print 'bpt: ', key1, E[key1]
            ind = []
            for i in range(len(D[key])):
                for j in range(len(E[key1])):
                    if D[key][i] == E[key1][j]:
                        print D[key][i], '=', E[key1][j]
                        ind.append(D[key][i])
                        print 'ind:', ind
                        #for i in range(len(D[key])):
                        #for i in ind:
                        print 'ind[0]:', ind[0]
                        print 'len(ind):', len(ind)
                        print 'ind[len(ind)-1]:', ind[len(ind)-1]
                        z[D[key][ind[0]]] += z[E[key1][ind[len(ind)-1]]]
                            #print 'newlist =', mylist3
                    #if D[key] != E[key1]:
                        #print D[key], '=/=', E[key1]
    return ind,z
""" 
"""  
D = defaultdict(list)
for i,item in enumerate(mylist):
    D[item].append(i)
D = {k:v for k,v in D.items() if len(v)>1}
E = defaultdict(list)
for i,item in enumerate(mylist2):
    E[item].append(i)
E = {k:v for k,v in E.items() if len(v)>1}
#ind = []
for key in D.keys():
    for key1 in E.keys():
        print 'lpt: ', key, D[key], 'bpt: ', key1, E[key1]
        ind = []
        for i in range(len(D[key])):
            for j in range(len(E[key1])):
                if D[key][i] == E[key1][j]:
                    print D[key][i], '=', E[key1][j]
                    ind.append(D[key][i])
                    print 'ind:', ind
                    print 'ind[0]:', ind[0]
                    print 'len(ind):', len(ind)
                    print 'ind[len(ind)-1]:', ind[len(ind)-1]
                    print 'key:', key
                    print 'key1', key1
                    if ind[0] != ind[(len(ind)-1)]:
                        print ind[0], '=/=', ind[(len(ind)-1)]
                        print '1st + 2nd','=', mylist3[ind[0]], '+', mylist3[ind[len(ind)-1]]
                        #mylist3[ind[0]] = mylist3[ind[0]] + mylist3[ind[len(ind)-1]]
                        mylist3[ind[0]] = np.array(mylist3[ind[0]]) + np.array(mylist3[ind[len(ind)-1]])
                        print 'new', mylist3[ind[0]]
                        print '--------'
print 'new list = ', mylist3
"""
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