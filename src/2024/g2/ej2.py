import matplotlib.pyplot as plt
import numpy as np
import aux as aux

Tini = 0;   # Tiempo inicial 
Tfin = 20;  # Tiempo final
T =  2;   # Periodo
fs = 1/T;   # Frecuencia de la Onda
fm = 100000;  # Frecuencia de la muestra
A = 5;      # Amplitud
phi = 0;    # Desplazamiento

#t1,y1 = aux.sin(Tini, Tfin, fs, A, phi, fm); 
#t,y1 = aux.sin(-2,2,2,1,0,50);
#t2,y2 = aux.normal(Tini, Tfin, fm); 

t1,y1 = aux.sin(-2,2,2,1,0,50) # Entrada 1
t2,y2 = aux.normal(-2,2,50)    # Entrada 2

y = [0]*len(t1);

for n in range(1,len(t1)):
    y[n] = np.sqrt(-2*y1[n-1]*y2[n] + np.power(y1[n-1],2)  + np.power(y1[n],2));

plt.plot(t1,y)
plt.show()

y = [0]*len(t2);

for n in range(1,len(t2)):
    y[n] = np.sqrt(np.power(y2[n-1],2)  + np.power(y2[n],2) -2*y2[n-1]*y2[n]);

plt.plot(t2,y)
plt.show()
