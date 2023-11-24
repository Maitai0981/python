while(True):
    mb = float(input("digite o tamanho do arquivo em MB: "))
    ms = float(input("digite a velocidade de internet em Mbps: "))
    t = (mb/(ms/8))/60
    print(f"O tempo aproximado de download é {t:.2f} minutos")
    print(30*" ")
