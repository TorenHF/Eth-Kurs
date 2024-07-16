capacityR = 50
capacityK = 10
repRateR= 1.5
repRateK = 1.1
wFactor= 5
l = 20

rabbits = [0 for x in range(0, l)]
kangos = [0 for x in range(0,l)]
time = [0 for x in range(0, l)]
totalAnimals = [0 for x in range(0,l)]

print("t", "r", "k", "a")
for i in range(0,l):
    rabbits[i] = rabbits[i-1] + repRateR*rabbits[i-1]*(capacityR-rabbits[i-1]-kangos[i-1]*wFactor)/capacityR
    kangos[i] = kangos[i-1] + repRateK*kangos[i-1]*(capacityK-kangos[i-1]-rabbits[i-1]/wFactor)/capacityK
    totalAnimals[i]= kangos[i]+rabbits[i]
    time[i] = time[i-1] + 1
    rabbits[0] = 2
    time[0]= 0
    kangos[0]= 5
    print(time[i], round(rabbits[i]), round(kangos[i]), round(totalAnimals[i]))