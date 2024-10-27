import numpy as np
import HouseClass
import functions
import random as rd
import pandas as pd
# import Temperature_during_day
import matplotlib.pyplot as plt

import HouseClass

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


# Since our data contains values for two periods (two years) we choose to look at the average when we later calculate the fourierseries
average_data = []
for n in range(int(len(data)/2)):
    data1 = data[n] 
    data2 = data[n+52]
    average_data.append((data1+data2)/2) 

average_data = average_data[0:len(average_data)-3] # For practical purposes we make this excactly 52 weeks long.


class Simulation:
    temp, clouds = [], []
    HourlyPowerConsumption = [] # Holds the watt used each hour

    def __init__(self, StartTime = 1, EndTime = 31, energy_label="E", house_area=108, house_placement=[63.4468,10.4219], family_size=2, CurrentRegion = "NO3", SolarPanelArea = 10,
                 eta = 0.2, I0 = 1000, S = 0.3, alpha = 0.004, T = 10, T0 = 25, city_code = "1-92416"):
        
        self.house = HouseClass.House(energy_label, house_area, house_placement, family_size, CurrentRegion, SolarPanelArea,
                eta, I0, S, alpha, T, T0, city_code)
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.timelist = np.arange((StartTime-1)*24, EndTime*24, 1)

        
        # Generating values for how much energy is used each hour

        self.EnergyConsumptionGenerator()
        

        # Generating weather values, specifically the temperature for each hour and cloudiness for each hour
    def temperatur(self, dag_i_aret, temp_avg):  # Generating temperatures throughout the day
        theta = 2 * np.pi / 3  # Phase shift, maximum temperature occurs around 14:00
        t = np.arange(0, 24)

        # Deviation between maximum and minimum temperature throughout the day
        maks_avvik = 10
        min_avvik = 3
        gjennomsnitt_avvik = (maks_avvik + min_avvik) / 2
        amplitude = (maks_avvik - min_avvik) / 2
        avvik = gjennomsnitt_avvik + amplitude * np.sin(2 * np.pi * (dag_i_aret - 172) / 365)
        A = avvik / 2  # Amplitude (half of the difference between max and min)

        mue = 0  # Initial expected deviation
        T = 24  # Minutes in a day
        temp_uten_stoy = A * np.sin(t * 2 * np.pi / 24 - theta) + temp_avg  # Calculation of temperature without noise
        random_avvik_liste = []

        for i in range(T):
            if i == 0:
                mue = 0
            else:
                mue = random_avvik_liste[i - 1]
            random_avvik = np.random.normal(mue, 0.08)
            random_avvik_liste.append(random_avvik)

        temp_list_minutt = temp_uten_stoy + random_avvik_liste  # Temperature list for each minute
        temp_list_hour = [float(temp_list_minutt[i]) for i in range(24)]  # Convert to regular floats for each hour

        return temp_list_hour


    #     # Initializing all the buildings that is inside the simulation
    # def generate_spot_prices(self, temp_avg = np.arange(10,10, 365)):
    #     temperature = []
    #     spot_prices = []
        
    #     hours = np.arange(0,24, 1)
    #     for i in range(self.StartTime, self.EndTime):
    #         if (i+1)%60 == 0:
    #             temperature.append(self.temperatur(i, temp_avg))
        
    #     for i in range(self.EndTime-self.StartTime):
    #         spot_pris = Generert_spotPris.spotpris(temperature, i)
    #         spot_prices.append(spot_pris)

    #     return spot_prices, temperature
    
    def EnergyConsumptionGenerator(self):
        # First gnerating the average power usage for each day of the year. 
        DayBasedTimeList = np.linspace(self.StartTime,self.EndTime,self.EndTime-self.StartTime) # Same as self.timelist, but only holds one value per da
        DailyMeanPowerConsumption = functions.fourier_series(average_data, 4, 365, DayBasedTimeList ) # Holds the average Power usage of all days thats between self.starttime and self.endtime
        
        
        #Then including noise based on the probability distribution generated through StocasticVariation
        # Simulates and generates the difference that is from the seemingly periodic part of the "data" curve
        StocasticVariation = average_data - functions.fourier_series(average_data, 4, 52, np.linspace(0,52,len(average_data))) 
        for i in range(len(DailyMeanPowerConsumption)):
            randVarind = (rd.randint(0,len(StocasticVariation)-1))
            DailyMeanPowerConsumption[i] += StocasticVariation[randVarind] 
        
        #Making a dataset that has a power usage variation throughout the day, taking the average power usage for that day into account
        #Daily Variation Set comes only from three months during winter, which is why we choose to only use it for variation and not average temperature during the day

        dailyvar = pd.read_csv("year_data_flattened.csv")
        time = dailyvar['Hour'].values
        power_variation = dailyvar['PowerConsumption'].values
        power_variation = power_variation[(self.StartTime-1) * 24:self.EndTime*24] # We only use the hours that is between the Start and End Days
        HourlyPowerConsumption = []

        for i, hourlyvariation in enumerate(power_variation):
            if (i) % 24 == 0:
                DailyIndex = int((i)/24)
                print(DailyIndex)
                DailyValue = DailyMeanPowerConsumption[DailyIndex-1]
            HourlyPowerConsumption.append(DailyValue + hourlyvariation)

        self.HourlyPowerConsumption = HourlyPowerConsumption


    def TemperatureSimulator(self):
        # Load the original mean temperatures from the text file
            df = pd.read_csv("mean_temperatures.txt")

            tList = np.arange(len(df[" Mean Temperature"]))
            PureSinus = functions.fourier_series(df[" Mean Temperature"],1 , len(df[" Mean Temperature"]), tList)
            PureSinus = functions.fourier_series(df[" Mean Temperature"],1 , len(df[" Mean Temperature"]), tList)
            VariationDistribution = PureSinus - df[" Mean Temperature"]
            GeneratedYearlyTemp = PureSinus
            for i in range(len(VariationDistribution)):
                randInd = rd.randint(0,len(VariationDistribution)-1) 
                GeneratedYearlyTemp[randInd] += VariationDistribution[randInd]/2
            
            
            StartDay, EndDay = HouseClass.date_to_days(df["Date"].iloc[0]), HouseClass.date_to_days(df["Date"].iloc[-1])
            return GeneratedYearlyTemp

    def WeatherSimulator(self, house):
        a =2




    


    
# simulation = Simulation()

# xliste = simulation.timelist
# liste = simulation.EstimatedGeneralPower
# fig, ax = plt.subplots()
# ax.plot(xliste,liste)
# plt.show()

# print(len(data))

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