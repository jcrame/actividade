import requests

url = 'https://pokeapi.co/api/v2/pokemon/pikachu'

resposta = requests.get(url) 

print ('status:', resposta.status_code)

dados = resposta.json()

print("nome: ", dados['name'])
print("número: ", dados['id'])
print("altura: ", dados['height'])
print("peso: ", dados['weight'])