import random, time, datetime

end_time = .1  # will gather input time, in minutes, from the GUI
start_time = time.time()


def getTemperature():
    randNum = random.randrange(60, 72)
    return randNum

def logic(temp, maxTemp, minTemp):
    if temp >= maxTemp:
        return (temp - 1)
    elif temp <= minTemp:
        return (temp + 1)


def heatON():
     getTemperature() + 1

def heatOFF():
    getTemperature() - 1


temp = getTemperature()             # float(input('what is the temperature'))

while (time.time() - start_time) < (end_time * 60):

    print(datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S"))
    GLOBAL_maxTemp = 66
    GLOBAL_minTemp = 66
    logic(temp, GLOBAL_maxTemp, GLOBAL_minTemp)
    print(logic(temp,GLOBAL_maxTemp, GLOBAL_minTemp))


