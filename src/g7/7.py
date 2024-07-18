import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import scipy as signal

def playSound(sound,fs):
    sd.play(sound,fs)
    sd.wait()
    return

# Define parameters
fs = 44100  # Sample rate (Hz)
duration = 5.0  # Duration in seconds
frequency = 1000  # Frequency of the sinusoid (Hz)

# Generate white noise

n_samples = int(duration * fs)
white_noise = np.random.normal(0, 1, n_samples)


# Generate time array
t = np.linspace(0, duration, int(fs * duration), endpoint=False)


# Generate sinusoidal signal
# sinusoidal_noise = np.sin(2 * np.pi * frequency * t) + np.sin(2 * np.pi * frequency/2 * t) + np.sin(2 * np.pi * frequency/4 * t);
sinusoidal_noise = np.sin(2 * np.pi * frequency/2 * t) + np.sin(2 * np.pi * frequency/4 * t);
# sinusoidal_noise = np.sin(2 * np.pi * frequency/4 * t);

# Generate white noise
# Generate time array
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Generate sinusoidal signal
sinusoid = np.sin(2 * np.pi * frequency * t)

# Transfer Function
w0 = frequency * np.pi;   # half the frequency as passband
num = w0;
den = [1,w0];

lowPass = signal.signal.TransferFunction(num, den);
discrete_lowpass = lowPass.to_discrete(num, method = 'gbt',alpha = 0.5);

a = discrete_lowpass.num[1:]
b = -discrete_lowpass.den

print("Filter coefficients: ", a, b);

# Apply filter

new_white_noise = signal.signal.lfilter(a, b, white_noise);
new_sinusoidal_noise = signal.signal.lfilter(a, b, sinusoidal_noise);

playSound(sinusoidal_noise,fs)
playSound(new_sinusoidal_noise,fs)

# Plot FFT
sp = np.fft.fft(sinusoidal_noise)
freq = np.fft.fftfreq(t.shape[-1])

plt.plot(freq, sp.real, freq, abs(sp.imag));
plt.show()

# Plot FFT new
sp = np.fft.fft(new_sinusoidal_noise)
freq = np.fft.fftfreq(t.shape[-1])

plt.plot(freq, sp.real, freq, abs(sp.imag));
plt.show()
