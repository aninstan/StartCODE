import numpy as np

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


class House:
    #OOOPS: house_area is just the part of the house that is actually heated.

    def __init__(self, energy_label="G", house_area=124, house_placement=None, family_size=2, SolarPanelArea = 10):
        if house_placement is None:
            house_placement = [0, 0]  # Avoid mutable default argument

        self.energy_label = energy_label
        self.house_area = house_area
        self.house_placement = house_placement
        self.family_size = family_size
        self.PowerUsage = 0.0
        self.PowerConditionsFactor = 1.0  # Specify the type for clarity
        self.SolarPanelArea = SolarPanelArea

        scalingfac: float = 1.0  # This is where we import the factor From Anine
        self.setPowerConditionsFactor(scalingfac)
        self.setPowerUsage()  # No need to pass area_increments

    def setPowerUsage(self):
        ClosestAreaIndex = (np.abs(self.house_area - AREA_INCREMENTS)).argmin()  # Access the global constant
        self.PowerUsage = energy_data[self.energy_label][AREA_INCREMENTS[ClosestAreaIndex]] * self.PowerConditionsFactor

    def setPowerConditionsFactor(self, powfac):
        self.PowerConditionsFactor = powfac

# Create an instance of House
house = House()


# Define area_increments as a global constant
