import numpy as np
import pickle
import pylab as plt

F_OFF = 1269.6
F_ON = 1273.6

C = 299792458.                   # Speed of light in m/s
LAMBDA_H1 = 0.2110611405413     # Wavelength of H1 emissions in m
NU_H1 = C / LAMBDA_H1
km = 1000.


def get_selector(frequencies):
    return np.where(
        ( (1*(1419.5 < frequencies)) * (1*(frequencies < 1420.2)) ) |
        ((1*(1423. < frequencies))  * (1 * (frequencies < 1424.5)) ))


count = 8192
freqs_full = np.linspace(F_ON + 150 - 6, F_ON + 150 + 6, count)
freqs_full_off = np.linspace(F_OFF + 150 - 6, F_OFF + 150 + 6, count)
freqs_on = np.linspace(F_ON + 150 - 6, F_ON + 150 + 2, count-2731)[count/2 - 2731:count/2]
freqs_off = np.linspace(F_OFF + 150-2, F_OFF + 150 + 6, count-2731)[count/2 - 2731:count/2]
freqs = np.linspace(F_ON + 150 - 6, F_ON + 150 + 2, count-2731)[count/2 - 2731:count/2]


def el_boxcar(x, width):
    medianed = np.zeros(len(x))
    x = list(x)
    for i in range(len(x)):
        boxcar = x[max(0, i-width/2):i+width/2]
        medianed[i] = np.median(boxcar)
    return medianed


def calibrate(on, on_n, off, off_n):
    count = len(on)  # 8192

    # on half
    on1 = on[count/2-2731:count/2]
    onn1 = on_n[count/2-2731:count/2]
    off1 = off[count/2-2731:count/2]
    offn1 = off_n[count/2-2731:count/2]

    T_sys_on = 100. / (np.sum(onn1) / np.sum(on1) - 1.)
    gonoff = np.mean(on1) / np.mean(off1)

    T_sky = (((on1 / gonoff / off1) - 1.0) * T_sys_on)

    selector = get_selector(freqs_on)
    coeffs = np.polyfit(np.arange(len(T_sky))[selector], T_sky[selector], 3)
    p = np.poly1d(coeffs)
    
    T_sky_on = T_sky - p(np.arange(len(T_sky)))
    #plt.plot(T_sky)
    #plt.plot(p(np.arange(len(T_sky))))
    
    # off half
    on1 = off[count/2:count/2+2731]
    onn1 = off_n[count/2:count/2+2731]
    off1 = on[count/2:count/2+2731]
    offn1 = on_n[count/2:count/2+2731]

    T_sys_off = 100. / (np.sum(onn1) / np.sum(on1) - 1.)
    gonoff = np.mean(on1) / np.mean(off1)

    T_sky = (((on1 / gonoff / off1) - 1.0) * T_sys_off)

    selector = get_selector(freqs_off)
    coeffs = np.polyfit(np.arange(len(T_sky))[selector], T_sky[selector], 3)
    p = np.poly1d(coeffs)

    T_sky_off = T_sky - p(np.arange(len(T_sky)))

    # average the two halfs
    return (T_sky_on + T_sky_off) / 2.0


stuff = pickle.load(open("specs.pkl", "rb"))

points = len(stuff)
lons = np.zeros(points)
lats = np.zeros(points)
spectras = []
NN = []

for i, ((lon, lat), Nspecs) in enumerate(stuff.items()):
    lons[i] = lon
    lats[i] = lat
    spec = []
    the_N = 0
    for N, (on, on_n, off, off_n) in Nspecs:
        result = calibrate(on, on_n, off, off_n)
        if not len(spec):
            spec = result
        else:
            spec = (the_N * spec + N * result) / (the_N + N)
        the_N += N
        #print the_N
    NN.append(the_N/179) 
    spectras.append(spec)
 
def peak_selector(frequencies):
    return np.where(
        ( (1*(1420.2 < frequencies)) * (1*(frequencies < 1423.)) ))

ticks = np.arange(1419.5,1424.5,0.5)    
plt.figure()   
for i in range(len(spectras)):
    plt.plot(freqs_on,spectras[i])#,label = (str(lons[i]),str(lats[i])))
    plt.xlabel('[Frequency $MHz$]')
    plt.ylabel('$T_{sky}$ [$K$]')
    plt.xticks(ticks,ticks)
    plt.title('$T_{sky}$ spectra of Magellanic Stream')
    plt.plot([1420.879,1420.879],[-5,25],'k',linewidth = '1')
    plt.text(1420.979,20, '$f_{min}$',size = 16)    
    plt.plot([1422.3,1422.3],[-5,25],'k',linewidth = '1')
    plt.text(1422.4,20, '$f_{max}$',size = 16)
    plt.legend()

def peakfinder(data):
    peaks = []
    for i in range(len(spectras)):
       selector = peak_selector(freqs_on)
       spec = data[i]
       peaks.append(max(spec[selector]))
    return peaks

np.savez('T_skys.npz', T_sky = spectras,freqs = freqs_on, lons = lons, lats = lats, N = NN)
np.savez('peaks.npz', peaks = peakfinder(spectras),lons = lons, lats = lats, N = NN)