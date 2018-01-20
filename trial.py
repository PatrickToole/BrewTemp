import random
import time
import datetime

end_time = .25 # will gather input time, in minutes, from the GUI
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
        print('heat off')
        return False
    elif temp <= minTemp:
        print('heat on')
        return True
    else:
        print('heat on')
        return True

# Define global variables
GLOBAL_maxTemp = 68
GLOBAL_minTemp = 64
Temp_actual = 55
HeaterON = logic(Temp_actual, GLOBAL_maxTemp, GLOBAL_minTemp)


while (time.time() - start_time) < (end_time * 60):
    print(datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S"))
    Temp_actual = getTemperature(Temp_actual)             # float(input('what is the temperature'))
    HeaterON = logic(Temp_actual, GLOBAL_maxTemp, GLOBAL_minTemp)
    time.sleep(0.1)
    print()