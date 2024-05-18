import matplotlib.pyplot as plt
import numpy as np
import aux as aux

Tini = 0;     # Tiempo inicial 
Tfin = 5;     # Tiempo final
T =  10;      # Periodo
fs = 1/T;     # Frecuencia de la Onda
fm = 200;     # Frecuencia de la muestra
A = 5;        # Amplitud
phi = 3.1416; # Desplazamiento

with open('te.txt', 'r') as file:
    # Read all lines
    lines = file.readlines()
    
    y = [0]*len(lines);
# Process the lines
for line in lines:
    print(line.strip())  # Strip removes newline characters
    y.append(float(line.strip())); 

print(len(y));
t = np.arange(0, len(y), 1)
plt.plot(t,y);
plt.show();

