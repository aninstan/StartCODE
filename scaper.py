import requests
import pandas as pd
from datetime import datetime

# Define a function to fetch data
def fetch_nordpool_prices(year, month, day, price_area):
    # Format the URL with the provided parameters
    url = f"https://www.hvakosterstrommen.no/api/v1/prices/{year}/{month:02d}-{day:02d}_{price_area}.json"
    
    # Make the GET request
    response = requests.get(url)
    
    # Check for a successful response
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        data = pd.DataFrame(data)
        data = data.drop(columns=['EUR_per_kWh', 'EXR', 'time_start', 'time_end']) 
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Fetch data
data = fetch_nordpool_prices(2024, 10, 25, "NO5")