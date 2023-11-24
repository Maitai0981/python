nota = 1

while (nota > 10):
    nota = float(input("digite sua nota: "))
    
    if nota >= 7:
        print("Aprovado")
        
    elif 4 < nota < 6.9:
        print("Refazer a prova")
    
    else:
        print("Reprovado")
        