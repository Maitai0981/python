r2 = float(input("digite sua autura: "))
print ('responda a pergunta a seguer com "homem" ou "mulher"')
r3 = input("qual seu sexo biologico: ")

while(True):
    if r3 == "mulher":
        m = round(((62.1*r2)-44.7),2)
        print("seu peso ideal é de",m,"Kg")
        break
    if r3 == ("homem"):
        h = round(((72.7*r2)-58),2)
        print("seu peso ideal é de",h,"Kg")
        break
        
