import matplotlib.pyplot as plt
import pylab as pl

dose = int(input("dose? "))
frequency = int(input("frequency? "))
degRate = 0.1
counter= [0 for x in range(50)]
time = [0 for x in range(50)]
concentrat = [0 for x in range(50)]
concentrat[0] = dose
print("Counter | Time | Concentration")
for i in range (1, 50):
    if counter[i-1] == frequency:
        counter[i] = 0
    else :
        counter[i] = counter[i - 1] + 1

    if counter[i] == 0:
        time[i] = time[i-1] + 0.001
        concentrat[i] = concentrat[i-1] + dose
    else:
        time[i] = time[i - 1] + 1
        concentrat[i]= concentrat[i-1] * (1-degRate)
    time[i] = round(time[i], 3)
    concentrat[i] = round(concentrat[i], 3)


    print(counter[i]," | ", time[i]," | ", concentrat[i] )
plt.plot(time, concentrat)
plt.title("meds")
pl.xlabel("time")
pl.ylabel("concentration")
plt.show()


