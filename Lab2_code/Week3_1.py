import numpy as np
import pylab as plt

########### Ideal ###########

no_sig1 = np.array(range(-150,-62))
zero = []
for i in no_sig1:
    zero.append (0)
sig = np.array(range(-62,63))
one = []
for i in sig:
    one.append(1)
no_sig2 = np.array(range(63,150))
zeroo = []
for i in no_sig2:
    zeroo.append(0)

f_ideal = np.array (range(-150,150))
out_ideal = zero + one + zeroo

plt.figure(1)
plt.plot(f_ideal, out_ideal, 'red', linewidth = 2, label='Ideal Bandpass Filter')
plt.ylim(-0.05,1.5)
plt.xlabel('Frequency [MHz]',fontsize = 14)
plt.ylabel('Normalized Power Output', fontsize = 14)
plt.legend()

########### Discrete ###########

discrete_nosig = np.array(range(-100,-63,25))
#print discrete_nosig
discrete_sig = np.array(range(-50,63,25))
#print discrete_sig
discrete_nosig2 = np.array(range(75,100,25))
#print discrete_nosig2

f_discrete = np.array(range(-100,100,25))
#print "fdiscrete",f_discrete

discrete_zero = []
for i in discrete_nosig:
    discrete_zero.append (0)
discrete_one = []
for i in discrete_sig:
    discrete_one.append (1)    
discrete_zeroo = []
for i in discrete_nosig2:
    discrete_zeroo.append (0)    
out_discrete = discrete_zero + discrete_one + discrete_zeroo
#print "out_discrete", out_discrete

plt.plot(f_discrete, out_discrete, 'green', linewidth = 2, label="Discrete Bandpass Filter")
plt.legend()

########### Theoretical ###########

def fix(fftoutput):
    """corrects for order of values in array"""
    half = len(fftoutput)/2
    return np.array(list(fftoutput[half:]) + list(fftoutput[:half]))

discrete_fft = np.fft.ifft(fix(out_discrete))

full_range = np.array([0] * 60 + list(fix(discrete_fft)) + [0] * 60)

measured_filter = np.fft.fft(full_range)
plt.plot(fix(np.fft.fftfreq(len(measured_filter), 1/200.)), fix(abs(measured_filter)**2), "--", color = "0.1", linewidth=2, label="Computed Prediction Filter")
plt.legend()

#################### Experimental #######################

#load all the data (filtered and unfiltered)
lo4_real = np.fromfile('FIR-lo-4/ddc_real_bram','>i')
lo4_imag = np.fromfile('FIR-lo-4/ddc_imag_bram','>i')
unflo4_real = np.fromfile('norm-lo-4/ddc_real_bram','>i')
unflo4_imag = np.fromfile('norm-lo-4/ddc_imag_bram','>i')
lo16_real = np.fromfile('FIR-lo-16/ddc_real_bram','>i')
lo16_imag = np.fromfile('FIR-lo-16/ddc_imag_bram','>i')
unflo16_real = np.fromfile('norm-lo-16/ddc_real_bram','>i')
unflo16_imag = np.fromfile('norm-lo-16/ddc_imag_bram','>i')
lo32_real = np.fromfile('FIR-lo-32/ddc_real_bram','>i')
lo32_imag = np.fromfile('FIR-lo-32/ddc_imag_bram','>i')
unflo32_real = np.fromfile('norm-lo-32/ddc_real_bram','>i')
unflo32_imag = np.fromfile('norm-lo-32/ddc_imag_bram','>i')
lo40_real = np.fromfile('FIR-lo-40/ddc_real_bram','>i')
lo40_imag = np.fromfile('FIR-lo-40/ddc_imag_bram','>i')
unflo40_real = np.fromfile('norm-lo-40/ddc_real_bram','>i')
unflo40_imag = np.fromfile('norm-lo-40/ddc_imag_bram','>i')
lo46_real = np.fromfile('FIR-lo-46/ddc_real_bram','>i')
lo46_imag = np.fromfile('FIR-lo-46/ddc_imag_bram','>i')
unflo46_real = np.fromfile('norm-lo-46/ddc_real_bram','>i')
unflo46_imag = np.fromfile('norm-lo-46/ddc_imag_bram','>i')
lo48_real = np.fromfile('FIR-lo-48/ddc_real_bram','>i')
lo48_imag = np.fromfile('FIR-lo-48/ddc_imag_bram','>i')
unflo48_real = np.fromfile('norm-lo-48/ddc_real_bram','>i')
unflo48_imag = np.fromfile('norm-lo-48/ddc_imag_bram','>i')
lo50_real = np.fromfile('FIR-lo-50/ddc_real_bram','>i')
lo50_imag = np.fromfile('FIR-lo-50/ddc_imag_bram','>i')
unflo50_real = np.fromfile('norm-lo-50/ddc_real_bram','>i')
unflo50_imag = np.fromfile('norm-lo-50/ddc_imag_bram','>i')
lo56_real = np.fromfile('FIR-lo-56/ddc_real_bram','>i')
lo56_imag = np.fromfile('FIR-lo-56/ddc_imag_bram','>i')
unflo56_real = np.fromfile('norm-lo-56/ddc_real_bram','>i')
unflo56_imag = np.fromfile('norm-lo-56/ddc_imag_bram','>i')
lo64_real = np.fromfile('FIR-lo-64/ddc_real_bram','>i')
lo64_imag = np.fromfile('FIR-lo-64/ddc_imag_bram','>i')
unflo64_real = np.fromfile('norm-lo-64/ddc_real_bram','>i')
unflo64_imag = np.fromfile('norm-lo-64/ddc_imag_bram','>i')

