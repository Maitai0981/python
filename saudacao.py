def saudacao():
    print("olá! Bem-vindo à função de saudação")
    
def soma(a,b):
    resultado = a + b
    return resultado

def sub(a,b):
    resultado = a - b
    return resultado

def mult(a,b):
    resultado = a * b
    return resultado

def divi(a,b):
    resultado = a / b
    return resultado

def poten(a,b):
    resultado = a ** b
    return resultado

def raiz(a,b):
    resultado = a ** (1/b)
    return resultado

def ip_e(*args):
    for i in args:
        print(i)

def dp(nome = "", idade = "", cidade = ""):
    print(f"{nome} tem {idade} anos e mora em {cidade}.")
    


#dp("Maria",30,"são paulo")

#ip_e(1,2,3)

'''op = [soma(5,3),sub(5,3),mult(5,3),divi(5,3),poten(5,3),raiz(5,3)]

for elment in op:
    print(elment)'''
    
    
#resultado_soma = soma(5, 3)
#print(f"resultado da soma: {resultado_soma}")    

#saudacao()


