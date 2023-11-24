from math import*
a = float(input("Digite o tamanho da área em metros quadrados: "))

r1 = ceil(a / 108)
r2 = (r1*80)
print("vacê presisara comprar {0} galões e isso custara em R$:{1:.2f}".format(r1,r2))

r3 = ceil(a/(3.6*6))
r4 = (r3*25)
print("você presisara comprar {0} lata e isso custara em R$:{1:.2f}".format(r3,r4))

q_latas1 = ceil(a//108)
q_galoes2 = ceil(((a % 108) /(3.6*6)))
preco_misto = ((q_latas1*80) + (q_galoes2*25))
print(f"você presisara comprar {q_latas1:.0f} latas e {q_galoes2:.0f} galões isso custara em R$:{preco_misto:.2f}")