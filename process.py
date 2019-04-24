import numpy as np 
import matplotlib.pyplot as plt 
import neurokit as nk
from biosppy import storage
from biosppy.signals import ecg


x = np.load('x_data.npy')
y = np.load('y_data.npy')
ecg_signal = x[0]
print(ecg_signal)
out = ecg.ecg(signal=ecg_signal, sampling_rate=100, show=False)
# print(out)
filtered = out["filtered"]
print(filtered)
plt.plot(filtered,linewidth=2, alpha=2.0)

plt.grid(color='r', linestyle='--', linewidth=0.3)
plt.show()