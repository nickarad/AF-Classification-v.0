import numpy as np 
import matplotlib.pyplot as plt 
import neurokit as nk
from biosppy import storage
from biosppy.signals import ecg


x = np.load('x_data.npy')
y = np.load('y_data.npy')
ecg_signal = x[0]
print(ecg_signal)
# processed_ecg = nk.ecg_process(ecg_signal,sampling_rate=300, filter_type="FIR", filter_band="bandpass", filter_frequency=[50, 60])
ecg_preprocessed = nk.ecg_preprocess(ecg_signal,sampling_rate=300, filter_type="FIR", filter_band="bandpass")
print(ecg_preprocessed)
filtered = ecg_preprocessed["df"]["ECG_Filtered"]
print(filtered)
plt.plot(filtered)
plt.grid(color='r', linestyle='--', linewidth=0.3)
plt.show()

ecg = np.zeros(2714)
# Find r peaks
r_peaks = ecg_preprocessed["ECG"]["R_Peaks"]
print(r_peaks)
for r in r_peaks:
    ecg[r] = ecg_signal[r]


# find q peaks
q_peaks = ecg_preprocessed["ECG"]["Q_Waves"]
print(q_peaks)
for q in q_peaks:
    ecg[q] = ecg_signal[q]

plt.plot(ecg)
plt.grid(color='r', linestyle='--', linewidth=0.3)
plt.show()


