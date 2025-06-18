import numpy as np;
import scipy as sp;
import matplotlib.pyplot as plt
import z_transform as zt

def euler(T, z):
    e = (np.ones(len(z)) - np.power(z, -1)) / T
    return e

def bilinear(T, z):
    bi = (2 / T) * np.divide(np.ones(len(z)) - np.power(z, -1), np.ones(len(z)) + np.power(z, -1))
    return bi

def db(F):
    return 20 * np.log10(F)

def H_s(s):
    h_s = np.divide(12500 * s, 44 * np.power(s, 2) + 60625 * s + 6250000 * np.ones(len(s)))
    return h_s

def get_cutoff(h_db):
    dbMax = max(h_db);
    for i in range(len(h_db)):
        if i == 0:
            dy = +1
        else:
            dy = (h_db[i] - h_db[i-1])/2
        diff = dbMax-h_db[i]
        if abs(diff) > 3 and dy < 0:
            return i
            break

def exercise_1():
    # frequencies
    freqs = np.arange(15000 // 2) 

    # Frequency range for analysis
    s = 1j * 2 * np.pi * freqs # s = jω, σ = 0, ω = 2 pi * freq 

    H = H_s(s)
    h_db = db(np.abs(H))

    # Get the -3 db diff 
    cut_f = get_cutoff(h_db)

    print(cut_f)
    plt.figure()
    plt.plot(freqs, h_db)
    plt.title('Response of H(s)')
    plt.xlabel('Frequencies (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True)
    # Mark the cutoff frequency
    plt.plot(freqs[cut_f], h_db[cut_f], 'ro', label='Cutoff Frequency')
    plt.legend()
    plt.show()

def exercise_2():
    # Valor arbitrario para la frecuencia de muestreo
    ftest = np.arange(15000 // 2)
    sTest = 2j * np.pi * ftest  # s = jw = j2pif

    H_f = np.abs(H_s(sTest))  # H(jw) -> respuesta en frecuencia
    fMax = np.argmax(H_f)  # frecuencia donde H(s) tiene máxima magnitud
    ic = get_cutoff(db(H_f))
    fCorte = ic

    # frecuencia de muestreo 4 veces la frecuencia de corte
    fm = 4 * fCorte
    T = 1 / fm
    f = np.arange(fm // 2)
    z = np.exp(2j * np.pi * f * T)  # z = e^j2pi f T
    HEuler = H_s(euler(T, z))
    HBilineal = H_s(bilinear(T, z))

    # frecuencia de muestreo más alta (8 veces fCorte) para comparar
    fm2 = 8 * fCorte
    T2 = 1 / fm2
    f2 = np.arange(fm2 // 2)
    z2 = np.exp(2j * np.pi * f2 * T2)
    HEuler2 = H_s(euler(T2, z2))
    HBilineal2 = H_s(bilinear(T2, z2))

    # Graficar
    s = 2j * np.pi * f
    s2 = 2j * np.pi * f2
    h_db_cont = db(np.abs(H_s(s)))
    h_db_euler_1 = db(np.abs(HEuler))
    h_db_bilinear_1 = db(np.abs(HBilineal))
    h_db_euler_2 = db(np.abs(HEuler2))
    h_db_bilinear_2 = db(np.abs(HBilineal2))
    freqs_cont = f
    freqs1 = f
    freqs2 = f2

    plt.figure(figsize=(12, 6))
    plt.plot(freqs_cont, h_db_cont, label='Continuous H(s)', color='black', linewidth=2)
    plt.plot(freqs1, h_db_euler_1, '--', label='Euler (fs=15kHz)')
    plt.plot(freqs1, h_db_bilinear_1, '--', label='Bilinear (fs=15kHz)')
    plt.plot(freqs2, h_db_euler_2, ':', label='Euler (fs=7.5kHz)')
    plt.plot(freqs2, h_db_bilinear_2, ':', label='Bilinear (fs=7.5kHz)')
    plt.title('Frequency Response Comparison')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    exercise_2();
    
main();