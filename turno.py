def ex(n):
    print(n * " ")

turno = input("didite o turno atual\n")
turno = turno.upper()
m = ["M","MATUTINO"]
v = ["V","VESPERTINO"]
n = ["N","NOTURNO"]
ex(30)

if turno in m:
    print("Bom dia")
elif turno in v:
    print("Bom tarde")
elif turno in n:
    print("Bom noite")
elif turno not in m or n or v:
    print("Dado invalido!")
