thislist = []
thislist.append(input("digite uma fruta: "))
thislist.append(input("digite uma fruta: "))
thislist.append(input("digite uma fruta: "))
thislist.append(input("digite uma fruta: "))
thislist.append(input("digite uma fruta: "))

print(                                        )
print(thislist)
print(                                        )

while(True):
    if "maçã" in thislist:
        x = thislist.index("maçã")
        print("maçã esta na posição",x,"da lista")
        print(                                            )
        print("você tem bom gosto ")
        if "limão" in thislist:
            y = thislist.index("limão")
            print(                                            )
            print("limão esta na posição",y,"da lista")
            print(                                            )
            print("você é azedo")
            break
    else:
        print("você tem mau gosto ")
        break
