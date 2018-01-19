import random
import time
import datetime

end_time = 1                            #will gather input time, in minutes, from the GUI
start_time = time.time()

def getTemperature():                    # will be gathering temperature from thermometer
    randNum = random.uniform(60.00, 72.00)
    print(round(randNum,2), 'C')
    print(round((randNum * 1.8 + 32), 2), 'F')
    return randNum


def logic(temp, maxTemp, minTemp):
    if temp >= maxTemp:
        print('turn heat off')
    elif temp <= minTemp:
        print('turn heat on')
    else:
        print('maintain current heat')


while (time.time() - start_time) < (end_time * 60):

    print(datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S"))
    temp = getTemperature()             # float(input('what is the temperature'))
    GLOBAL_maxTemp = 68
    GLOBAL_minTemp = 64
    logic(temp, GLOBAL_maxTemp, GLOBAL_minTemp)
    time.sleep(15)
    print()

