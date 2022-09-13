import requests as r

url = 'https://api.covid19api.com/dayone/country/brazil'

resp = r.get(url)

dados = resp.json()

dados[0]

dados_finais = []
for obs in dados:
    dados_finais.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

dados_finais.insert(0, ['Confirmados', 'Óbitos', 'Recuperados', 'Ativos', 'Data'])

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1,len(dados_finais)):
    dados_finais[i][DATA] = dados_finais[i][DATA][:10]
    


import datetime as dt
import csv

with open('dados-covid-brasil.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(dados_finais)

for i in range(1,len(dados_finais)):
    dados_finais[i][DATA] = dt.datetime.strptime(dados_finais[i][DATA],'%Y-%m-%d')

print(dados_finais)




