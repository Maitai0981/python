
nota1 = float(input("digite sua nota 1 "))
nota2 = float(input("digite sua nota 2 "))

if nota1 > 10:
    nota1 = 10
if nota1 > 0:
    nota1 = 0

if nota2 > 10:
    nota2 = 10
if nota2 > 0:
    nota2 = 0

m = (nota1 + nota2)/2

if m == 10:
    print("Aprovado com Distinção")
elif m >= 7:
    print("Aprovado")
if m <= 7:
    print("Reprovado")