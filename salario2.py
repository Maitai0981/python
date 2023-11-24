s1 = float(input("quanto você ganha por hora: "))
s2 = float(input("quantas horas você trabalha no mês: "))
s3 = round(s1*s2, 2)
ir = (11*s3)/100
inss = (8*s3)/100
si = (5*s3)/100
d = ir+inss+si
sl = s3 - d
print("Salário Bruto : R$",s3)
print("IR (11%) : R$",ir)
print("INSS (8%) : R$",inss)
print("Sindicato ( 5%) : R$",si)
print("Você pagara ao gaverno: R$",d)
print("Salário Liquido : R$",sl)
