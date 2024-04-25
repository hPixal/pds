import matplotlib.pyplot as plt
import numpy as np
import aux as aux

# h = [1, 2,   2, 0];
# x = [2, 1, 0.5, 0];
# t = [0, 1,   2, 3];

Tini = 0;   # Tiempo inicial 
Tfin = 20;  # Tiempo final
T =  2;   # Periodo
fs = 1/T;   # Frecuencia de la Onda
fm = 100;  # Frecuencia de la muestra
A = 5;      # Amplitud
phi = 0;    # Desplazamiento

#t1,y1 = aux.sin(Tini, Tfin, fs, A, phi, fm); 
#t,y1 = aux.sin(-2,2,2,1,0,50);
#t2,y2 = aux.normal(Tini, Tfin, fm); 

t1,h = aux.sin(Tini, Tfin, fs, A, phi, fm) # Entrada 1
t2,x = aux.normal(Tini,Tfin,fm)    # Entrada 2

t = range(len(t1));

y = aux.circularconv(x,h);

plt.plot(t,x);
plt.plot(t,h);
plt.plot(t,y);
plt.show();