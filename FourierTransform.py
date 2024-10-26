import numpy as np
import matplotlib.pyplot as plt

def fourier_series(data, N,time, timestep):
    L = len(data)*timestep
    series = np.zeros_like(data, dtype=float)
    series += np.mean(data) 
    for n in range(1, N + 1):
        # Calculate coefficients
        a_n = (2 / L) * np.sum(data * np.cos(2 * np.pi * n * time / L))
        b_n = (2 / L) * np.sum(data * np.sin(2 * np.pi * n * time / L))
        series += a_n * np.cos(2 * np.pi * n * time / L) + b_n * np.sin(2 * np.pi * n * time / L)
    return series

