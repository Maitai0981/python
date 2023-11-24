h = int(input("digite a quantidade de Humanos: ")) # habitantes 
v = int(input("digite a quantidade de Vampiros: ")) # vampiros
while (v <= 0 ):
    v = int(input("digite a quantidade de Vampiros: ")) # vampiros
d = 0 # dias

while (h > 0): # enquanto houver habitantes
    t = v
    h -= t
    v += t
    d += 1 # passou 1 dia 

print(f"a quantidade de dias necessarios para dominação dos vampiros é de {d} dias")