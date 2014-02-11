import numpy as np
import matplotlib.pyplot as plt
from math import *

npts = 10000 # number of elements in each sample
N = 1000000
def CLT(N):
    averages = []
    for i in range(N):
        #print "N =", i+1
        x_i = np.random.rand(npts)
        #print "initial sample:", x_i
        mu_i = np.mean(x_i)
        averages.append(mu_i)
        #print "mean =", mu_i
        s_i = sqrt(np.mean((x_i)**2) - (np.mean(x_i))**2)
        #print "std dev = ", s_i
    return averages

plt.figure(1)
plt.hist(CLT(N),bins=50, normed=True)
plt.xlabel('Average')
plt.ylabel('Count')
plt.title('Frequency of averages')