import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# The function for getting the mean value for the Demand in kWh
def consumption(file_path):
    # Load and clean the data
    data = pd.read_csv(file_path).dropna()
    data = data.head(100000)
    
    # Take the mean of 'Demand_kWh' for each hour
    hourly_mean_demand = data.groupby('Hour')['Demand_kWh'].mean()    
    return hourly_mean_demand

# Load hourly mean demand from the file
hourly_mean_demand = consumption("skibidi.csv")

def noise_function(x):
    # Add Gaussian noise to each data point
    return x + np.random.normal(0, 0.05)

# def generate_sine_wave(amplitude, length):
#     # Generate a sine wave pattern with a given amplitude and length
#     frequency = 2 * np.pi / length
#     phase_shift = np.pi / 2
#     days = np.arange(length)
#     sine_wave = amplitude * np.sin(frequency * days + phase_shift)
#     return sine_wave

year_data = []

hourly_mean_demand = hourly_mean_demand - np.average(hourly_mean_demand)
# Step 2: Generate 365 days of noisy demand data
for _ in range(365):
    daily_data = hourly_mean_demand.apply(noise_function)  
    year_data.append(daily_data.values)  

year_data = np.array(year_data)
# sine_wave = generate_sine_wave(0.1, 365)  # Generate a sine wave for 365 days

# for i, day_data in enumerate(year_data):
#     year_data[i] = day_data * (1 + sine_wave[i])

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