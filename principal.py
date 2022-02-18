import json
import requests as re

try:
    api = re.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
    api = json.loads(api.text)
except Exception as erro:
    print('Ocorreu um erro com sua requisição. Tente novamente.\n'
          f'Código de erro: {erro}.')
else:
    print(f'Dólar para Real:\n'
          f'[Topo]: 1 USD = {api["USDBRL"]["high"]} BRL.\n'
          f'[Piso]: 1 USD = {api["USDBRL"]["low"]} BRL.')
    print()
    print(f'Euro para Real:\n'
          f'[Topo]: 1 EUR = {api["EURBRL"]["high"]} BRL.\n'
          f'[Piso]: 1 EUR = {api["EURBRL"]["low"]} BRL.')
