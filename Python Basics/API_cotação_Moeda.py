import requests

url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)

print(req.status_code)

dados = req.json()

vlr_reais = float(input("Digite o valor, em R$, a ser convertido:\n"))

cotacaoU = dados['rates']['BRL']
print(f'R${vlr_reais} em dólar vale: US$ {(vlr_reais/cotacaoU):.2f}')


