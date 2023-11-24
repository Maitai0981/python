

'''for i in range(1,100):
    print(i,end=",")
    
minha_string = "Python"
for letra in minha_string:
    print(letra)
print()
l = [1,2,3]
for letra in l:
    print(letra)'''

n = 0
a = 1
for i in range(1,6):
    p = float(input(f"didite a nota do aluno {i}: "))
    n += p
    
n /= 5
print(f"{n:.2f}")
