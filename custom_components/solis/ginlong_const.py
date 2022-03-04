"""
  Access to the Ginlong platform 2.0 API for PV monitoring.
  Works for all Ginlong brands using the Ginlong Platform 2.0 portal API
  Solis, Solarman, Sofar Solar and possibly MyEvolveCloud

  For more information: https://github.com/hultenvp/solis-sensor/
"""

# VERSION
VERSION = '0.1.0'

INVERTER_SERIAL = 'serial'
INVERTER_PLANT_ID = 'plantID'
INVERTER_LAT = 'lat'
INVERTER_LON = 'lon'
INVERTER_ADDRESS = 'address'
INVERTER_DEVICE_ID = 'deviceId'
INVERTER_DATALOGGER_SERIAL = 'dataloggerSerial'
INVERTER_TIMESTAMP_ONLINE = 'timestampOnline'
INVERTER_TIMESTAMP_UPDATE = 'timestampUpdate'
INVERTER_TEMPERATURE = 'inverterTemperature'
INVERTER_POWER_LIMIT = 'inverterPowerLimit'
INVERTER_ACPOWER = 'acPower'
INVERTER_ACFREQUENCY = 'acFrequency'
INVERTER_ENERGY_LAST_MONTH = 'energyLastMonth'
INVERTER_ENERGY_TODAY = 'energyToday'
INVERTER_ENERGY_THIS_MONTH = 'energyThisMonth'
INVERTER_ENERGY_THIS_YEAR = 'energyThisYear'
INVERTER_ENERGY_TOTAL_LIFE = 'energyTotalLife'
INVERTER_POWER_STATE = "powerState"
INVERTER_STATE = "state"
RADIATOR1_TEMP = "radiatorTemp1"
STRING1_VOLTAGE = 'dcVoltage1'
STRING2_VOLTAGE = 'dcVoltage2'
STRING3_VOLTAGE = 'dcVoltage3'
STRING4_VOLTAGE = 'dcVoltage4'
STRING1_CURRENT = 'dcCurrent1'
STRING2_CURRENT = 'dcCurrent2'
STRING3_CURRENT = 'dcCurrent3'
STRING4_CURRENT = 'dcCurrent4'
STRING1_POWER = 'dcPower1'
STRING2_POWER = 'dcPower2'
STRING3_POWER = 'dcPower3'
STRING4_POWER = 'dcPower4'
PHASE1_VOLTAGE = 'acVoltage1'
PHASE2_VOLTAGE = 'acVoltage2'
PHASE3_VOLTAGE = 'acVoltage3'
PHASE1_CURRENT = 'acCurrent1'
PHASE2_CURRENT = 'acCurrent2'
PHASE3_CURRENT = 'acCurrent3'
BAT1_REMAINING_CAPACITY = 'packRemainingCapacity1'
BAT_REMAINING_CAPACITY = 'remainingCapacity'
BAT_TOTAL_ENERGY_CHARGED = 'totalEnergyCharged'
BAT_TOTAL_ENERGY_DISCHARGED = 'totalEnergyDischarged'
BAT_DAILY_ENERGY_CHARGED = 'dailyEnergyCharged'
BAT_DAILY_ENERGY_DISCHARGED = 'dailyEnergyDischarged'
GRID_DAILY_ON_GRID_ENERGY = 'dailyOnGridEnergy'
GRID_DAILY_ENERGY_PURCHASED = 'dailyEnergyPurchased'
GRID_DAILY_ENERGY_USED = 'dailyEnergyUsed'
GRID_MONTHLY_ENERGY_PURCHASED = 'monthlyEnergyPurchased'
GRID_MONTHLY_ENERGY_USED = 'monthlyEnergyUsed'
GRID_YEARLY_ENERGY_PURCHASED = 'yearlyEnergyPurchased'
GRID_YEARLY_ENERGY_USED = 'yearlyEnergyUsed'
GRID_TOTAL_ON_GRID_ENERGY = 'totalOnGridEnergy'
GRID_TOTAL_CONSUMPTION_ENERGY = 'totalConsumptionEnergy'
GRID_TOTAL_POWER = 'totalPower'
GRID_TOTAL_CONSUMPTION_POWER = 'totalConsumptionPower'
GRID_TOTAL_ENERGY_USED = 'totalEnergyUsed'
