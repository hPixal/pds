import numpy as np
import matplotlib.pyplot as plt

def senoidal(f_m, f_s, t_i, t_f, amp, alpha):
    dt = 1/f_m
    x = np.arange(t_i, t_f, dt)
    y = amp * np.sin(2 * np.pi * f_s * x + alpha)
    return x, y

# Parámetros comunes
f_s = 4000     # Frecuencia de la onda senoidal
t_i = 0     # Tiempo inicial
t_f = 1     # Tiempo final
amp = 1     # Amplitud de la onda senoidal
alpha = 0   # Desfase

# Frecuencias de muestreo
frecuencias_muestreo = [129, 8500]

# Crear subplots
fig, axes = plt.subplots(1, len(frecuencias_muestreo), figsize=(15, 3), sharey=True)

for i, f_m in enumerate(frecuencias_muestreo):
    x, y = senoidal(f_m, f_s, t_i, t_f, amp, alpha)
    axes[i].stem(x, y, basefmt=" ")
    axes[i].set_title(f'f_m = {f_m} Hz')
    axes[i].set_xlabel('Tiempo (s)')
    axes[i].grid(True)

axes[0].set_ylabel('Amplitud')
plt.tight_layout()
plt.show()