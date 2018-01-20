import random
import time
import datetime

end_time = 1  # will gather input time, in minutes, from the GUI
start_time = time.time()


def getTemperature(temp):  # will be gathering temperature from thermometer
    #     randNum = random.uniform(60.00, 72.00)
    #     print(round(randNum,2), 'C')
    #     print(round((randNum * 1.8 + 32), 2), 'F')

    time_delta = 15
    target_temp = 67

    temp_delta_heat = (82.165 * time_delta / 3600)
    temp_delta_cool = (time_delta / 120)

    if HeaterON == True:  # temp < target_temp:
        temp += temp_delta_heat
    print(temp)

    elif HeaterON == False:  # temp > target_temp:
    temp -= temp_delta_cool
    print(temp)


    return temp


def logic(temp, maxTemp, minTemp):  # Determine if heater needs to be turned on/off
    if temp >= maxTemp:
        print('turn heat off')
        HeaterON = False
    elif temp <= minTemp:
        print('turn heat on')
        HeaterON = True
    else:
        print('maintain current heat')


# Define global variables
GLOBAL_maxTemp = 68
GLOBAL_minTemp = 64
HeaterON = True
Temp_actual = 55

getTemperature(55)