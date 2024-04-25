import matplotlib.pyplot as plt
import numpy as np
import aux as aux

Tini = 0;   # Tiempo inicial 
Tfin = 5;  # Tiempo final
T =  10;   # Periodo
# fs = 1/T;   # Frecuencia de la Onda
fm = 200;  # Frecuencia de la muestra
A = 5;      # Amplitud
phi = 3.1416;    # Desplazamiento

t,y1  = aux.sin(Tini, Tfin,  1, A, phi, fm);
t,y2  = aux.sin(Tini, Tfin,  2, A, phi, fm);
t,y3  = aux.sin(Tini, Tfin,  3, A, phi, fm);
t,y4  = aux.sin(Tini, Tfin,  4, A, phi, fm);
t,y5  = aux.sin(Tini, Tfin,  5, A, phi, fm);
t,y6  = aux.sin(Tini, Tfin,  6, A, phi, fm);
t,y7  = aux.sin(Tini, Tfin,  7, A, phi, fm);
t,y8  = aux.sin(Tini, Tfin,  8, A, phi, fm);
t,y9  = aux.sin(Tini, Tfin,  9, A, phi, fm);
t,y10 = aux.sin(Tini, Tfin, 10, A, phi, fm);

plt.plot(t,y1)
plt.plot(t,y2)
plt.plot(t,y3)
plt.plot(t,y4)
plt.plot(t,y5)
plt.plot(t,y6)
plt.plot(t,y7)
plt.plot(t,y8)
plt.plot(t,y9)
plt.plot(t,y10)
plt.show()


y = y1+y2+y3+y4+y5+y6+y7+y8+y9+y10;

plt.plot(t,y);
plt.show();

values = np.zeros(10);
categories = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# values[0] = aux.squared_error(y, y1);
# values[1] = aux.squared_error(y, y2);
# values[2] = aux.squared_error(y, y3);
# values[3] = aux.squared_error(y, y4);
# values[4] = aux.squared_error(y, y5);
# values[5] = aux.squared_error(y, y6);
# values[6] = aux.squared_error(y, y7);
# values[7] = aux.squared_error(y, y8);
# values[8] = aux.squared_error(y, y9);
# values[9] = aux.squared_error(y,y10);

values[0] = aux.signal_inner_product(y, y1);
values[1] = aux.signal_inner_product(y, y2);
values[2] = aux.signal_inner_product(y, y3);
values[3] = aux.signal_inner_product(y, y4);
values[4] = aux.signal_inner_product(y, y5);
values[5] = aux.signal_inner_product(y, y6);
values[6] = aux.signal_inner_product(y, y7);
values[7] = aux.signal_inner_product(y, y8);
values[8] = aux.signal_inner_product(y, y9);
values[9] = aux.signal_inner_product(y,y10);


for i in range(len(values)):
    print(values[i])

# Create bar chart
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()



