h = int(input("digite a quantidade de Humanos: ")) # habitantes
v = int(input("digite a quantidade de Vampiros: ")) # vampiros
while (v <= 0 ):
    v = int(input("digite a quantidade de Vampiros: ")) # vampiros
m = int(input("digite quantos vampiros os caçadores matam por dia: ")) # morte da vampiros
d = 0

while (h > 0 and v > 0): # enquanto houver habitantes
    t = v
    h -= t
    v += t
    v -= m
    d += 1

if v > 0:
    print("VAMPIRIZADA 🧛🏼‍♂️") 

if h > 0:
    print("LIVRE ") 
   
print(f"{d} dias")