lo4_complex = lo4_real + 1j*lo4_imag
lo4_ft = np.fft.fft(lo4_complex)
unflo4_complex = unflo4_real + 1j*unflo4_imag
unflo4_ft = np.fft.fft(unflo4_complex)

lo16_complex = lo16_real + 1j*lo16_imag
lo16_ft = np.fft.fft(lo16_complex)
unflo16_complex = unflo16_real + 1j*unflo16_imag
unflo16_ft = np.fft.fft(unflo16_complex)

lo32_complex = lo32_real + 1j*lo32_imag
lo32_ft = np.fft.fft(lo32_complex)
unflo32_complex = unflo32_real + 1j*unflo32_imag
unflo32_ft = np.fft.fft(unflo32_complex)

lo40_complex = lo40_real + 1j*lo40_imag
lo40_ft = np.fft.fft(lo40_complex)
unflo40_complex = unflo40_real + 1j*unflo40_imag
unflo40_ft = np.fft.fft(unflo40_complex)

lo46_complex = lo46_real + 1j*lo46_imag
lo46_ft = np.fft.fft(lo46_complex)
unflo46_complex = unflo46_real + 1j*unflo46_imag
unflo46_ft = np.fft.fft(unflo46_complex)

lo48_complex = lo48_real + 1j*lo48_imag
lo48_ft = np.fft.fft(lo48_complex)
unflo48_complex = unflo48_real + 1j*unflo48_imag
unflo48_ft = np.fft.fft(unflo48_complex)

lo50_complex = lo50_real + 1j*lo50_imag
lo50_ft = np.fft.fft(lo50_complex)
unflo50_complex = unflo50_real + 1j*unflo50_imag
unflo50_ft = np.fft.fft(unflo50_complex)

lo56_complex = lo56_real + 1j*lo56_imag
lo56_ft = np.fft.fft(lo56_complex)
unflo56_complex = unflo56_real + 1j*unflo56_imag
unflo56_ft = np.fft.fft(unflo56_complex)

lo64_complex = lo64_real + 1j*lo64_imag
lo64_ft = np.fft.fft(lo64_complex)
unflo64_complex = unflo64_real + 1j*unflo64_imag
unflo64_ft = np.fft.fft(unflo64_complex)

########################### Negative ########################################

lo4_complex_m = lo4_real - 1j*lo4_imag
lo4_ft_m = np.fft.fft(lo4_complex_m)

lo16_complex_m = lo16_real - 1j*lo16_imag
lo16_ft_m = np.fft.fft(lo16_complex_m)

lo32_complex_m = lo32_real - 1j*lo32_imag
lo32_ft_m = np.fft.fft(lo32_complex_m)

lo40_complex_m = lo40_real - 1j*lo40_imag
lo40_ft_m = np.fft.fft(lo40_complex_m)

lo46_complex_m = lo46_real - 1j*lo46_imag
lo46_ft_m = np.fft.fft(lo46_complex_m)

lo48_complex_m = lo48_real - 1j*lo48_imag
lo48_ft_m = np.fft.fft(lo48_complex_m)

lo50_complex_m = lo50_real - 1j*lo50_imag
lo50_ft_m = np.fft.fft(lo50_complex_m)

lo56_complex_m = lo56_real - 1j*lo56_imag
lo56_ft_m = np.fft.fft(lo56_complex_m)

lo64_complex_m = lo64_real - 1j*lo64_imag
lo64_ft_m = np.fft.fft(lo64_complex_m)

unflo4_complex_m = unflo4_real - 1j*unflo4_imag
unflo4_ft_m = np.fft.fft(unflo4_complex_m)

unflo16_complex_m = unflo16_real - 1j*unflo16_imag
unflo16_ft_m = np.fft.fft(unflo16_complex_m)

