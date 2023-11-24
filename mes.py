import time 

nmes = int(input("digite o numero que indique um mês do ano "))
mes = ["janeiro", "fevereiro","março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
m = nmes - 1
if m > 11:
    m = 11
if m < 0:
    m = 0
print(f"estamos no mes {mes[m]}")

for i in (range(20)):
    time.sleep(1)