import time
import datetime
from testmail import notify
#from mash_working import logic

end_time = float(input('How long would you like to heat for(minutes)?'))
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


def strikelogic(temp, maxTemp):  # Determine if heater needs to be turned on/off
    if temp > (maxTemp-1):
        print('heat off')
        #notify()
        return False
    else:
        print('heat on')
        return True

def maintenencelogic(temp, maxTemp):  # Determine if heater needs to be turned on/off
    if temp > maxTemp:
        print('heat off')
        return False
    else:
        print('heat on')
        return True

# Define global variables
GLOBAL_maxTemp = float(input('What is your target strike temperature:'))
Temp_actual = float(input('What is the initial water temperature:'))
HeaterON = strikelogic(Temp_actual, GLOBAL_maxTemp)
target_time = datetime.datetime(input('yyyy, dd, mm, hh'))

while (time.time() - start_time) < (end_time * 60):
    if Temp_actual < (GLOBAL_maxTemp-1):
        print(datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S"))
        Temp_actual = getTemperature(Temp_actual)  # float(input('what is the temperature'))
        HeaterON = strikelogic(Temp_actual, GLOBAL_maxTemp)
        time.sleep(.25)
        print()

    elif Temp_actual >= (GLOBAL_maxTemp-1) and (time.time() - start_time) < (end_time * 60):
        print(datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S"))
        Temp_actual = getTemperature(Temp_actual)  # float(input('what is the temperature'))
        HeaterON = maintenencelogic(Temp_actual, GLOBAL_maxTemp)
        time.sleep(.25)
        print()