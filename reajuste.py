salario = float(input("qual o seu salario:\n"))

if salario < 280:
    percentual = (20/100)
    reajuste = salario + (salario*percentual)
    almento = reajuste - salario

elif salario > 280 and salario < 700:
    percentual = (15/100)
    reajuste = salario + (salario*percentual)
    almento = reajuste - salario

elif salario > 700 and salario < 1500:
    percentual = (10/100)
    reajuste = salario + (salario*percentual)
    almento = reajuste - salario

elif salario > 1500:
    percentual = (5/100)
    reajuste = salario + (salario*percentual)
    almento = reajuste - salario

print(f"o salario inicial é de {salario:.2f}")
print(f"o percentual de reajuste foi de {percentual*100}%")
print(f"o salario aumentou {almento:.2f}")
print(f"o salario de reajuste é de {reajuste:.2f}")
