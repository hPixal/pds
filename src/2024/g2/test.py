import matplotlib.pyplot as plt
import numpy as np
import aux as aux

# t = np.arange(0,10,0.1)
# y = np.sin(t)
# plt.plot(t,y)
# plt.show()

a1 = np.convolve([1,2,3],[4,5,6])
a2 = aux.linearconv([1,2,3],[4,5,6])

print("Numpy lib: ")
for i in range(len(a1)):
    print(a1[i])

print("Casera: ")
for i in range(len(a2)):
    print(a2[i])