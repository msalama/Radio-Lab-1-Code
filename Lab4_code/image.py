import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import signal

####### All points
coord = np.load('coordinates.npz')

l = coord['lon']
b = coord['lat']
N = coord['N']

msx = np.sin(np.deg2rad(b))*np.cos(np.deg2rad(l))
msy = np.sin(np.deg2rad(b))*np.sin(np.deg2rad(l))
x = (b+90)*msx
y = (b+90)*msy

######## Observable points
obscoords = np.load('obscoords.npz')
lpt = obscoords['lpt']
bpt = obscoords['bpt']

obsmsx = np.sin(np.deg2rad(bpt))*np.cos(np.deg2rad(lpt))
obsmsy = np.sin(np.deg2rad(bpt))*np.sin(np.deg2rad(lpt))
obsx = (bpt+90)*obsmsx
obsy = (bpt+90)*obsmsy

######## Projection Plots
plt.figure()
plt.plot(obsx,obsy,'go',alpha= 0.5,markersize = 3,label = 'observed points')
plt.legend()
plt.xlim(-30,15)
plt.ylim(-30,15)
plt.plot([-100, 100], [0,0], 'white', linewidth = "0.8")
plt.plot([0, 0], [-100,100], 'white', linewidth = "0.8")
a = np.linspace(-30,15)
b = np.linspace(-30,15)
plt.plot(a,b,'white', linewidth = "0.8")
plt.plot(a,-b,'white', linewidth = "0.8")
plt.tick_params(axis='both',bottom='off',top='off',left='off',right='off',labelbottom='off',labelleft='off')

b75 = plt.Circle((0,0),15.*np.cos(15*np.pi/180),fill=False,color = 'white')
b60 = plt.Circle((0,0),30.*np.cos(30*np.pi/180),fill=False,color = 'white')
fig = plt.gcf()
fig.gca().add_artist(b75)
fig.gca().add_artist(b60)
ax=plt.gca()
ax.set_xlim((-30,15))
ax.set_ylim((-30,15))
plt.text(0,0, '$-90^{o}$',color = 'white')
plt.text(-15.*np.cos(15*np.pi/180)-4,-15.*np.sin(15*np.pi/180), '$-75^{o}$',color = 'white')
plt.text(-30.*np.cos(30*np.pi/180)-3,-30.*np.sin(15*np.pi/180), '$-60^{o}$',color = 'white')
plt.text(-29,0, '$0^{o}$',color = 'white')
plt.text(-25,-27, '$45^{o}$',color = 'white')
plt.text(-5,28, '$-90^{o}$',color = 'white')
plt.text(1,-29, '$90^{o}$',color = 'white')
plt.text(3,6,'$longitude$',color = 'white', size = 14)
plt.text(-23,10,'$latitude$',color = 'white',size = 14)
plt.text(11,0, '$180^{o}$',color = 'white')


######### IMAGE ##############

IMG = np.zeros((300,300),dtype= float)
WGHT = np.zeros((300,300),dtype= float)

lons = np.load('peaks.npz')['lons']
lats = np.load('peaks.npz')['lats']
Ns = np.load('peaks.npz')['N']

Nmsx = np.sin(np.deg2rad(lats))*np.cos(np.deg2rad(lons))
Nmsy = np.sin(np.deg2rad(lats))*np.sin(np.deg2rad(lons))
Nx = (lats+90)*Nmsx
Ny = (lats+90)*Nmsy

xind = []
yind = []
for i in Nx:
    xind.append(np.around(i)/0.2+150)
for i in Ny:
    yind.append(np.around(i)/0.2+150)
    
indices = np.indices((len(x),len(y)))

peaks = np.load('peaks.npz')['peaks']
"""
for xi,yi,peaki in zip(xind,yind,peaks):
    IMG[yi,xi] += peaki

for xi,yi,Ni in zip(xind,yind,N):
    IMG[yi,xi] += Ni
"""
N_col = np.load('N_col.npz')['N_HI']

for xi,yi,peaki in zip(xind,yind,N_col):
    IMG[yi,xi] += peaki

for xi,yi,Ni in zip(xind,yind,Ns):
    WGHT[yi,xi] += Ni
    
###########################
# The following makeGaussian function was taken from:
# http://stackoverflow.com/questions/7687679/how-to-generate-2d-gaussian-with-python
def makeGaussian(size, fwhm = 3, center=None):
    """ Make a square gaussian kernel.   
    size is the length of a side of the square
    fwhm is full-width-half-maximum, which
    can be thought of as an effective radius.
    """
    x = np.arange(0, size, 1, float)
    y = x[:,np.newaxis]
    if center is None:
        x0 = y0 = size // 2
    else:
	x0 = center[0]
        y0 = center[1]
    return np.exp(-4*np.log(2) * ((x-x0)**2 + (y-y0)**2) / fwhm**2)
###########################

#kernel = makeGaussian(60,fwhm = 20)
kernel = makeGaussian(60,fwhm = 20)

result_img = scipy.signal.convolve2d(IMG,kernel)
result_wght = scipy.signal.convolve2d(WGHT,kernel)

for xi in range(len(result_img)):
    for yi in range(len(result_img)):
        if result_img[yi,xi] <= 1/1000.:
            result_img[yi,xi]+= 0
            result_wght[yi,xi]+= 1

###Check will not be dividing by zero:
for xi in range(len(result_img)):
    for yi in range(len(result_img)):
        if result_wght[yi,xi] == 0:
            print yi,xi
             
fin_img = result_img/result_wght         

plt.imshow(fin_img,origin='lower',interpolation = 'nearest',cmap = 'hot', extent = (-30,30,-30,30))#,vmin=0,vmax=7)
plt.colorbar()
plt.title('Map of Column Densities of HI')

#plt.figure()
#plt.imshow(IMG,origin='lower',interpolation = 'nearest',cmap = 'hot', extent = (-30,30,-30,30))#,vmin=0,vmax=7)
