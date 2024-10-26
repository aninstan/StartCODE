import numpy as np
import HouseClass
import SolarPanel
import FourierTransform

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
        17.93, 18.5, 21.37, 21.79, 20.21, 21.82, 22.53, 22.55, 20.13, 
        17.67, 18.24, 18.69, 17.79, 16.69, 15.81, 17.14, 16.24, 15.38, 
        15.54, 15.40, 14.04, 13.76, 13.31, 12.41, 12.18, 12.47, 12.32, 
        12.30, 12.02, 11.83, 11.72, 11.57, 12.0, 12.25, 12.71, 12.66, 
        12.67, 12.63, 13.29, 13.58, 13.43, 13.62, 15.07, 15.9, 15.01, 
        15.84]) * ConversionVariable

class Simulation:
    time, day, year = 12, 1, 2024
    month, textday = "january", "1"
    temp, clouds = [], []
    numhouses, timestep = 10**2, 4 # 24 needs to be divisible by timestep
    houses = np.zeros(numhouses)

    timelist = np.arange(0,len(data),24/ timestep * len(data))
    EstimatedGeneralPower = FourierTransform.fourier_series(data, 10, timelist, timestep)


    def _init_(self,locations = None,areas = None,energylabels = None, solarpanelareas = None):
        for i in range(self.numhouses):
            self.houses[i] = HouseClass.House()


    def Simulator(self):
        for day in range(365):
            for time in range(24 / self.timestep):
                for house in self.houses:
                    self.TemperatureSimulator(house)
                    self.WeatherSimulator(house)
                    

                self.TimePasser(self)


    def TemperatureSimulator(self, house):
        a = 2


    def WeatherSimulator(self, house):
        a =2

def TimePasser(self):
        if time<23:
            time += self.timestep
        if time==24:
            time = 0
            day += 1
        if day == 365:
            year +=1


simulation = Simulation()