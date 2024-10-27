import numpy as np
import weather
import example


AREA_INCREMENTS = np.array([50, 75, 100, 125, 160, 200, 300, 400, 500])


# Define energy_data globally
energy_data = {
    'A': {50: 97.00, 75: 93.00, 100: 91.00, 125: 89.80, 160: 88.75, 200: 88.00, 300: 87.00, 400: 86.50, 500: 86.20},
    'B': {50: 115.00, 75: 108.33, 100: 105.00, 125: 103.00, 160: 101.25, 200: 100.00, 300: 98.33, 400: 97.50, 500: 97.00},
    'C': {50: 140.00, 75: 130.00, 100: 125.00, 125: 122.00, 160: 119.38, 200: 117.50, 300: 115.00, 400: 113.75, 500: 113.00},
    'D': {50: 179.00, 75: 164.33, 100: 157.00, 125: 152.60, 160: 148.75, 200: 146.00, 300: 142.33, 400: 139.40, 500: 139.00},
    'E': {50: 220.00, 75: 200.00, 100: 190.00, 125: 184.00, 160: 178.75, 200: 175.00, 300: 170.00, 400: 167.50, 500: 166.00},
    'F': {50: 280.00, 75: 253.33, 100: 240.00, 125: 232.00, 160: 225.00, 200: 220.00, 300: 213.33, 400: 210.00, 500: 208.00},
    'G': {50: 300.00, 75: 275.00, 100: 250.00, 125: 240.00, 160: 230.00, 200: 225.00, 300: 220.00, 400: 215.00, 500: 210.00},  # Example values
}

# Date convertion for PV-production
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
class SolarPanel:

    def __init__(self, A = 1, eta = 0.2, I0 = 1000, phi = 60, S = 0.3, alpha = 0.004, T = 10, T0 = 25):
        #Mange parametre som avhenger av solcellepanel-typen
        self.Area = A # Det totale arealet til solcellepanelene
        self.eta = eta # Virkningsgraden til solcellepaneltypen
        self.I0 = I0 # Maksimal solinnstråling under klare himmelforhold
        self.alpha = alpha # Temperaturkoeffisient
        self.T = T # Aktuell temperatur i omgivelsene 
        self.T0 = T0 # Referansetemperatur


    def solcellepanel_effekt(self, tlist, day, latitude, skyfactor, temperature): #målt i watt

        delta = 23.44 * np.sin(np.radians((360 / 365) * (day - 81)))

        # Beregn timevinkel (omega)
        omega = 15 * (tlist - 12)

        # Beregn solhøyde (h)
        h = np.maximum(0,np.degrees(np.arcsin(np.sin(np.radians(latitude)) * np.sin(np.radians(delta)) +
            np.cos(np.radians(latitude)) * np.cos(np.radians(delta)) * np.cos(np.radians(omega)))))
        
        # Beregn solhøyde (h)
                            # h = np.degrees(np.arcsin(np.sin(np.radians(phi)) * np.sin(np.radians(delta)) +
                            # np.cos(np.radians(phi)) * np.cos(np.radians(delta)) * np.cos(np.radians(omega))))
# Hva skjer med np.degrees og ikke np.maximum i den ene filen fra tidligere?


        # Endelig formel for estimert effekt (P)
        P = self.Area * self.eta * self.I0 * np.sin(np.radians(h)) * (1 - skyfactor) * (1 - self.alpha * (temperature - self.T0))

        return P
    



class House:
    #OOOPS: house_area is just the part of the house that is actually heated.
    AVERAGE_ENERGY = energy_data["E"][100] # Based on average energy label and average area for a household


    def __init__(self, energy_label="E", house_area=108, house_placement=None, family_size=2, CurrentRegion = "NO3", SolarPanelArea = 10,
                 eta = 0.2, I0 = 1000, S = 0.3, alpha = 0.004, T = 10, T0 = 25):
        
        if house_placement is None:
            house_placement = [0, 0]  # Avoid mutable default argument

        self.energy_label = energy_label
        self.house_area = house_area
        self.house_placement = house_placement
        self.latitude = house_placement[0]
        self.longitude = house_placement[1]
        self.family_size = family_size
        self.PowerUsage = 0.0
        self.PowerConditionsFactor = 1.0  # Specify the type for clarity
        self.CurrentRegion = CurrentRegion      
        self.Solarpanels = SolarPanel(SolarPanelArea,eta, I0, S, alpha, T, T0)
        self.Solarpanels = SolarPanel(SolarPanelArea,eta, I0, S, alpha, T, T0)

        self.setPowerUsage()

        self.weatherData = weather.weather_forecast(self.latitude, self.longitude)

    def PowerProduction(self, weatherData, date): #Time is a vector that holds the date 
        Power = []
        ValidHours = len(example.fetch_nordpool_prices(date[0], date[1], date[2], self.CurrentRegion)) # The amount of hours in the future that we have spot prices for, and thus finding the Solar generated power for.
        for i in range(ValidHours):
            day = date_to_days(weatherData['date'].iloc[i])
            Cloudiness = weatherData['cloudiness'].iloc[i]
            Temperature = weatherData['temperature'].iloc[i]
            Time = weatherData['time'].iloc[i]
            Power.append(self.solcellepanel_effekt(Time, day, self.latitude, Cloudiness, Temperature))
        return Power


    def setPowerUsage(self):
            ClosestAreaIndex = (np.abs(self.house_area - AREA_INCREMENTS)).argmin()  # Access the global constant
            self.PowerConditionsFactor = energy_data[self.energy_label][AREA_INCREMENTS[ClosestAreaIndex]] / self.AVERAGE_ENERGY # factor: Energy efficiency compared to average household





# Create an instance of House
house = House()


