import numpy as np
import HouseClass
# import SolarPanel
import FourierTransform
import matplotlib.pyplot as plt
import random as rd
import pandas as pd

TotHouseHolds = 2.6 * 10**6
PowerUsageOfHouseHold = 0.3
ConversionVariable = 10**9 * (PowerUsageOfHouseHold / TotHouseHolds) / 10**3
data = np.array([14.64, 14.9, 15.18, 15.51, 16.97, 18.88, 18.35, 17.46, 18.52, 18.35, #Holds the Power in KW
        18.35, 18.53, 17.83, 17.32, 17.97, 17.85, 17.78, 18.31, 18.7, 
        18.13, 17.82, 19.16, 18.44, 17.74, 17.19, 17.08, 16.98, 15.11, 
        15.52, 14.08, 14.73, 14.37, 15.05, 13.13, 12.29, 11.94, 12.08, 
        11.75, 11.63, 12.02, 12.04, 11.57, 11.69, 11.53, 12.01, 12.13, 
        11.99, 12.49, 12.56, 13.19, 13.09, 13.62, 13.42, 13.95, 15.17, 
        16.19, 15.59, 15.57, 16.11, 16.57, 17.83, 18.49, 18.37, 17.96, 
        17.93, 18.5, 21.37, 21.58, 21.79, 20.21, 21.82, 22.53, 22.55, 20.13, 
        17.67, 18.24, 18.69, 17.79, 16.69, 15.81, 17.14, 16.24, 15.38, 
        15.54, 15.40, 14.04, 13.76, 13.31, 12.41, 12.18, 12.47, 12.32, 
        12.30, 12.02, 11.83, 11.72, 11.57, 12.0, 12.25, 12.71, 12.66, 
        12.67, 12.63, 13.29, 13.58, 13.65]) * ConversionVariable



class Simulation:
    time, day, year = 12, 1, 2024
    temp, clouds = [], []
    numhouses = 1
    houses = [None] * numhouses
    StartTime, EndTime = 0, 365 # Holds the start and end time of the simulation in days
    timelist = np.linspace(StartTime, EndTime, (EndTime-StartTime))
    PowerConsumption = [] # Holds the average power (Watts) a household uses based on the day of the year

    def __init__(self, locations=None, areas=None, energylabels=None, solarpanelareas=None):
        
        # Initializing all the buildings that is inside the simulation

        for i in range(self.numhouses):
            self.houses[i] = HouseClass.House()
    
    def EnergyConsumptionGenerator(self):
        # Generating the average power usage for each day of the year. 
        self.PowerConsumption = FourierTransform.fourier_series(data, 10, 365, self.timelist) # Holds the average Power usage of all days
        StocasticVariation = data - FourierTransform.fourier_series(data,10, 50, self.timelist)
        for i in range(len(self.DailyBasis)):
            randVarind = rd.randint(0,len(self.DailyBasis))
            self.PowerConsumption[i] += StocasticVariation[randVarind] # Simulates and generates the difference that is from the seemingly periodic part of the "data" curve

        #Making a dataset that has a power usage variation throughout the day, taking the average power usage for that day into account
            #Daily Variation Set comes only from three months during winter, which is why we choose to only use it for scaling
            dailyvar = pd.read_csv("year_data_flattened.csv")
            time = data['Hour'].values
            power_usage = data['PowerConsumption'].values

    def WeatherSimulationGenerator(self):
        []





    


    
simulation = Simulation()

xliste = simulation.timelist
liste = simulation.EstimatedGeneralPower
fig, ax = plt.subplots()
ax.plot(xliste,liste)
plt.show()

print(len(data))

# data = np.array([14.64, 14.9, 15.18, 15.51, 16.97, 18.88, 18.35, 17.46, 18.52, 18.35, #Holds the Power in KW
#         18.35, 18.53, 17.83, 17.32, 17.97, 17.85, 17.78, 18.31, 18.7, 
#         18.13, 17.82, 19.16, 18.44, 17.74, 17.19, 17.08, 16.98, 15.11, 
#         15.52, 14.08, 14.73, 14.37, 15.05, 13.13, 12.29, 11.94, 12.08, 
#         11.75, 11.63, 12.02, 12.04, 11.57, 11.69, 11.53, 12.01, 12.13, 
#         11.99, 12.49, 12.56, 13.19, 13.09, 13.62, 13.42, 13.95, 15.17, 
#         16.19, 15.59, 15.57, 16.11, 16.57, 17.83, 18.49, 18.37, 17.96, 
#         17.93, 18.5, 21.37, 21.58, 21.79, 20.21, 21.82, 22.53, 22.55, 20.13, 
#         17.67, 18.24, 18.69, 17.79, 16.69, 15.81, 17.14, 16.24, 15.38, 
#         15.54, 15.40, 14.04, 13.76, 13.31, 12.41, 12.18, 12.47, 12.32, 
#         12.30, 12.02, 11.83, 11.72, 11.57, 12.0, 12.25, 12.71, 12.66, 
#         12.67, 12.63, 13.29, 13.58, 13.65]) * ConversionVariable