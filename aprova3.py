nota1 = float(input("digite sua nota 1 "))
nota2 = float(input("digite sua nota 2 "))
nota3 = float(input("digite sua nota 3 "))

if nota1 > 10:
    nota1 = 10
if nota1 > 0:
    nota1 = 0

if nota2 > 10:
    nota2 = 10
if nota2 > 0:
    nota2 = 0

if nota3 > 10:
    nota3 = 10
if nota3 > 0:
    nota3 = 0

m = (nota1 + nota2 + nota3)/3

if m == 10:
    print("Aprovado com Distinção")
elif m >= 7:
    print("Aprovado")
if m <= 7:
    print("Reprovado")