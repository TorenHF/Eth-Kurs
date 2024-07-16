
a = False
b = int(5)


while a==False and b > 0:
    print("please enter PIN")
    x = int(input("digit 1: "))
    y = int(input("digit 2: "))
    z = int(input("digit 3: "))

    if x ==0 and y ==0 and z == 7:
        a=True
        print("success")
    else:
        print("try again")
        b= b -1
        print("Attempts left:", b)
        if b == 0:
            b= True
            print("LOCKED")








