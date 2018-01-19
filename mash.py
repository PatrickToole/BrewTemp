import random
import time
import datetime

end_time = 1 #will gather input time, in minutes, from the GUI
start_time = time.time()

while (time.time() - start_time) < (end_time * 60):

    print() #this is for spacing the output to more readable blocks

    def getTemperature():
        randNum = random.randrange(60, 72)
        print(randNum, 'C')
        print(randNum * 1.8 + 32, 'F')
        return randNum

    def logic(temp, maxTemp, minTemp):
        if temp >= maxTemp:
            print('turn heat off')
        elif temp <= minTemp:
            print('turn heat on')
        else:
            print('maintain current heat')

    time.sleep(15)

    temp = getTemperature()  # float(input('what is the temperature'))
    GLOBAL_maxTemp = 68
    GLOBAL_minTemp = 64
    logic(temp, GLOBAL_maxTemp, GLOBAL_minTemp)

    print(datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S"))



