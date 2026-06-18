import requests

nome = input("qual o pokemon?").strip().strip()
qtpokemon = input("quantos pokemons que ver")
infopokemonURL = "https://pokeapi.co/api/v2/pokemon/" + nome 
quantidadepokemonURL = "https://pokeapi.co/api/v2/pokemon?limit="+qtpokemon

resposta = requests.get(infopokemonURL) 
respostaqt = requests.get(quantidadepokemonURL) 
print ('status:', resposta.status_code)


dados = resposta.json()
dadosqt = respostaqt.json()

print('--- Imformações gerais ---')
print("nome: ", dados['name'])
print("número: ", dados['id'])
print("altura: ", dados['height'])
print("peso: ", dados['weight'])

print ('--- Habilidades ---')
for item in dados ['types']:
    print('-', item['type']['name'])

print ('--- stats ---')
for stat in dados['stats']:
    print('-', stat['stat']['name'], ':', stat["base_stat"] )


print("pokemon disponiveis")
for name in dadosqt['results']:
    print('-',name['name'])
