estoque = []                         # lista de produtos
def ver_estoque():    
    if len(estoque) == 0:        
        print('Estoque vazio.')    
    else:        
        for i, produto in enumerate(estoque, 1):            
            print(f'{i}. {produto}') 

adicionar = []

def adicionar():
    
     produto = input(f"Digite o produto ")
     produto.append(produto)
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


while True: print('\n1 - Adicionar  2 - Retirar  3 - Ver estoque  4 - Sair') 
    opcao = input('Escolha: ') # complete com if/elif para chamar cada funcao
