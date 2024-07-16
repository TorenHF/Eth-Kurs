import numpy as np



board = np.zeros((3,3), str)
board[0:3, 0:3] = "-"
boardscores = np.zeros((3,3), int)
multiples = np.zeros(8, int)
win = False
def showBoard():
    print("  C 1 2 3")
    print("R -------")
    for g in range(3):
        print(g+1, end=" | ")
        for h in range(3):
            print(board[g,h], end=" ")
        print("")


def round():
    print("Player x:")
    a = int(input("Row? "))
    b = int(input("Collum? "))
    board[a-1,b-1] = "x"
    boardscores[a-1,b-1] = 1

    print("Player o:")
    c = int(input("Row? "))
    d = int(input("Collum? "))
    board[c-1,d-1] = "o"
    boardscores[c-1, d-1] = 2
    showBoard()

def multiply(): #This function is supposed to help me find out when a player has won
    for i in range(3):
        multiples[i] = boardscores[i,0]*boardscores[i,1]*boardscores[i,2]
    for j in range(3):
        multiples[j+3] = boardscores[0, j]* boardscores[1, j]* boardscores[2, j]
    multiples[6] = boardscores[0,0]*boardscores[1,1]*boardscores[2,2]
    multiples[7] = boardscores[0,2]*boardscores[1,1]*boardscores[2,0]
    return multiples
while win == False:
    round()
    multiply()
    for a in multiples:
        if multiples[a] == 1:
            win = True
            showBoard()
            print("Player x wins!")
            break

        if multiples[a] == 8:
            win = True
            showBoard()
            print("Player o wins!")
