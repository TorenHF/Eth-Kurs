import numpy as np
import matplotlib.pyplot as plt
board = np.array([[3,4,8], [7,0,5],[2,1,6]], int)
store = np.zeros((1,1), int)
n=int(input("how many moves? "))
def boardPrint():
    print("C 1 2 3")
    print("R -----")
    for i in range(3):
        print(" ", end=" ")
        for q in range(3):
            print( board[i, q], end=" ")
        print()


def move():
    print("piece to move:")
    a = int(input("x-label: "))
    b = int(input("y-label: "))
    print("new squarw:")
    c = int(input("x-label: "))
    d = int(input("y-label: "))
    store[0,0] = board[c, d]
    board[c, d] = board[a, b]
    board[a,b] = store[0,0]
boardPrint()
for i in range(n):
    move()
boardPrint()
