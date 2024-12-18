import numpy as np
import matplotlib.pyplot as plt
from bokeh.io import export_svgs
from bokeh.plotting import curdoc, figure, show

import Simulation
import Generert_spotPris
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
startTime = 1 # Startday from 1-365
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
                                   family_size, location[2], solarpanelArea, eta, I0, None, alpha, None, T0)


# Konstant
energyEfficiencyConstant = simulation.house.getEnergyEfficiencyConstant() # House Area and energylabel contribution to the powerusage
medianTemp = simulation.TemperatureSimulator() # Estimate used for calculating more accurate temperature data


# Generated spotprices
tlist = np.arange(0,24)
spotPrices = []

for i in range(startTime, endTime+1): # total days we want spotprices over
    daySpotPrices = Generert_spotPris.spotpris_dagen(tlist, simulation.temperatur(i, medianTemp[i]), Generert_spotPris.spotpris_gjennomsnitt(i)) # total values over a day, temperature, average spotprice for day
    for j in range(24):
        spotPrices.append(daySpotPrices[j])

# Generate PV-production
tlist = np.arange(0,24)
PV_Production = []

for i in range(startTime, endTime+1):
    for j in range(24):
        hourlyPV_Production = simulation.house.Solarpanels.solcellepanel_effekt(tlist, i, location[0], simulation.house.Solarpanels.S, (simulation.temperatur(i, medianTemp[i]))[j])
        PV_Production.append(hourlyPV_Production[j])

# plt.plot(ttt, PV_Production)
p = figure(title="3 days PV production", 
           x_axis_label='Hour', 
           y_axis_label='Prod', 
           x_range=(0, 24*3), 
           width=1000, 
           height=400, 
           output_backend="svg")

v = figure(title="Year", 
           x_axis_label='Hour', 
           y_axis_label='Spotprice', 
           x_range=(0, 24*3), 
           width=1000, 
           height=400, 
           output_backend="svg")



p.background_fill_color = None
p.border_fill_color = None
p.line(x=np.arange(24*3), y=hourlyPV_Production, line_width=2)

v.background_fill_color = None
v.border_fill_color = None
v.line(x=, y=spotPrices, line_width=2)

p.title.text_color = "white"  
p.xaxis.axis_label_text_color = "white"  
p.yaxis.axis_label_text_color = "white"  
p.xaxis.major_label_text_color = "white"
p.yaxis.major_label_text_color = "white" 

v.title.text_color = "white"
v.xaxis.axis_label_text_color = "white"
v.yaxis.axis_label_text_color = "white"
v.xaxis.major_label_text_color = "white"
v.yaxis.major_label_text_color = "white"

export_svgs(p, filename="static/Pvplot.svg")
export_svgs(p, filename="static/Spotplot.svg")