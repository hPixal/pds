import matplotlib.pyplot as plt
import numpy as np
import aux as aux

t1,y1 = aux.sin(-2,2,2,1,0,50) # Entrada 1
t2,y2 = aux.normal(-2,2,50)    # Entrada 2

y = [0]*len(t1);
y = aux.linearconv(y1,y2);
t = range(len(y));
print(len(y));

plt.plot(t1,y1);
plt.plot(t2,y2);
plt.show()

plt.plot(t,y);
plt.show()