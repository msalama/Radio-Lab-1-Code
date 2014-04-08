import numpy as np
import pylab as plt

lsqdata = np.load('ay121_lsq_data.npz')['arr_0']
plt.plot(lsqdata)