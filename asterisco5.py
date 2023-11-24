i = 5

while (i >= 1): #contador de linhas
    j = i
    
    while (j >= 1): #contador de asteriscos
        print("*", end="")
        j -= 1
    print()
    i -= 1

i = 0

while (i <= 5): #contador de linhas
    j = -i
            
    while (j <= 0): #contador de asteriscos
        print("*", end="")
        j += 1
    print()
    i += 1

