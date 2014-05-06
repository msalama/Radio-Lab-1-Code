import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#import QuTiP


npts = 10000
theta = 2*np.pi* np.random.rand(npts)
nu = 2.*np.random.rand(npts) - 1.
phi = np.arccos(nu) 
x = np.sin(phi)*np.cos(theta)
y = np.sin(phi)*np.sin(theta)
z = np.cos(phi) 

#Magellanic Stream Coordinates
coord = np.load('coordinates.npz')

l = coord['lon']
b = coord['lat']

msx = np.sin(np.deg2rad(b+270))*np.cos(np.deg2rad(l))
msy = np.sin(np.deg2rad(b+270))*np.sin(np.deg2rad(l))
msz = np.cos(np.deg2rad(b+270)) 

fig3d = plt.figure()
ax = Axes3D(fig3d, azim = -30, elev =  20)    #azimuth & elevation for viewing of the plot
#ax.plot(x,y,z,'o')
ax.plot(msx,msy,msz,'o')
plt.xlabel('x')
plt.ylabel('y')
ax.set_alpha(0.25)
plt.title('3D Representation of Sampling of Magellanic Stream')
#ax.set_aspect('equal')

#b = Bloch()