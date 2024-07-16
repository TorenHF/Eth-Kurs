
counter=  0
mark = input("Mark: ")
a = mark
print("enter 0 to calculate average")
while a != 0:
    a = int(input("next Mark: "))
    mark = int(mark) + int(a)
    counter = int(counter) + 1
    print("enter 0 to calculate average")

average = mark / counter
print("Average:", average)