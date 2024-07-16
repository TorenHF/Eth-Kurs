import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as rd
# array for storing the population
population = np.empty((100, 100))

# number of days that shall be simulated
days = int(input("Duration of the simulation? "))
amountSick = int(input("How many sick people at the start? "))
sickProb = int(input("Infection rate (%)? "))
numb = np.zeros((days, 1))
# necessary for the graphical representation
fig = plt.figure()
cmap = plt.get_cmap('brg', 8)
mat = plt.imshow(population, cmap=cmap, interpolation='nearest', animated=True)
cax = plt.colorbar(mat, ticks=np.arange(0, 8))
plt.clim(0, 8)
plt.grid(True)
counter = np.zeros((days, 1), int)
# end of the graphic options
def update(d):
    mat.set_data(population)
    plt.title("Day: " + str(d))
    count(d)

def count(f):
    for u in range(100):
        for g in range(100):
            if 8 > population[u,g] > 0:
                counter[f] = counter[f] +1
    return counter
def rando():
    randomnumber = rd.randint(0, 99)
    return randomnumber
def infectious(x,y):
    if 7 > population[x,y] > 0 :
        contagious = True
    else:
        contagious = False
    return contagious

def infection(x,y):
    if population[x, y] == 0 :
        if infectious(x-1,y) == True or infectious(x-1,y-1) == True  or infectious(x,y-1)== True or infectious(x+1,y+1)== True or infectious(x+1,y)== True or infectious(x,y+1)== True:
            if rando() < sickProb-1:
                population[x, y] = 1
    elif population[x,y]< 8 :
         population[x,y] = population[x,y] + 1
# initial state of the simulation
def setup():
    for i, j in np.ndindex(population.shape):
        population[i, j] = 0
    for k in range(amountSick):
        o = rd.randint(0, 99)
        p = rd.randint(0, 99)
        population[o, p] = 1
        return population[o, p]
    update(0)

    return mat,

# updating the animation
def animate(t):
    for i, j in np.ndindex(population.shape):
        if 0< i< 99 and 0< j< 99:
            # calculation of the infection
            infection(i, j)

    # updating the representation with the new values
    update(t)
    return mat,
#for h in range(days):
    #if numb == 0:
        #numb = 0
    #else:
        #numb[h, 1] += numb[h-1, 1]+1

# animating the representation
ani = animation.FuncAnimation(fig, animate, range(1, days), repeat=False, interval=300, blit=False, init_func=setup)
plt.plot(numb, counter)
plt.show()
