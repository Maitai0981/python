print("""indiqua tabuada com
 S: soma
 B: Subtracao
 M: Multiplicacao
 D: Divisao""") 
t = input("digite qual tabuada: ")
n = int(input("digite um numero inteiro"))
num = 1
while (num <= 10):
	if t.upper() == 'S':
		c = n + num
		num += 1

	if t.upper() == 'B':
		c = n - num
		num += 1

	if t.upper() == 'M':
		c = n * num
		num += 1

	if t.upper() == 'D':
		c = n / num
		num += 1
	print(c)


