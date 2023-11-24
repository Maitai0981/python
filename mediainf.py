p = 0
nota = float(input("digite a nota: "))
notat = 0
while (0 <= nota <= 10):
	notat += nota
	p += 1
	nota = float(input("digite a nota: "))
	
if p > 0:
	m = round(notat/p, 2)
	print("Media: {}".format(m))
