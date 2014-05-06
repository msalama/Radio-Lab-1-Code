import numpy as np

lmbda = 0.2110611405413 #m 
c = 2.99792458*10**8 #m/s
f_0 = c/lmbda #Hz
print 'f_0 = ', f_0/10**6, " MHz"

vmin = -400 #km/s
vmax = -100 #km/s

fmax = (1-(vmin/c)*1000.)*f_0/10**6
print 'fmax = ', fmax, " MHz", " at ",vmin,"km/s"
fmin = (1-(vmax/c)*1000.)*f_0/10**6
print 'fmin = ', fmin, " MHz", " at ",vmax,"km/s"
fmid = (fmax + fmin)/2
print 'fmid', fmid, " MHz"

print "delf = ", fmax - fmin , " MHz"
delf2 = (vmax -vmin)/c/1000.*f_0
print 'delf2', delf2

print f_0/10**6 + delf2

######## Column density

T_sky = np.load('T_skys.npz')['T_sky']
f = np.load('T_skys.npz')['freqs']
v = c * f_0 * (1 - f/f_0)/10**6

def coldens(velocity, data):
    N_HI = 0
    for vel,T in zip(velocity,data):
        N_HI += 1.8*10**8*T*vel
    return N_HI

N_COL = []
for i in range(len(T_sky)):
    N_col = coldens(v,T_sky[i])
    N_COL.append(N_col)
    
np.savez('N_col.npz',N_HI = N_COL)