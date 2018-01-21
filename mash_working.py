import time
import datetime

end_time = float(input('How long would you like to mash for(minutes)')) # will gather input time, in minutes, from the GUI
start_time = time.time()


def getTemperature(temp):  # will be gathering temperature from thermometer

    time_delta = 15

    temp_delta_heat = (82.165 * time_delta / 3600)
    temp_delta_cool = (time_delta / 120)

    if HeaterON == True:  # temp < target_temp:
        temp += temp_delta_heat
        print(round(temp,2), 'C')
        print(round(temp*1.8+32, 2), 'F')

    elif HeaterON == False:  # temp > target_temp:
        temp -= temp_delta_cool
        print(round(temp,2), 'C')
        print(round(temp*1.8+32, 2), 'F')

    return temp


def logic(temp, maxTemp):  # Determine if heater needs to be turned on/off
    if temp > maxTemp:
        print('heat off')
        return False
    else:
        print('heat on')
        return True

# Define global variables
GLOBAL_maxTemp = float(input('What is your target mash temperature:'))
Temp_actual = float(input('What is the initial water temperature:'))
HeaterON = logic(Temp_actual, GLOBAL_maxTemp)


while (time.time() - start_time) < (end_time * 60):
    print(datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S"))
    Temp_actual = getTemperature(Temp_actual)             # float(input('what is the temperature'))
    HeaterON = logic(Temp_actual, GLOBAL_maxTemp)
    time.sleep(1)
    print()