total = 0

while True:
    preco = float(input("Digite o preço do produto (0 para encerrar): R$ "))

    if preco == 0:
        break

    total += preco

print(f"Total da compra: R$ {total}")
