import numpy as np
a = int(input("how many players? "))
b = int(input("how many rounds? "))
scores = np.zeros((a, b), int)
results = np.zeros((a, 1), int)

for i in range(0, b):
    print("round ", i+1)
    for x in range(0, a):
        scores[x,i] = int(input("Player: " ))

for n in range(0, a):
    for m in range(0, b):
        if m == 0:
            results[n] = scores[n, m]
        else:
            results[n] += scores[n, m]

for k in range(0, a):
    print()
    print("player", k+1)
    for l in range(0, b):
        print(scores[k, l], end=" ")
print()
print("Results:")
for p in range(a):
    print(results[p], end=" ")


