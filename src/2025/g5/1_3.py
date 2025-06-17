import numpy as np;
import scipy as sp;
import matplotlib.pyplot as plt
import z_transform as zt

def main():
    # Define the transfer function, remember that H(Z) is
    # H(Z) = Y(Z)/X(Z)
    # Where 
    # Y(Z) = (b_0 + b_1 * z^-1 + b_2 * z^-2 + ... + b_n * z^-n)
    # X(Z) = (a_0 + a_1 * z^-1 + a_2 * z^-2 + ... + a_n * z^-n)
    # Which can be expressed only by it's coeffs for math analysis
    
    
    # Problem 1
    A_z = [1,-2,2,-1];
    B_z = [1,-17/10,0.8,-1/10];
    zt.H_ejw(A_z, B_z,False,False,True);
    
    # Impulse response
    
    N = 50
    x = np.zeros(N)
    x[3] = 1
    y = np.zeros(N)
    for n in range(3, N):
        y[n] = 1.7*y[n-1] - 0.8*y[n-2] + 0.1*y[n-3] + x[n] - 2*x[n-1] + 2*x[n-2] - x[n-3]

    plt.plot(range(N), y)
    plt.title("Impulse response")
    plt.xlabel("n")
    plt.ylabel("y[n]")
    plt.grid(True)
    plt.show()
    
    return

main();