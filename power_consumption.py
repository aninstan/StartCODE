import matplotlib.pyplot as plt
import pandas as pd

def handle_data(filename):
    df = pd.read_csv(filename)
    df = df.dropna()
    return df

def consumption_data(data):
    # gruppere dataen etter dato og finne gjennomsnittlig forbruk per dag
    data['From'] = pd.to_datetime(data['From'])
    data['From'] = data['From'].dt.date
    data['From'] = pd.to_datetime(data['From'])
    
    daily_consumption = data.groupby('From')['Demand_kWh'].mean()
    return daily_consumption

def plot_consumption(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data.values, 'b-', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Consumption (kWh)')
    plt.title('Daily Energy Consumption')
    plt.grid(True)
    plt.show()

def main():
    # Handle data
    filename = 'data_hourly.csv'
    data = handle_data(filename)
    daily_consumption = consumption_data(data)
    plot_consumption(daily_consumption)

main()