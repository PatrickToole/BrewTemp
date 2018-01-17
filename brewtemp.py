temp = getTemperatue()  #float(input('what is the temperature'))
GLOBAL_maxTemp = 70
GLOBAL_minTemp = 63

logic(temp, GLOBAL_maxTemp, GLOBAL_minTemp)

def logicONOFF(temp, maxTemp, minTemp):
      if temp >= maxTemp:
          print('turn heat off')
      elif temp <= minTemp:
          print('turn heat on')
      else:
          print('maintain current heat')
      print temp