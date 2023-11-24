from pessoal import function

horas = float(input("quantas hora voce trabalha\n"))
salario = float(input("quanto voce ganha por hora\n"))

total1 = horas * salario
if total1 < 900:
    ir = 0
    inss = 10/100
    fgts = 11/100
    desconto = ((total1*inss)+(total1* fgts)+(total1*ir))
    sdesconto = total1 - desconto


if total1 > 900 and total1 < 1500:
    ir = 5/100
    inss = 10/100
    fgts = 11/100
    desconto = ((total1*inss)+(total1* fgts)+(total1*ir))
    sdesconto = total1 - desconto

if total1 > 1500 and total1 < 2500:
    ir = 10/100
    inss = 10/100
    fgts = 11/100
    desconto = ((total1*inss)+(total1* fgts)+(total1*ir))
    sdesconto = total1 - desconto
    
if total1 > 2500:
    ir = 20/100
    inss = 10/100
    fgts = 11/100
    desconto = ((total1*inss)+(total1* fgts)+(total1*ir))
    sdesconto = total1 - desconto

print(f"seu salario sem desconto é de R$:{total1:.2f}")
print(f"inposto de renda é de R$:{ir:.2f}")
print(f"o desconto do INSS é de R$:{inss:.2f}")
print(f"o descont do FGTS é de R$:{fgts:.2f}")
print(f"o desconto total é de R$:{desconto:.2f}")
print(f"o salario com o desconto aplicado é de {sdesconto:.2f}")