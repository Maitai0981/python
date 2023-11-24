def ex(n):
    print(n * " ")


v1 = float(input("digite um numero:\n"))
ex(30)

v2 = float(input("digite um numero:\n"))
ex(30)

v3 = float(input("digite um numero:\n"))
ex(30)
if v3 > v2 or v3 > v1:
    print(f"o maior numero é {v3}")

elif v1 > v2 or v1 > v3:
    print(f"o maior numero é {v1}")

else:
    print(f"o maior numero é {v2}")
ex(30)
if v3 < v2 or v3 < v1:
    print(f"o maior numero é {v3}")

elif v1 < v2 or v1 < v3:
    print(f"o maior numero é {v1}")

else:
    print(f"o maior numero é {v2}")