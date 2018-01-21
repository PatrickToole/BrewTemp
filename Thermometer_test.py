
def getTemperature(temp, HeaterStatus):  # will be gathering temperature from thermometer
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

GLOBAL_maxTemp = 68
GLOBAL_minTemp = 64
Temp_actual = 55
HeaterON = logic(Temp_actual, GLOBAL_maxTemp, GLOBAL_minTemp)
