import matplotlib.pyplot as plt
import numpy as np
import aux as aux

Tini = 0;   # Tiempo inicial 
Tfin = 20;  # Tiempo final
T =  10;   # Periodo
fs = 1/T;   # Frecuencia de la Onda
fm = 100;  # Frecuencia de la muestra
A = 5;      # Amplitud
phi = 3.1416;    # Desplazamiento

t1,y1 = aux.sin(Tini, Tfin, fs+fs/2, A, phi, fm)
t2,y2 = aux.sin(Tini, Tfin, fs, A, phi, fm)

print("fs + fs/2 :" ,aux.signal_inner_product(y1,y2))

plt.subplot(3,1,1)
plt.plot(t1,y1);
plt.plot(t2,y2);


t1,y1 = aux.sin(Tini, Tfin, fs, A, 0, fm)
t2,y2 = aux.sin(Tini, Tfin, fs, A, phi, fm)

print("phi = 0 3.1416:" ,aux.signal_inner_product(y1,y2))

plt.subplot(3,1,2)
plt.plot(t1,y1);
plt.plot(t2,y2);

t1,y1 = aux.sin(Tini, Tfin, fs, A, phi/2, fm)
t2,y2 = aux.sin(Tini, Tfin, fs, A, phi, fm)

print("phi = 3.1416 3.1416/2:" ,aux.signal_inner_product(y1,y2))

plt.subplot(3,1,3)
plt.plot(t1,y1);
plt.plot(t2,y2);
plt.show();

