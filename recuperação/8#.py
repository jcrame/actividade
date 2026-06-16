# lista de produtos
estoque = []

def ver_estoque():    
    if len(estoque) == 0:        
        print('Estoque vazio.')    
    else:        
        for i, produto in enumerate(estoque, 1):            
            print(f'{i}. {produto}') 


def adicionar():
    
     produto = input(f"Digite o produto ")
     estoque.append(produto)
     print(f"{produto} foi cadastrado:")

pass 


def retirar():
     produto = input("Digite o nome do produto para retirar: ")
     if produto in estoque:
        estoque.remove(produto)
        print(f"{produto} foi retirado do estoque.")
     else:
        print("Produto não encontrado no estoque.")



pass

opcao = ""

while True: 
    print('\n1- Adicionar  2- Retirar  3- Ver estoque  4- Sair') 
    opcao = input('Escolha: ')
    if opcao == "1":
        adicionar()
    elif opcao == "2":
        retirar()
    elif opcao == "3":
        ver_estoque()
    elif opcao == "4":
        print("Programa encerrado.")
        break    
    else: 
        print("Opção inválida!")
