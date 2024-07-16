# Halooooo
k = (input("Team 1: "))
s = (input("Team 2: "))


print("First leg:")
print(k, "against" , s)
print(k[0],k[1],k[2], ":", s[0], s[1],s[2])

s_temp = s
s = k
k = s_temp

print("Return leg:")
print(k, "against" , s)
print(k[0],k[1],k[2], ":", s[0], s[1],s[2])

i = 1
while i < 6:
  print(i)
  i += 1


