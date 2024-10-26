import numpy as np
import matplotlib.pyplot as plt


# Fourier_series takes following inputs : 
# data ; the dataset you want to make a fourierseries from.
# It is important that this set is periodic within the timescale provided.
# N is how many harmonic overfrequencies we want.
# timelist is the time value we want to generate values for.
def fourier_series(data, N,T, timelist):
    a0 = np.average(data) # Equilibrium component.
    returnarr = np.zeros(len(timelist)) + a0
    temptlist = np.linspace(-T/2,T/2,len(data))
    dt = T / (len(temptlist))
    # Calculating Fourier-Coeffisients
    for n in range(1,N+1):
        w = 2 * np.pi * n / T
        # Calculating Coefficients via Riemann sums
        a_n = 2 / T * np.sum(data * np.cos(w*temptlist)) * dt
        b_n = 2 / T * np.sum(data * np.sin(w*temptlist)) * dt
        for i, t in enumerate(timelist):
            returnarr[i] += a_n * np.cos(w*t) + b_n * np.sin(w*t)
    return returnarr


















    # L = len(data) # The period
    # series = np.zeros_like(data*24/timestep, dtype=float)
    # series += np.mean(data) 
    # for n in range(1, N + 1):
    #     # Calculate coefficients
    #     a_n = (2 / L) * np.sum(data * np.cos(2 * np.pi * n * time / L))
    #     b_n = (2 / L) * np.sum(data * np.sin(2 * np.pi * n * time / L))
    #     series += a_n * np.cos(2 * np.pi * n * time / L) + b_n * np.sin(2 * np.pi * n * time / L)
    # return series

