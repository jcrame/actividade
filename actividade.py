nome = input("coloque teu nome: ")
idade = input("adicione tua idade: ")
cidade = input("de qual cidade é vc: ")

print(f"mi nombre es {nome} y tengo {idade} años y soy de {cidade}")




print ("pode colocar suas notas")

nota1 = float(input("nota #1: "))
nota2 = float(input("nota #2: "))

suma = nota1 + nota2
print (f'nota1 + nota2 = {suma}')

subtracao = nota1 - nota2
print (f'nota1 - nota2 = {subtracao}')

multiplicacao = nota1*nota2
print (f'nota1 x nota2 = {multiplicacao}')

divisao = nota1 / nota2
print (f'nota1 / nota2 = {divisao}')




numero = int(input("coloque numero: "))

for i in range(1,11):
    result = i*numero
    print(f'{i} x {numero} = {result}' ) 



numero_secreto = 99

palpite = None

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número secreto: "))

    if palpite < numero_secreto:
        print("O palpite é menor do número secreto.")
    elif palpite > numero_secreto:
        print("O palpite é maior do número secreto.")
    else:
        print("Parabéns nossa! Você acertou o número secreto!")
        break

    
