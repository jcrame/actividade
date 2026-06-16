filmes = []

for i in range(5):
    filme = input(f"Digite o {i+1 } filme favorito: ")
    filmes.append(filme)

print("\nFilmes cadastrados:")

for numero, filme in enumerate(filmes, 1):
    print(f"{numero}. {filme}")

print(f"\nQuantidade de filmes cadastrados: {len(filmes)}")
