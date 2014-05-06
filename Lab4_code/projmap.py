import numpy as np
#np.seterr("raise")
from pylab import *
import matplotlib.pyplot as plt
import glob
import os

### All coordinates mapping space to observe
coord = np.load('coordinates.npz')
l = coord['lon']
b = coord['lat']

### Points observed so far
data_dir = "mag-data"
point_dirs = glob.glob(os.path.join(data_dir, "*"))
array_files = []
for point_dir in point_dirs:
    array_file = glob.glob(os.path.join(point_dir, "*.npz"))
    array_files.append(array_file)
file1 = []
for firstfile in array_files:
    file1.append(firstfile[0])

lpt = []
bpt = []
for files in file1:
    coord = np.load(files)
    lpt.append(coord['l'])
    bpt.append(coord['b'])

np.savez('obscoords.npz', lpt = lpt, bpt = bpt)

figure()
ax = plt.subplot(111, polar=True)
ax.plot(np.deg2rad(l), b, 'o', linewidth=3)
bpts = np.array(bpt)
lpts = np.array(lpt)
ax.plot(np.deg2rad(lpts), bpts, 'ro', linewidth=3,label='Observed')
ax.legend(loc='lower left')
ax.set_ylim(-90,-60)
ax.set_yticks(np.arange(-90,-40,15))
ax.grid(True)
ax.set_title("Sampled points in Galactic Sphere", va='bottom')
