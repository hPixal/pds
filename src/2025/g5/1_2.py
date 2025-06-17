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
    A_z = [1];
    B_z = [1,-1/2,1/4];
    zt.H_ejw(A_z, B_z,False,10000,True);
    
    # Problem 2
    A_z = [0,1];
    B_z = [1,-1,-1];
    zt.H_ejw(A_z, B_z,False,10000,True);
    
    # Problem 3
    A_z = [7];
    B_z = [1,-2,6];
    zt.H_ejw(A_z, B_z,False,10000,True);
    
    # Problem 4
    A_z = [2 ** k for k in range(8)]
    B_z = [1];
    zt.H_ejw(A_z, B_z,False,10000,True);
    
    return

main();