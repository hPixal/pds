#-------------- Algoritmos auxiliares --------------
#----------------- ejecutar UNA VEZ ----------------
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

def sin(Tini, Tfin, fs, A, phi, fm):
    Tm = 1/fm
    t = np.arange(Tini, Tfin-Tm, Tm)
    y = A * np.sin(2 * np.pi * fs * t + phi)
    return t, y

def normal(Tini, Tfin, fm):
    Tm = 1/fm
    t = np.arange(Tini, Tfin-Tm, Tm)
    y = (1/np.sqrt(2*np.pi))*np.exp(-np.power(t,2)/2)
    return t,y

def suave(long, fm):
    T = 1/fm
    t = np.arange(-long,long-T,T)
    y = 1+np.sin(np.pi*t/long+np.pi/2)
    return t,y

def delta(tini,tfin,d,fm):
    # tini < d < tfin
    T = 1/fm
    t = np.arange(tini,tfin-T,T)
    y = [0]*len(t)
    y[int((d-tini)/T)] = 1
    return t,y

def linearconv(x1,x2):
    
    size = len(x1) + len(x2) - 1;
    y = [0]*size;

    for i in range(len(x1)):
        for j in range(len(x2)):
            y[i+j] += x1[i]*x2[j]
    
    return y