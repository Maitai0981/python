pp = float(input("digite o peso do peixe: "))
if pp <= 50:
    print("você não pagara multa")
if pp > 50:
    ex = (pp - 50.00)
    m = (ex*4.00)
    print('voce deve pagar: R$',m)
