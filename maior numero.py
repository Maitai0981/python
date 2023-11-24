numero1 = float(input("digite um numero: "))
numero2 = float(input("digite um numero: "))
if numero1 > numero2:
    print ("o numero {0} é mior que o numero {1}".format(numero1,numero2))
if numero2 > numero1:
    print ("o numero {0} é mior que o numero {1}".format(numero2,numero1))
if numero2 == numero1:
    print ("os numeros {1} e {0} são iguais".format(numero2,numero1))