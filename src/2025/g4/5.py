import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window

def sinusoidal(f_m, f_s, t_i, t_f, amp, alpha):
    x = np.arange(t_i, t_f, 1/f_m)
    y = amp * np.sin(2 * np.pi * f_s * x + alpha)
    return x, y

def main():
    
    return
    

    
def dft(signal):
    N = len(signal)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def dirac_delta(N, n0=0):
    delta = np.zeros(N)
    if 0 <= n0 < N:
        delta[n0] = 1
    return delta

def energy(signal):
    N = len(signal)
    p2 = 0
    for n in range(N-1):
        p2 += abs(signal[n]) ** 2
    return p2

def parseval(x):
    N = len(x)
    X = dft(x)
    
    Xp2 = (1/N)*energy(X)
    xp2 = energy(x)
    
    print(f"xp2 (time domain): {xp2}")
    print(f"Xp2 (frequency domain): {Xp2}")
    
    if(xp2 == Xp2 ):
        print('Se cumple parseval')
        
main()