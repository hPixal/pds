import numpy as np
import matplotlib.pyplot as plt

def senoidal(n,f_s, amp, alpha):
    y = amp * np.sin(2 * np.pi * f_s * n + alpha)
    return y

def eq1(n,x_n):
    f_s = 5 # Hz
    amp = 2 
    alpha = 0
    return senoidal(n,f_s,amp,alpha)*x_n

def eq2(n, x_n):  # x_n is an array
    n0 = 2
    up_n = n + n0
    low_n = n - n0
    result = 0
    
    for k in range(int(low_n), int(up_n) + 1):
        if 0 <= k < len(x_n):  # Ensure index is within bounds
            result += x_n[k]
    return result

def eq3(x_n):
    return x_n + 2

def eq4(n, x_n):
    return n * x_n

def ejercicio1():
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    
    # Equation 1
    n = np.linspace(0, 5, int(5 / 0.01) + 1)
    x_n = np.ones_like(n)  # Example: constant array of ones
    y_n_eq1 = np.zeros_like(n)
    
    for i in range(len(n)):  # Fixed loop syntax
        y_n_eq1[i] = eq1(n[i], x_n[i])
    
    axs[0, 0].plot(n, y_n_eq1, label="y(n) - eq1")
    axs[0, 0].set_xlabel("n")
    axs[0, 0].set_ylabel("y(n)")
    axs[0, 0].set_title("Graph of y(n) = g[n]x[n] (eq1)")
    axs[0, 0].legend()
    axs[0, 0].grid()
    
    # Equation 2
    n = np.linspace(0, 5, int(5 / 0.2) + 1)
    x_n = np.ones_like(n)
    y_n_eq2 = np.zeros_like(n)
    
    for i in range(len(n)):
        y_n_eq2[i] = eq2(i, x_n)  # Pass index for eq2
    
    axs[0, 1].stem(n, y_n_eq2, label="y(n) - eq2")
    axs[0, 1].set_xlabel("n")
    axs[0, 1].set_ylabel("y(n)")
    axs[0, 1].set_title("Graph of y(n) = eq2")
    axs[0, 1].legend()
    axs[0, 1].grid()
    
    # Equation 3
    n = np.linspace(0, 5, int(5 / 0.01) + 1)
    x_n = np.ones_like(n)
    y_n_eq3 = eq3(x_n)
    
    axs[1, 0].plot(n, y_n_eq3, label="y(n) - eq3")
    axs[1, 0].set_xlabel("n")
    axs[1, 0].set_ylabel("y(n)")
    axs[1, 0].set_title("Graph of y(n) = eq3")
    axs[1, 0].legend()
    axs[1, 0].grid()
    
    # Equation 4
    n = np.linspace(0, 5, int(5 / 0.01) + 1)
    x_n = np.ones_like(n)
    y_n_eq4 = eq4(n, x_n)
    
    axs[1, 1].plot(n, y_n_eq4, label="y(n) - eq4")
    axs[1, 1].set_xlabel("n")
    axs[1, 1].set_ylabel("y(n)")
    axs[1, 1].set_title("Graph of y(n) = eq4")
    axs[1, 1].legend()
    axs[1, 1].grid()
    
    plt.tight_layout()
    plt.show()
    
    
ejercicio1()