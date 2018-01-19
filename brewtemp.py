import random
import time
def main():
    t_end = time.time() + 60

    def getTemperature():
        randNum = random.randrange(60,72)
        print(randNum,'C', randNum*1.8+32,'F' )
        return randNum


    def logic(temp, maxTemp, minTemp):
        if temp >= maxTemp:
            print('turn heat off')
        elif temp <= minTemp:
            print('turn heat on')
        else:
            print('maintain current heat')
    if t_end > time.time():
        main()
    else:
        exit()

    temp = getTemperature()  #float(input('what is the temperature'))
    GLOBAL_maxTemp = 68
    GLOBAL_minTemp = 64
    logic(temp, GLOBAL_maxTemp, GLOBAL_minTemp)

main()