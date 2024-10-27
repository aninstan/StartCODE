import numpy as np
import matplotlib.pyplot as plt
# import Simulation as sim


# Fourier_series takes following inputs : 
# data ; the dataset you want to make a fourierseries from.
# It is important that this set is periodic within the timescale provided.
# N is how many harmonic overfrequencies we want.
# timelist is the time value we want to generate values for.
# T is the period over which the signal is

TotHouseHolds = 2.6 * 10**6
PowerUsageOfHouseHold = 0.3
ConversionVariable = 10**9 * (PowerUsageOfHouseHold / TotHouseHolds) / 10**3
data = np.array([ 17.32, 17.97, 17.78, 18.31, 18.7, 
        18.13, 17.82, 19.16, 18.44, 17.74, 17.19, 17.08, 16.98, 15.11, 
        15.52, 14.08, 14.73, 14.37, 15.05, 13.13, 12.29, 11.94, 12.08, 
        11.75, 11.63, 12.02, 12.04, 11.57, 11.69, 11.53, 12.01, 12.13, 
        11.99, 12.49, 12.56, 13.19, 13.09, 13.62, 13.42, 13.95, 15.17, 
        16.19, 15.59, 15.57, 16.11, 16.57, 17.83, 18.49, 18.37, 
        17.93, 18.5, 21.37, 21.58, 21.79, 20.21, 21.82, 22.53, 22.55, 20.13, 
        17.67, 18.24, 18.69, 17.79, 16.69, 15.81, 17.14, 16.24, 15.38, 
        15.54, 15.40, 14.04, 13.76, 13.31, 12.41, 12.18, 12.47, 12.32, 
        12.30, 12.02, 11.83, 11.72, 11.57, 12.0, 12.25, 12.71, 12.66, 
        12.67, 12.63, 13.29, 13.58, 13.65, 14.64, 14.9, 15.18, 15.51, 16.97, 18.88, 18.35, 17.46, 18.52, 18.35, #Holds the Power in KW
        18.35, 18.53, 17.83]) * ConversionVariable

#finner effektforbruk hver uke i året basert på gjennomsnittet iløpet av 2 år
new_data=[]
for n in range(int(len(data)/2)):
    data1 = data[n] 
    data2 = data[n+52]
    new_data.append((data1+data2)/2) 

data = new_data






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
# data = sim.data

# timelist1=np.arange(0,len(data) * 7)
# timelist2=np.arange(0,len(new_data) * 7*2)

# T1=365*2
# T2 = 365
# n = 1
# returnarr1 = fourier_series(data, n, T1, timelist1)
# returnarr2 = fourier_series(new_data, n, T2, timelist2)







# # plt.plot(timelist1,returnarr1)
# plt.plot(timelist2,returnarr2)

# # plt.plot(np.linspace(0,365*2,52*2),data)
# plt.plot(np.linspace(0,365, 52), new_data)

# plt.show()


















    # L = len(data) # The period
    # series = np.zeros_like(data*24/timestep, dtype=float)
    # series += np.mean(data) 
    # for n in range(1, N + 1):
    #     # Calculate coefficients
    #     a_n = (2 / L) * np.sum(data * np.cos(2 * np.pi * n * time / L))
    #     b_n = (2 / L) * np.sum(data * np.sin(2 * np.pi * n * time / L))
    #     series += a_n * np.cos(2 * np.pi * n * time / L) + b_n * np.sin(2 * np.pi * n * time / L)
    # return series

