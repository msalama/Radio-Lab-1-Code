import numpy as np
import pylab as plt

A = np.load('fsig_190000.0.npz')
A.files
A['arr_0']
data1 = A['arr_0']

plt.subplot(221)
plt.plot(data1)
plt.title('$f_{sig-} = 190kHz$')

B = np.load('fsig_210000.0.npz')
B.files
B['arr_0']
data2 = B['arr_0']

print len(data2)
plt.subplot(222)
plt.plot(data2)
plt.title('$f_{sig+} = 210kHz$')

C = np.load('fsig_760000.0.npz')
C.files
C['arr_0']
data3 = C['arr_0']

plt.subplot(223)
plt.plot(data3)
plt.title('$f_{sig-} = 760kHz$')

D = np.load('fsig_840000.0.npz')
D.files
D['arr_0']
data4 = D['arr_0']

plt.subplot(224)
plt.plot(data4)
plt.title('$f_{sig+} = 840kHz$')