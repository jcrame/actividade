total = float(input("Qual é o total da conta? R$ "))
percentual = float(input("Qual é o percentual da gorjeta? %"))

def calcular_gorjeta(total, percentual):
    gorjeta = total * (percentual / 100)
    total_pagar = total + gorjeta
    return gorjeta, total_pagar

gorjeta, total_pagar = calcular_gorjeta(total, percentual)

print(f"Gorjeta: R${gorjeta}")
print(f"Total a pagar: R${total_pagar}")
