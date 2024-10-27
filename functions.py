import numpy as np

#  Fourier_series takes following inputs : 
# data ; the dataset you want to make a fourierseries from.
# It is important that this set is periodic within the timescale provided.
# N is how many harmonic overfrequencies we want.
# timelist is the time value we want to generate values for.
# T is the period over which the signal is
def fourier_series(data, N,T, timelist): #finner en fourierrekke for dataen.
    a0 = np.average(data) # Equilibrium component.
    returnarr = np.zeros(len(timelist)) + a0
    temptlist = np.linspace(0,T,len(data))
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

# Beregn deklinasjon (delta)
def solcellepanel_effekt(A, eta, I0, phi, n, S, alpha, T, T0, t): #målt i watt
    delta = 23.44 * np.sin(np.radians((360 / 365) * (n - 81)))

    # Beregn timevinkel (omega)
    omega = 15 * (t - 12)

    # Beregn solhøyde (h)
    h = np.degrees(np.arcsin(np.sin(np.radians(phi)) * np.sin(np.radians(delta)) +
                            np.cos(np.radians(phi)) * np.cos(np.radians(delta)) * np.cos(np.radians(omega))))

    # Endelig formel for estimert effekt (P)
    P = A * eta * I0 * np.sin(np.radians(h)) * (1 - S) * (1 - alpha * (T - T0))

    return P