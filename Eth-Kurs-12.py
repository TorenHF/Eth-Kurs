import numpy as np
import matplotlib.pyplot as plt
import random as rd

height = int(input("Height? "))
balls = int(input("Amount of balls? "))
bins = np.zeros(height+1, int)

def decision():
    a = rd.randint(0,1)
    return a

for a in range(balls):
    print("Ball", a)
    sum = 0
    for i in range(height):
        direction = decision()
        sum = sum + direction
        print(direction)
    bins[sum]= bins[sum] +1
    print("Ball fell into bin:" )
    print(sum+1)


print("Amount of balls in the bins:")
for i in range(height+1):
    print(bins[i], end=" ")
plt.plot(bins)
plt.show()