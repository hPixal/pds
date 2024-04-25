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

plt.plot(t1,y1)
print("midvalue y1: ", aux.midvalue(y1));
print("maximum y1: ", max(y1));
print("minimum y1: ", min(y1));
print("amplitude y1: ", aux.amplitude(y1));
print("energy y1: ", aux.energy(y1));
print("power y1: ", aux.power(y1));
print("skewness y1: ", aux.skewness(y1));
plt.show()

plt.plot(t2,y2)
print("midvalue y2: ", aux.midvalue(y2));
print("maximum y2: ", max(y2));
print("minimum y2: ", min(y2));
print("amplitude y2: ", aux.amplitude(y2));
print("energy y2: ", aux.energy(y2));
print("power y2: ", aux.power(y2));
print("skewness y2: ", aux.skewness(y2));
plt.show()

plt.plot(t3,y3)
print("midvalue y3: ", aux.midvalue(y3));
print("maximum y3: ", max(y3));
print("minimum y3: ", min(y3));
print("amplitude y3: ", aux.amplitude(y3));
print("energy y3: ", aux.energy(y3));
print("power y3: ", aux.power(y3));
print("skewness y3: ", aux.skewness(y3));
plt.show()
