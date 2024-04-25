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

def soft(long, fm):
    T = 1/fm
    t = np.arange(-long,long-T,T)
    y = 1+np.sin(np.pi*t/long+np.pi/2)
    return t,y

def square(Tini, Tfin, fs, A, phi, fm):
    Tm = 1/fm
    t = np.arange(Tini, Tfin-Tm, Tm)
    y = A * np.sign(np.sin(2 * np.pi * fs * t + phi))
    return t, y

def ramp(Tini, Tfin, fm):
    Tm = 1/fm
    t = np.arange(Tini, Tfin-Tm, Tm)
    y = t
    return t, y

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

def circularconv(x,h):
    N = len(h);
    y = [0]*N;

    for k in range(N):
        for l in range(N):
            pos = (k+l)%N;
            y[k] += h[l]*x[pos];
    return y;

def midvalue(y):
    x = sorted(y)
    return (x[0]+x[len(y)-1])/2;

def maximum(y):
    return max(y);


def amplitude(y):
    return (max(y) - min(y))/2;

def energy(y):
    return sum(np.power(y,2))

def variance(y):
    return np.var(y)

def skewness(y):
    return np.mean(np.power(y,3))

def power(y):
    return np.mean(np.power(y,2))

def signal_inner_product(x, y):
    return np.dot(x, y)

def mean_squared_error(y_true, y_pred):
    return np.mean((y_pred - y_true) ** 2)

def squared_error(y_true, y_pred):
    return sum(np.square(y_pred - y_true));