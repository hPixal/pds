import numpy as np
import matplotlib.pyplot as plt

def senoidal(f_m, f_s, t_i, t_f, amp, alpha):
    dt = 1/f_m
    x = np.arange(t_i, t_f, dt)
    y = amp * np.sin(2 * np.pi * f_s * x + alpha)
    return x, y

def piramid(t_values):
    return [max(0, 1 - abs(t)) for t in t_values]

def sinc(t):
    return np.where(t == 0, 1, np.sin(np.pi * t) / (np.pi * t))

def interpolate(x, t_original, t_interpolated, interpolation_func):
    """Perform interpolation of x from t_original to t_interpolated using a given interpolation function"""
    interpolated = np.zeros_like(t_interpolated)
    for i, t in enumerate(t_interpolated):
        interpolated[i] = np.sum(x * interpolation_func((t - t_original) / T))
    return interpolated

# Original parameters
N = 10  # Number of original samples
fs = 10  # Original sampling frequency (Hz)
T = 1 / fs  # Original sampling period

# New upsampled parameters
upsample_factor = 4
fs_new = fs * upsample_factor  # New sampling frequency (40 Hz)
T_i = 1 / fs_new  # New sampling period

# Generate the original discrete signal (sine wave)
t_original = np.arange(N) * T  # Time samples for original signal
x_original = np.sin(2 * np.pi * 1 * t_original)  # A 1 Hz sine wave

# Generate the new interpolated time points
t_interpolated = np.arange(N * upsample_factor) * T_i

# Apply sinc interpolation
x_interpolated_sinc = interpolate(x_original, t_original, t_interpolated, sinc)

# Apply piramid interpolation
x_interpolated_piramid = interpolate(x_original, t_original, t_interpolated, piramid)

# Plot results
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Top left: Sinc function
t_sinc = np.linspace(-2, 2, 500)
axs[0, 0].plot(t_sinc, sinc(t_sinc), 'b-')
axs[0, 0].set_title("Sinc Function")
axs[0, 0].grid()

# Top right: Piramid function
t_piramid = np.linspace(-2, 2, 500)
axs[0, 1].plot(t_piramid, piramid(t_piramid), 'g-')
axs[0, 1].set_title("Piramid Function")
axs[0, 1].grid()

# Bottom left: Interpolated signal with sinc
axs[1, 0].stem(t_original, x_original, linefmt='r-', markerfmt='ro', basefmt="r-", label="Original Samples")
axs[1, 0].plot(t_interpolated, x_interpolated_sinc, 'b-', label="Interpolated (Sinc)")
axs[1, 0].set_title("Interpolated Signal (Sinc)")
axs[1, 0].legend()
axs[1, 0].grid()

# Bottom right: Interpolated signal with piramid
axs[1, 1].stem(t_original, x_original, linefmt='r-', markerfmt='ro', basefmt="r-", label="Original Samples")
axs[1, 1].plot(t_interpolated, x_interpolated_piramid, 'g-', label="Interpolated (Piramid)")
axs[1, 1].set_title("Interpolated Signal (Piramid)")
axs[1, 1].legend()
axs[1, 1].grid()

plt.tight_layout()
plt.show()