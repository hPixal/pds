import numpy as np
import matplotlib.pyplot as plt

def check_ergodicity(S, k, tol):
    """
    The method i'll be doing it's the following
    1 - Split the signal S into K equal-sized subsets (folds)
    2 -  For each fold i from 1 to K:
        2.1 - Calculate mean
        2.2 - Calculate variance
        2.3 - Calculate amplitude
        2.4 - Store results of the fold
    3 - For statistical check that is in the accepted tolerance
    """
    # Step 1: Split the signal into K equal-sized subsets
    subsets = np.array_split(S, k)
    
    means = []
    variances = []
    amplitudes = []
    
    # Step 2: Process each subset
    for subset in subsets:
        # 2.1 Calculate mean
        mean = np.mean(subset)
        means.append(mean)
        
        # 2.2 Calculate variance
        variance = np.var(subset)
        variances.append(variance)
        
        # 2.3 Calculate amplitude (max - min)
        amplitude = np.max(subset) - np.min(subset)
        amplitudes.append(amplitude)
    
    # Step 3: Check if the statistics are within the tolerance
    mean_diff = np.max(means) - np.min(means)
    variance_diff = np.max(variances) - np.min(variances)
    # amplitude_diff = np.max(amplitudes) - np.min(amplitudes)
    
    if mean_diff <= tol and variance_diff <= tol:
        return True, means, variances, amplitudes  # Signal is ergodic
    else:
        return False, means, variances, amplitudes  # Signal is not ergodic


N = 500  # Number of samples
signal = np.random.normal(loc=0, scale=1, size=N)  # Mean=0, Std Dev=1
k = 4  # Number of folds
tol = 0.5  # Tolerance

# Check ergodicity
is_ergodic, means, variances, amplitudes = check_ergodicity(signal, k, tol)

# Plot the signal
plt.figure(figsize=(10, 6))
plt.stem(signal, label="Signal")
plt.title("Signal with Folds and Statistical Analysis")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")

# Add vertical lines for folds
fold_indices = np.linspace(0, N, k + 1, dtype=int)
for idx in fold_indices:
    plt.axvline(x=idx, color='red', linestyle='--', alpha=0.7)

# Add text at the bottom with statistics and ergodicity result
stats_text = (
    f"Means: {np.round(means, 2)}\n"
    f"Variances: {np.round(variances, 2)}\n"
    f"Amplitudes: {np.round(amplitudes, 2)}\n"
    f"Ergodic: {'Yes' if is_ergodic else 'No'}"
)
print(stats_text);
plt.figtext(0.125,0.9, stats_text, wrap=True, horizontalalignment='left', fontsize=9)

plt.legend()
plt.show()


