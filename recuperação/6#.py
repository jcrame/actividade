km = int(input('digite a velocidade:'))

def classificar_velocidade():
    if km >= 0 and km <= 40:
        print ("Lento")
    elif km >= 41 and km <= 80:
        print ("Normal")
    elif km >= 81 and km <= 120:
        print ("Rápido")
    else:
        print ("Muito rápido")

classificar_velocidade()
