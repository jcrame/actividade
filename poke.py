import requests

nome = input("qual o pokemon?").strip().strip()

url = "https://pokeapi.co/api/v2/pokemon/" + nome 

resposta = requests.get(url) 

print ('status:', resposta.status_code)

dados = resposta.json()

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