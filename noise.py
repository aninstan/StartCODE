import numpy as np
import pandas as pd
import FourierTransform
import random as rd
import matplotlib.pyplot as plt

month_days = {
    1: 31,  # January
    2: 28,  # February (29 dager i skuddår)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

def date_to_days(df): #konverterer dato til dag i året
    month = int(df[5:7])  
    date = int(df[8:10]) 
    temp_måned_dager = 0

    for i in range(1, month):
        temp_måned_dager += month_days[i]

    antall_dager = date + temp_måned_dager
    return antall_dager

# Load the original mean temperatures from the text file
df = pd.read_csv("mean_temperatures.txt")

tList = np.arange(len(df[" Mean Temperature"]))
PureSinus = FourierTransform.fourier_series(df[" Mean Temperature"],1 , len(df[" Mean Temperature"]), tList)
VariationDistribution = PureSinus - df[" Mean Temperature"]
GeneratedYearlyTemp = PureSinus
for i in range(len(VariationDistribution)):
    randInd = rd.randint(0,len(VariationDistribution)-1) 
    GeneratedYearlyTemp[randInd] += VariationDistribution[randInd]/2

# plt.plot(tList, GeneratedYearlyTemp)
# plt.show()
    
StartDay, EndDay = date_to_days(df["Date"].iloc[0]), date_to_days(df["Date"].iloc[-1])

print(StartDay, EndDay)