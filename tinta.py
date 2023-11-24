from math import*
a = int(input("digite a area a ser pintada em m²: "))
if a <= 54:
    print("você presisara comprar 1 lata e isso custara em R$ 80.00")
if a > 54:
    r1 = ceil(a/54)
    r2 = float(r1*80)
    print("vacê presisara comprar {0} lata e isso custara em R$:{1:.2f}".format(r1,r2))
