import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# This Document Generates the year_data_flattened.csv file based on the data_hourly.csv file. Thus this script doesnt need to be called except for
# the first time you have to initialize year_data_flattened.


# The function for getting the mean value for the Demand in kWh
def consumption(file_path):
    # Load and clean the data
    data = pd.read_csv(file_path).dropna()
    data = data.head(100000)
    
    # Take the mean of 'Demand_kWh' for each hour, over all days and for all households. This will give a list that shows ish how the demand varies over 
    # the 0-24 hours of a day. Note that the dataset is only for three months of winter, which is why we think it will give an ish good result, where everything
    # doesnt cancel each other.
    hourly_mean_demand = data.groupby('Hour')['Demand_kWh'].mean()    
    return hourly_mean_demand

# Load hourly mean demand from the file
hourly_mean_demand = consumption("skibidi.csv")

def noise_function(x):
    # Add Gaussian noise to each data point
    return x + np.random.normal(0, 0.05)

year_data = []

#Since we are not going to use this data for the actual average demand (this is done earlier in the Simulation.py file), we will just use it for the
# variation that is from hour to hour during the day. Thus we will remove the average of the hourly_mean_demand, so that the average when we add this list later
# is kept the same.

hourly_mean_demand = hourly_mean_demand - np.average(hourly_mean_demand)

for _ in range(365):
    daily_data = hourly_mean_demand.apply(noise_function)  
    year_data.append(daily_data.values)  

year_data = np.array(year_data)

w = 2 * np.pi / (24 * 365)
for i, day_data in enumerate(year_data):
    year_data[i] = day_data * (1 + np.sin(w*i))


year_data_flattened = year_data.flatten()
x_ticks = np.arange(0, 365 * 24, 24)
x_labels = [f'Day {i+1}' for i in range(365)]

#dump the data to a csv file
year_data_flattened = pd.DataFrame(year_data_flattened)
year_data_flattened.to_csv("year_data_flattened.csv")


plt.figure(figsize=(18, 6))
plt.plot(year_data_flattened)
plt.xticks(x_ticks, x_labels, rotation=90)  
plt.title("Year")
plt.xlabel("Day")
plt.ylabel("Demand")
plt.tight_layout()

plt.show()