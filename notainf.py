p = 0
nota = 1
while (0 <= nota <= 10):
	nota = float(input("digite a nota: "))
	if 5 <= nota <= 10:
		p = p + 1

print("Passaram: {}".format(p))
