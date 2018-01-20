import time

# represents 1 hour in a minute. to change to 1 hour make end time 60 and sleep timers 15. well i think lol
end_time = 1                            #will gather input time, in minutes, from the GUI
start_time = time.time()

temp = 55
target_temp = 67

temp_delta_heat = (82.165/3600*15)
temp_delta_cool = (15/120)

while (time.time() - start_time) < (end_time * 60):

    while temp < target_temp:
        temp += temp_delta_heat
        time.sleep(0)
        print(temp)
    while temp > target_temp:
        temp -= temp_delta_cool
        time.sleep(0)
        print(temp)




