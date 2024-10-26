def unoptimize_battery_schedule(battery_capacity_kWh, battery_charge_rate_kW, spot_price, load_kWh, pv_production_kWh, init_battery_soc):
    # [Previous function implementation goes here]
    hours = len(spot_price)
    state_of_charge = [0] * hours  # % of battery capacity
    power_from_grid = [0] * hours  # kW (positive = charging, negative = discharging)
   
    # Initialize first hour with provided initial SOC
    net_load = load_kWh[0] - pv_production_kWh[0]
    state_of_charge[0] = init_battery_soc
    intialEnergyInBattery = state_of_charge[0]/100 * battery_capacity_kWh




    # Intial hour calculations
    if net_load > battery_charge_rate_kW or net_load > intialEnergyInBattery:
        power_from_grid[0] = net_load - min(battery_charge_rate_kW, intialEnergyInBattery)
        state_of_charge[0] = ((intialEnergyInBattery  - min(battery_charge_rate_kW, intialEnergyInBattery))/battery_capacity_kWh)*100
    else:
        power_from_grid[0] = 0
        state_of_charge[0] = ((intialEnergyInBattery - net_load)/battery_capacity_kWh)*100


    if state_of_charge[0] > 100:
        power_from_grid[0] -= ((state_of_charge[0] - 100)/100)*battery_capacity_kWh
        state_of_charge[0] = 100


    # All other hours
    for hour in range(1, hours):
        net_load = load_kWh[hour] - pv_production_kWh[hour]
        EnergyInBattery = state_of_charge[hour-1]/100 * battery_capacity_kWh




        if net_load > battery_charge_rate_kW or net_load > EnergyInBattery:
            power_from_grid[hour] = net_load - min(battery_charge_rate_kW, EnergyInBattery)
            state_of_charge[hour] = ((intialEnergyInBattery  - min(battery_charge_rate_kW, EnergyInBattery))/battery_capacity_kWh)*100
        else:
            power_from_grid[hour] = 0
            state_of_charge[hour] = ((EnergyInBattery - net_load)/battery_capacity_kWh)*100


        if state_of_charge[hour] > 100:
            power_from_grid[hour] -= ((state_of_charge[hour] - 100)/100)*battery_capacity_kWh
            state_of_charge[hour] = 100


    return state_of_charge, power_from_grid


