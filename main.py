import Simulation
### Antar at anine vil oppdatere disse variablene basert på input fra nettside, hvis ikke gitt, sett til None, så vil defaultparametre bli brukt ###

# House:
energy_label = "E" 
house_area = 108
family_size = 2
CurrentRegion = "NO3"

# Solarpanel:
solarpanelArea = 1 # Total solar panel area.
eta = 0.2 # Efficiency of the type of solar panel.
I0 = 1000 # Maximum solar irradiance under clear sky conditions.
alpha = 0.004 # Temperature coefficient.
T0 = 25 # Reference temperature.

# Location and time
startTime = 0 # Startday from 1-365
endTime = 31 # Endday from 1-365

locations = {
    1: [60.39299, 5.32415, "NO5", 1-92416], # Bergen
    2: [63.4468, 10.4219, "NO3", 1-211102], # Trondheim
    3: [59.9139, 10.7522, "NO1", 1-72837],  # Oslo
    4: [59.7433, 10.2045, "NO1", 1-58733],  # Drammen
    5: [58.9690, 5.7331, "NO2", 1-15183],   # Stavanger
}
location = locations[2] # Data about location based of chosen location


### Start Code #### (pun intended)

simulation = Simulation.Simulation(startTime, endTime, energy_label, house_area, (location[0], location[1]), 
                                   family_size, location[2], solarpanelArea, "remove", eta, I0, None, alpha, None, T0)




