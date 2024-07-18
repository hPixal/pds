import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import scipy as scy
from scipy.io import wavfile

# Beat Detection Steps
#  0. Load sound
#  1. Normalize
#  2. Filter
#  3. Apply envelope
#  4. Find peaks
#  5. Find beat based on the peaks

# Part 0 - Load sound

# 0.1 Load sound
file_path = 'tp/testBeat.wav'
sample_rate, data = wavfile.read(file_path);

n_samples = len(data)
white_noise = np.random.normal(0, 1, n_samples)

#data = data + white_noise

# 0.2 Plot the sound
# plt.plot(data) 
# plt.show()

# 0.3 Play Sound
# sd.play(data, sample_rate)
# sd.wait()

# Part 1 - Normalize

# 1.1 Obtain min and max
lower_bound = np.min(data)
upper_bound = np.max(data)

# 1.2 Normalized the data using the bounds
normalized = (data - lower_bound) / (upper_bound - lower_bound)

# 1.3 Plot the normalized data
# plt.plot(normalized)
# plt.show()

# Part 2 - Filter

# 2.1 Define filter parameters
frequency = 1000;
w0 = frequency * np.pi;   # half the frequency as passband
num = w0;
den = [1,w0];

# 2.2 Generate transfer function for butterworth filter
lowPass = scy.signal.TransferFunction(num, den);
discrete_lowpass = lowPass.to_discrete(num, method = 'gbt',alpha = 0.5);

a = discrete_lowpass.num[1:]
b = -discrete_lowpass.den

# print("Filter coefficients: ", a, b);

# 2.3 Apply filter

filtered = scy.signal.lfilter(a, b, data)

# 2.4 Plot the filtered data

# plt.plot(filtered)
# plt.show()

# Part 3 - Apply envelope

analytic_signal = scy.signal.hilbert(filtered)
envelope = np.abs(analytic_signal)

plt.figure(figsize=(12, 6))
plt.plot(filtered, label='Normalized Signal')
plt.plot(envelope, label='Envelope', linewidth=2)
plt.legend()
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('Signal and its Envelope')
plt.show()

# Part 4 - Find peaks

# Part 5 - Find beat based on the peaks