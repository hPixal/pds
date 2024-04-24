import matplotlib.pyplot as plt
import numpy as np
import aux as aux

h = [1, 2,   2, 0];
x = [2, 1, 0.5, 0];
t = [0, 1,   2, 3];


y = aux.circularconv(x,h);

plt.plot(t,x);
plt.plot(t,h);
plt.plot(t,y);
plt.show();