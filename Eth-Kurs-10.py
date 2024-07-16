import numpy as np
import matplotlib.pyplot as plt

prop = 0.4
rodOrg = np.array([40,10,10,10,10,10,10,10,100])
cells = rodOrg.size
rodOld = np.copy(rodOrg)
rodNew = np.zeros(9, int)
cycles = 12

rodNew[0]=rodOld[0]
rodNew[cells-1] = rodOld[cells-1]
def update():
    for a in range(1,cycles):
        for i in range (1,cells-1):
              rodNew[i] = \
                 (1 - 2*prop) * rodOld[i] + \
                 prop * (rodOld[i-1] + rodNew[i+1])
              rodOld[i] = rodNew[i]
        plt.pause(0.3)
        plt.bar(range(cells), rodNew, color='green')



plt.bar(range(cells), rodOld, color='green')
plt.title("Temperature in Rod")
plt.xlabel("Cells")
plt.ylabel("Temperature")
plt.pause(0.3)
update()
plt.show()