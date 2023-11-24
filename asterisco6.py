i = 5
e = 0
while (i >= 1): #contador de linhas
    if e == 0:
        print("*"*i+"*"*i, end="")
        e += 2
    elif e > 1:
        print("*"*i+" "*e+"*"*i, end="")
        e += 2
    print()
    i -= 1

i = 1
e = 8

while (i <= 5): #contador de linhas
    if e == 0:
        print("*"*i+"*"*i, end="")
        e -= 2
    elif e > 1:
        print("*"*i+" "*e+"*"*i, end="")
        e -= 2
    print()
    i += 1

n = 1

