import numpy as np
import matplotlib.pyplot as plt

def senoidal(n, f_s, amp, alpha):
    y = amp * np.sin(2 * np.pi * f_s * n + alpha)
    return y

def eq1(y_n, x_n, n):
    # Update the value of y_n at index n
    y_n[n] = x_n[n] + y_n[n-2]
    return y_n

def eq2(y_n, x_n, n):
    y_n[n] = x_n[n] + 0.5*x_n[n-1]
    return y_n

def eq3(y_n, x_n, n):
    y_n[n] = 0.5*y_n[n-1] + 0.25*y_n[n-2] + x_n[n]
    return y_n

def ejercicio4():
    # n goes from 0 to 20 (inclusive)
    n_arr = np.arange(0, 21)
    y_n0 = np.zeros_like(n_arr, dtype=float)
    x_n = np.zeros_like(n_arr, dtype=float)
    
    # Initial conditions
    x_n[0] = 1
    y_n0[0] = 1 # Impulse
    y_n = y_n0.copy()
    
    # Create a single figure with subplots
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    
    # Compute y_n using eq1
    for n in range(2, len(n_arr)):
        y_n = eq1(y_n, x_n, n)
    
    # Plot the results for eq1
    axs[0].stem(n_arr, y_n, basefmt=" ")
    axs[0].set_title("Graph of y[n] using eq1")
    axs[0].set_xlabel("n")
    axs[0].set_ylabel("y[n]")
    axs[0].grid()
    
    # Compute y_n using eq2
    y_n = y_n0.copy()
    for n in range(1, len(n_arr)):
        y_n = eq2(y_n, x_n, n)
    
    # Plot the results for eq2
    axs[1].stem(n_arr, y_n, basefmt=" ")
    axs[1].set_title("Graph of y[n] using eq2")
    axs[1].set_xlabel("n")
    axs[1].set_ylabel("y[n]")
    axs[1].grid()
    
    # Compute y_n using eq3
    y_n = y_n0.copy()
    for n in range(2, len(n_arr)):
        y_n = eq3(y_n, x_n, n)
    
    # Plot the results for eq3
    axs[2].stem(n_arr, y_n, basefmt=" ")
    axs[2].set_title("Graph of y[n] using eq3")
    axs[2].set_xlabel("n")
    axs[2].set_ylabel("y[n]")
    axs[2].grid()
    
    # Adjust layout and show the figure
    plt.tight_layout()
    plt.show()

# Call the function to execute and graph
ejercicio4()
        
