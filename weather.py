import requests
import pandas as pd

def weather_forecast(lat, lon):
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    params = {
        "lat": lat,
        "lon": lon
    }
    headers = {
        "User-Agent": "Your-Name - your-email@example.com"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        
        # Initialize lists to store data
        dates = []
        times = []
        temperatures = []
        cloudiness = []
        
        # Extract relevant data from each time-series entry
        for entry in data['properties']['timeseries']:
            dates.append(entry['time'][:10])
            times.append(entry['time'][11:-7])
            temperatures.append(entry['data']['instant']['details']['air_temperature'])
            cloudiness.append(entry['data']['instant']['details'].get('cloud_area_fraction', None))
        
        # Create a DataFrame from the lists
        df = pd.DataFrame({ 
            "date": dates,
            "time": times,
            "temperature": temperatures,
            "cloudiness": cloudiness
        })
        
        # Display the DataFrame
        return df
    else:
        print(f"Failed to retrieve data: {response.status_code}")

# Example usage
weather_forecast(59.9, 10.8)





def historical_weather(loc):
    # make 1-211102 a variable for the url

    url = f"https://www.yr.no/api/v0/locations/{loc}/observations/year"

# Set headers with User-Agent information
    headers = {
        "User-Agent": "Your-Name - your-email@example.com"
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Initialize lists to store daily data
        dates = []
        min_temps = []
        max_temps = []
        mean_temps = []

        # Loop through each month
        for month in data["historical"]["months"]:
            # Loop through each day within the month
            for day in month["days"]:
                # Store date
                dates.append(day["time"])

                temperature_data = day["temperature"]
                min_temps.append(temperature_data.get("min"))
                max_temps.append(temperature_data.get("max"))
                mean_temps.append(temperature_data.get("mean"))

        # Create DataFrame
        df = pd.DataFrame({
            "date": dates,
            "min_temperature": min_temps,
            "max_temperature": max_temps,
            "mean_temperature": mean_temps,
        })

        #clean up the data
        df["date"] = pd.to_datetime(df["date"])
        df = df.dropna()

        return df
    else:
        print(f"Failed to retrieve data: {response.status_code}")

# Example usage
historical_weather("1-211102")