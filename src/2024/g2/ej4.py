import matplotlib.pyplot as plt
import numpy as np
import aux as aux

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

# t1,y1 = aux.sin(-2,2,2,1,0,50) # Entrada 1
# t2,y2 = aux.normal(-2,2,50)    # Entrada 2

t = np.arange(1, 10, 0.1);
y_1 = [0]*100;
x = [0]*100;
y_1[1] = x[1];
y_1[2] = x[2];
for n in range(3,100):
 print(x,y_1); # y_1[n]
 y_1[n] = x[n] + y_1[n-2];


plt.plot(x,y_1)
plt.show()
