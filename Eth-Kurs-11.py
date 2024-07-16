import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
prop = 0.2
cycles = 50
heatstart = np.zeros([24,24], int)

height, width = heatstart.shape
heatstart[:,:] = 20
for i in range(10, 20):
    heatstart[i, 4] = 50

for i in range(4, 21):
    heatstart[20, i] = 60

for i in range(4, 10):
    heatstart[i, 20] = 80
for i in range(4, 21):
    heatstart[4, i] = 99

heatOld = np.copy(heatstart)
heatNew = np.copy(heatOld)
fig = plt.figure()
contour = plt.contour(heatOld)
plt.colorbar(contour)
def animate(z):

    global heatNew
    global heatOld
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            heatNew[i, j] = heatOld[i, j] * (1 - 4 * prop) + prop * (heatOld[i, j - 1] + heatOld[i - 1, j] + heatOld[i + 1, j] + heatOld[i, j + 1])
    heatNew[4, 4:21] = 99
    heatNew[5:10, 20] = 80
    heatNew[11:20, 4] = 50
    heatNew[20, 4:21] = 60
    heatOld = np.copy(heatNew)
    plt.clf()
    plt.title("cycles " + str(z))
    contour = plt.contour(heatNew)
    plt.colorbar(contour)


anim = ani.FuncAnimation(fig, animate, frames = cycles, interval=10, blit=False)
plt.show()