unflo32_complex_m = unflo32_real - 1j*unflo32_imag
unflo32_ft_m = np.fft.fft(unflo32_complex_m)

unflo40_complex_m = unflo40_real - 1j*unflo40_imag
unflo40_ft_m = np.fft.fft(unflo40_complex_m)

unflo46_complex_m = unflo46_real - 1j*unflo46_imag
unflo46_ft_m = np.fft.fft(unflo46_complex_m)

unflo48_complex_m = unflo48_real - 1j*unflo48_imag
unflo48_ft_m = np.fft.fft(unflo48_complex_m)

unflo50_complex_m = unflo50_real - 1j*unflo50_imag
unflo50_ft_m = np.fft.fft(unflo50_complex_m)

unflo56_complex_m = unflo56_real - 1j*unflo56_imag
unflo56_ft_m = np.fft.fft(unflo56_complex_m)

unflo64_complex_m = unflo64_real - 1j*unflo64_imag
unflo64_ft_m = np.fft.fft(unflo64_complex_m)

def peak(freq,unf,fil):
    f_spike = []
    spike = []
    prenorm = []
    for i in range(len(unf)):
        if abs(unf[i])**2 >= 2.5e17:
            f_spike.append(freq[i])
            spike.append(unf[i])
            prenorm.append(fil[i])
    return f_spike, spike, prenorm   

plt.figure(1)         
                           
f_spike_lo4, spike_lo4, prenorm_lo4 = peak(np.fft.fftfreq(len(unflo4_complex),1./200),unflo4_ft,lo4_ft)
normlo4_ft = np.array(prenorm_lo4)/np.array(spike_lo4)
freqlo4 = np.array(f_spike_lo4)
plt.plot(freqlo4,abs(normlo4_ft)**2,'bo', markersize = 8)   

f_spike_lo16, spike_lo16, prenorm_lo16 = peak(np.fft.fftfreq(len(unflo16_complex),1./200),unflo16_ft,lo16_ft)
normlo16_ft = np.array(prenorm_lo16)/np.array(spike_lo16)
freqlo16 = np.array(f_spike_lo16)
plt.plot(freqlo16,abs(normlo16_ft)**2,'bo', markersize = 8)

f_spike_lo32, spike_lo32, prenorm_lo32 = peak(np.fft.fftfreq(len(unflo32_complex),1./200),unflo32_ft,lo32_ft)
normlo32_ft = np.array(prenorm_lo32)/np.array(spike_lo32)
freqlo32 = np.array(f_spike_lo32)
plt.plot(freqlo32,abs(normlo32_ft)**2,'bo', markersize = 8) 

f_spike_lo40, spike_lo40, prenorm_lo40 = peak(np.fft.fftfreq(len(unflo40_complex),1./200),unflo40_ft,lo40_ft)
normlo40_ft = np.array(prenorm_lo40)/np.array(spike_lo40)
freqlo40 = np.array(f_spike_lo40)
plt.plot(freqlo40,abs(normlo40_ft)**2,'bo', markersize = 8) 

f_spike_lo46, spike_lo46, prenorm_lo46 = peak(np.fft.fftfreq(len(unflo46_complex),1./200),unflo46_ft,lo46_ft)
normlo46_ft = np.array(prenorm_lo46)/np.array(spike_lo46)
freqlo46 = np.array(f_spike_lo46)
plt.plot(freqlo46,abs(normlo46_ft)**2,'bo', markersize = 8) 

f_spike_lo48, spike_lo48, prenorm_lo48 = peak(np.fft.fftfreq(len(unflo48_complex),1./200),unflo48_ft,lo48_ft)
normlo48_ft = np.array(prenorm_lo48)/np.array(spike_lo48)
freqlo48 = np.array(f_spike_lo48)
plt.plot(freqlo48,abs(normlo48_ft)**2,'bo', markersize = 8) 

f_spike_lo50, spike_lo50, prenorm_lo50 = peak(np.fft.fftfreq(len(unflo50_complex),1./200),unflo50_ft,lo50_ft)
normlo50_ft = np.array(prenorm_lo50)/np.array(spike_lo50)
freqlo50 = np.array(f_spike_lo50)
plt.plot(freqlo50,abs(normlo50_ft)**2,'bo', markersize = 8) 

f_spike_lo56, spike_lo56, prenorm_lo56 = peak(np.fft.fftfreq(len(unflo56_complex),1./200),unflo56_ft,lo56_ft)
normlo56_ft = np.array(prenorm_lo56)/np.array(spike_lo56)
freqlo56 = np.array(f_spike_lo56)
plt.plot(freqlo56,abs(normlo56_ft)**2,'bo', markersize = 8) 

