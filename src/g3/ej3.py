import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import aux as aux

"""
degrees = [1, 2, 3, 4, 5]

# Range of x values
x_values = np.linspace(-1, 1, 100)

for degree in degrees:
    legendre_values = [aux.legendre(degree, x) for x in x_values]
    plt.plot(x_values, legendre_values, label=f'Degree {degree}')

plt.xlabel('x')
plt.ylabel(f'Legendre Polynomial')
plt.title(f'Legendre Polynomials')
plt.grid(True)
plt.show()
"""
def leg(x):
    y = [0]*len(x)
    for i in range(len(x)):
        y[i] = 45*x[i] - 35*np.power(x[i],3)
        y[i] = y[i]/16
    
    return y;

def escalon(x):
    y = [0]*len(x)
    for i in range(len(x)):
        if x[i] < 0:
            y[i] = -1
        else:
            y[i] = 1
    return y

def aprox (a1,a2,x):

    aprox = [0]*len(x)

    var1 = np.sqrt(3/2)

    for i in range(len(x)):
        aprox[i] = a1*(x[i]*var1) + a2*(np.sqrt(7/2)*(5*(x[i]**3)/2 - (3/2)*x[i]))
    return aprox

t = np.arange(-1,1,0.01)
y1 = leg(t);
y2 = escalon(t);


err = aux.squared_error(y1,y2)

#plt.plot(t,leg(t),'r')
#plt.plot(t,escalon(t))

#plt.show()

t1 = np.arange(-0.1,0.1,0.01)

alpha1 = np.sqrt(3/2)
alpha2 = -np.sqrt(7/32)


z = np.zeros((len(t1),len(t1)));

for i in range(len(t1)):
    for j in range(len(t1)):
        auxsignal = [0]*len(t)
        auxsignal = aprox(alpha1+t1[i],alpha2+t1[j],t)
        z[i][j] = aux.squared_error(y2,auxsignal)
        if(np.isnan(z[i][j])):
            print("#############")
            print(auxsignal)
            print("#############")

print(len(z))
print(len(z[0]))
print(len(t1))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(t1)):
    for j in range(len(t1)):
        auxsignal = [0]*len(t)
        auxsignal = aprox(alpha1+t1[i], alpha2+t1[j], t)
        if np.isnan(auxsignal).any():
            continue
        ax.scatter(t1[i], t1[j], z[i][j], marker='o')

ax.set_xlabel('t1')
ax.set_ylabel('t1')
ax.set_zlabel('z')

plt.show()

plt.show()
        