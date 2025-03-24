import matplotlib.pyplot as plt
import numpy as np
import aux as aux

Tini = 0;   # Tiempo inicial 
Tfin = 20;  # Tiempo final
T =  10;   # Periodo
fs = 1/T;   # Frecuencia de la Onda
fm = 100;  # Frecuencia de la muestra
A = 5;      # Amplitud
phi = 0;    # Desplazamiento

t1,y1 = aux.square(Tini, Tfin, fs, A, phi, fm)
t2,y2 = aux.sin(Tini, Tfin, fs, A, phi, fm)
t3,y3 = aux.ramp(Tini, Tfin, fm)

plt.subplot(3,1,1)
plt.plot(t1,y1)
print("valor medio y1: ", aux.pnorm(y1,1)/len(y1));
print("maximo y1: ", max(y1));
print("minimo y1: ", min(y1));
print("amplitud y1: ", max(np.abs(y1)));
print("energia y1: ", aux.pnorm(y1,2)**2);
print("accion y1: ", aux.pnorm(y1,1));
print("potencia y1: ", (aux.pnorm(y1,2)**2)/len(y1));
print("raiz del val cuadratico medio:", np.sqrt(aux.pnorm(y1,2)**2)/len(y1));


plt.subplot(3,1,2)
plt.plot(t2,y2)
print("valor medio y1: ", aux.pnorm(y1,1)/len(y1));
print("maximo y1: ", max(y1));
print("minimo y1: ", min(y1));
print("amplitud y1: ", max(np.abs(y1)));
print("energia y1: ", aux.pnorm(y1,2)**2);
print("accion y1: ", aux.pnorm(y1,1));
print("potencia y1: ", (aux.pnorm(y1,2)**2)/len(y1));
print("raiz del val cuadratico medio:", np.sqrt(aux.pnorm(y1,2)**2)/len(y1));

plt.subplot(3,1,3)
plt.plot(t3,y3)
print("valor medio y1: ", aux.pnorm(y1,1)/len(y1));
print("maximo y1: ", max(y1));
print("minimo y1: ", min(y1));
print("amplitud y1: ", max(np.abs(y1)));
print("energia y1: ", aux.pnorm(y1,2)**2);
print("accion y1: ", aux.pnorm(y1,1));
print("potencia y1: ", (aux.pnorm(y1,2)**2)/len(y1));
print("raiz del val cuadratico medio:", np.sqrt(aux.pnorm(y1,2)**2)/len(y1));

plt.show()