f_spike_lo64, spike_lo64, prenorm_lo64 = peak(np.fft.fftfreq(len(unflo64_complex),1./200),unflo64_ft,lo64_ft)
normlo64_ft = np.array(prenorm_lo64)/np.array(spike_lo64)
freqlo64 = np.array(f_spike_lo64)
plt.plot(freqlo64,abs(normlo64_ft)**2,'bo', markersize = 8) 

################## Negative ########################

f_spike_lo4_m, spike_lo4_m, prenorm_lo4_m = peak(np.fft.fftfreq(len(unflo4_complex_m),1./200),unflo4_ft_m,lo4_ft_m)
normlo4_ft_m = np.array(prenorm_lo4_m)/np.array(spike_lo4_m)
freqlo4_m = np.array(f_spike_lo4_m)
plt.plot(freqlo4_m,abs(normlo4_ft_m)**2,'bo', markersize = 8)   

f_spike_lo16_m, spike_lo16_m, prenorm_lo16_m = peak(np.fft.fftfreq(len(unflo16_complex_m),1./200),unflo16_ft_m,lo16_ft_m)
normlo16_ft_m = np.array(prenorm_lo16_m)/np.array(spike_lo16_m)
freqlo16_m = np.array(f_spike_lo16_m)
plt.plot(freqlo16_m,abs(normlo16_ft_m)**2,'bo', markersize = 8)

f_spike_lo32_m, spike_lo32_m, prenorm_lo32_m = peak(np.fft.fftfreq(len(unflo32_complex_m),1./200),unflo32_ft_m,lo32_ft_m)
normlo32_ft_m = np.array(prenorm_lo32_m)/np.array(spike_lo32_m)
freqlo32_m = np.array(f_spike_lo32_m)
plt.plot(freqlo32_m,abs(normlo32_ft_m)**2,'bo', markersize = 8) 

f_spike_lo40_m, spike_lo40_m, prenorm_lo40_m = peak(np.fft.fftfreq(len(unflo40_complex_m),1./200),unflo40_ft_m,lo40_ft_m)
normlo40_ft_m = np.array(prenorm_lo40_m)/np.array(spike_lo40_m)
freqlo40_m = np.array(f_spike_lo40_m)
plt.plot(freqlo40_m,abs(normlo40_ft_m)**2,'bo', markersize = 8) 

f_spike_lo46_m, spike_lo46_m, prenorm_lo46_m = peak(np.fft.fftfreq(len(unflo46_complex_m),1./200),unflo46_ft_m,lo46_ft_m)
normlo46_ft_m = np.array(prenorm_lo46_m)/np.array(spike_lo46_m)
freqlo46_m = np.array(f_spike_lo46_m)
plt.plot(freqlo46_m,abs(normlo46_ft_m)**2,'bo', markersize = 8) 

f_spike_lo48_m, spike_lo48_m, prenorm_lo48_m = peak(np.fft.fftfreq(len(unflo48_complex_m),1./200),unflo48_ft_m,lo48_ft_m)
normlo48_ft_m = np.array(prenorm_lo48_m)/np.array(spike_lo48_m)
freqlo48_m = np.array(f_spike_lo48_m)
plt.plot(freqlo48_m,abs(normlo48_ft_m)**2,'bo', markersize = 8) 

f_spike_lo50_m, spike_lo50_m, prenorm_lo50_m = peak(np.fft.fftfreq(len(unflo50_complex_m),1./200),unflo50_ft_m,lo50_ft_m)
normlo50_ft_m = np.array(prenorm_lo50_m)/np.array(spike_lo50_m)
freqlo50_m = np.array(f_spike_lo50_m)
plt.plot(freqlo50_m,abs(normlo50_ft_m)**2,'bo', markersize = 8) 

f_spike_lo56_m, spike_lo56_m, prenorm_lo56_m = peak(np.fft.fftfreq(len(unflo56_complex_m),1./200),unflo56_ft_m,lo56_ft_m)
normlo56_ft_m = np.array(prenorm_lo56_m)/np.array(spike_lo56_m)
freqlo56_m = np.array(f_spike_lo56_m)
plt.plot(freqlo56_m,abs(normlo56_ft_m)**2,'bo', markersize = 8) 

f_spike_lo64_m, spike_lo64_m, prenorm_lo64_m = peak(np.fft.fftfreq(len(unflo64_complex_m),1./200),unflo64_ft_m,lo64_ft_m)
normlo64_ft_m = np.array(prenorm_lo64_m)/np.array(spike_lo64_m)
freqlo64_m = np.array(f_spike_lo64_m)
plt.plot(freqlo64_m,abs(normlo64_ft_m)**2,'bo', markersize = 8, label = 'Measured Values')

#plt.xlabel('Frequency [MHz]')
#plt.ylabel('Power')
plt.title('Comparison of FIR filters')
plt.legend()