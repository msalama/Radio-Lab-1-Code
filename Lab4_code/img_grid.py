import numpy as np
import pylab as plt
#from astropy.convolution import convolve, convolve_fft, Gaussian2DKernel
#from scipy import signal
import scipy
data = np.loadtxt('img_grid_data.txt')

xraw = data[:,0]
yraw = data[:,1]
z = data[:,2]

plt.plot(xraw,yraw,'o')
plt.xlabel('x')
plt.ylabel('y')

x = []
y = []
for i in xraw:
    x.append(np.around(i))
for i in yraw:
    y.append(np.around(i))

IMG = np.zeros((10,10),dtype = float)
coords = np.indices((10,10))

for xi,yi,zi in zip(x,y,z):
    IMG[xi,yi] += zi

#kernel = Gaussian2DKernel(width=2)
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

kernel = makeGaussian(2)

result = scipy.signal.convolve2d(IMG,kernel)


"""  
plt.figure()   
plt.plot(xraw,yraw)
plt.plot(xraw,result)
plt.imshow(IMG,origin='lower',interpolation = 'nearest',cmap = 'hot', extent = (-2,10,-2,10))#,vmin=2,vmax=6)
plt.colorbar()
"""
#different colormaps: jet, hot
