import numpy as np;
import scipy as sp;
import matplotlib.pyplot as plt
import z_transform as zt

def plot_H_ejw(omega, H, Y_z, X_z,fs = None):
    """
    Plots the magnitude, phase, and the unit circle with poles and zeros of the frequency response H(e^{jω}).

    Parameters:
        omega (array-like): Array of frequency values in radians/sample.
        H (array-like): Array of complex frequency response values corresponding to omega.
        Y_z (array-like): Numerator coefficients.
        X_z (array-like): Denominator coefficients.
    """
    zeros = np.roots(Y_z)
    poles = np.roots(X_z)

    plt.figure(figsize=(15, 5))

    # Magnitude
    plt.subplot(1, 3, 1)
    plt.plot(omega, np.abs(H))
    plt.title('Magnitud |H(e^{jω})|')
    plt.xlabel('ω (rad/muestra)')
    plt.ylabel('Magnitud')
    plt.grid(True)

    # Phase
    plt.subplot(1, 3, 2)
    plt.plot(omega, np.angle(H))
    plt.title('Fase ∠H(e^{jω})')
    plt.xlabel('ω (rad/muestra)')
    plt.ylabel('Fase (radianes)')
    plt.grid(True)

    # Unit circle, poles and zeros
    plt.subplot(1, 3, 3)
    theta = np.linspace(0, 2 * np.pi, 400) # Range of radiants of the unit circle.
    plt.plot(np.cos(theta), np.sin(theta), 'k--', label='Unit circle')
    plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Ceros')
    plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Polos')
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.title('Polos y Ceros en el plano Z')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.legend()
    plt.axis('equal')
    plt.grid(True)

    # Check for unstable poles (outside unit circle)
    unstable = np.any(np.abs(poles) > 1)
    if unstable:
        plt.text(0, -1.3, 'Unstable system\n(Poles outside the unit circle)', 
                 color='red', fontsize=12, ha='center', va='top', fontweight='bold')
    else:
        plt.text(0, -1.3, 'Stable system\n(Poles inside the unit circle)', 
                 color='green', fontsize=12, ha='center', va='top', fontweight='bold')
    if fs is not None:
        freqs = []
        for p in poles:
            angle = np.angle(p)
            if angle != 0:  # ignorar polos reales
                f = (angle / (2 * np.pi)) * fs
                freqs.append(f)
    if freqs:
        text = "Frecuencias naturales:\n" + "\n".join(f"{f:.2f} Hz" for f in freqs)
        plt.subplot(1, 3, 3)
        plt.text(1.1, -1.2, text, fontsize=10, color='blue', va='top')
            
    plt.tight_layout()
    plt.show()

    

def H_ejw(A_z,B_z,omega=False,plot=False):
    """
    Computes the frequency response H(e^{jω}) of a digital filter given its numerator and denominator coefficients.
    Parameters
    ----------
    Y_z : array_like
        Sequence of numerator coefficients (b_k) of the filter's transfer function.
    X_z : array_like
        Sequence of denominator coefficients (a_k) of the filter's transfer function.
    omega : float or array_like
        Frequency value(s) (in radians/sample) at which to evaluate the frequency response.
    Returns
    -------
    complex or ndarray
        The computed frequency response H(e^{jω}) at the specified frequency or frequencies.
    Notes
    -----
    The function evaluates the transfer function:
        H(e^{jω}) = (Σ b_k * e^{-jωk}) / (Σ a_k * e^{-jωk})
    where the sums are over the indices of the numerator and denominator coefficients, respectively.
    Optional
    -----
    Make plot=True for a plot of the result.
    """
    
    # H(e^jωk)
    # H(e^jωk) = Y_z(e^jωk) / X_z(e^jωl) k and l are the powers of Z^-k, Z^-l
    #                                    for the num and den accordingly.
    # num: the result of the expression in the numerator
    # den: the result of the expression in the denominator
    
    if omega is False or omega is None:
        omega = np.linspace(-np.pi, np.pi, 512)
    
    # Evaluate numerator: sum b_k * e^{-jωk}
    num = sum(bk * np.exp(-1j * omega * (-k)) for k, bk in enumerate(A_z))

    # Evaluate denominator: sum a_k * e^{-jωk}
    den = sum(ak * np.exp(-1j * omega * (-k)) for k, ak in enumerate(B_z))
    H =  num/den
    if plot:
        plot_H_ejw(omega, H, A_z, B_z, 1000)
    return

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
    zt.H_ejw(A_z, B_z,False,False,True);
    
    # Problem 2
    A_z = [0,1];
    B_z = [1,-1,-1];
    zt.H_ejw(A_z, B_z,False,False,True);
    
    # Problem 3
    A_z = [7];
    B_z = [1,-2,6];
    zt.H_ejw(A_z, B_z,False,False,True);
    
    # Problem 4
    A_z = [2 ** k for k in range(8)]
    B_z = [1];
    zt.H_ejw(A_z, B_z,False,True);
    
    return

main();