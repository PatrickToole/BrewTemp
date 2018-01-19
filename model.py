import random, time, datetime

end_time = .1  # will gather input time, in minutes, from the GUI
start_time = time.time()


def getTemperature():
    randNum = random.randrange(60, 72)
    return randNum

def logic(temp, maxTemp, minTemp):
    if temp > maxTemp:
        return heatOFF()
    elif temp < minTemp:
        return heatON()



def heatON():
     getTemperature() + 1
     print(temp)
def heatOFF():
    getTemperature() - 1
    print(temp)

while (time.time() - start_time) < (end_time * 60):

    print(datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S"))
    temp = getTemperature()             # float(input('what is the temperature'))
    GLOBAL_maxTemp = 68
    GLOBAL_minTemp = 64
    logic(temp, GLOBAL_maxTemp, GLOBAL_minTemp)
    print()


