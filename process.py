import numpy as np 
import matplotlib.pyplot as plt 
import neurokit as nk
from biosppy import storage
from biosppy.signals import ecg


x = np.load('x_data.npy')
y = np.load('y_data.npy')
x = x[0:100]
x_filt = np.array([])
for ecg_signal in x:
    # ecg_signal = r
    out = ecg.ecg(signal=ecg_signal, sampling_rate=300, show=False)
    filtered = out["filtered"]
    x_filt = np.append(x_filt,filtered)
    # print(filtered)
x_filt = x_filt.reshape(-1, 2714)
np.save('x_filtered.npy', x_filt)
print(x_filt.shape)
print(x_filt)

# ===================================================


# ecg_signal = x[0]
# print(ecg_signal)
# out = ecg.ecg(signal=ecg_signal, sampling_rate=300, show=False)
# # print(out)
# filtered = out["filtered"]
# print(filtered)
# plt.plot(filtered,linewidth=2, alpha=2.0)
# plt.grid(color='r', linestyle='--', linewidth=0.3)
# plt.show()