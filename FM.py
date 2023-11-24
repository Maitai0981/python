g = input('digite o seu sexo ')
f = ["f","F","feminino","Feminino","FEMININO"]
m = ["m","M","masculino","Masculino","MASCULINO"]
x = ["x","X","invalido","Invalido","INVALIDO"]
if g in f:
    print('seu sexo é feminino')
if g in m:
    print('seu sexo é masculino')
if g in x:
    print('seu sexo é invalido')