from dataclasses import dataclass
import requests as r
import datetime as dt
import csv



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
    
with open('dados-covid-brasil.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(dados_finais)

for i in range(1,len(dados_finais)):
    dados_finais[i][DATA] = dt.datetime.strptime(dados_finais[i][DATA],'%Y-%m-%d')

#Criação do gráfico

def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
            
                'label': labels[i],
                'data': y[i]
            })
                   

        return datasets
    else:
        return[{
            'label': labels[0],
            'data': y
        }]

def set_title(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title': title,
        'display': display
    }

def create_chart(x, y, labels, kind='bar', title=''):

    datasets = get_datasets(y, labels)
    options = set_title(title)

    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets':datasets
        },
        'options':options
    }

    return chart

def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content

def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)

from PIL import Image
from IPython.display import display

def display_image(path):
    img_pil =Image.open(path)
    display(img_pil)

y_data_1 = []
for obs in dados_finais[1::10]:
    y_data_1.append(obs[CONFIRMADOS])
y_data_2 = []
for obs in dados_finais[1::10]:
    y_data_2.append(obs[RECUPERADOS])

labels = ['Confirmados','Recuperados']

x = []
for obs in dados_finais[1::10]:    
    x.append((obs[DATA]).strftime('%d/%m/%Y'))

chart = create_chart(x, [y_data_1,y_data_2], labels, title='Gráfico de Confirmados VS Recuperados')
chart_content = get_api_chart(chart)
save_image('meu-primeiro-gráfico.png',chart_content)
display_image('meu-primeiro-gráfico.png')
