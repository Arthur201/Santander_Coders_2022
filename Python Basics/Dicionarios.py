
from this import d


dados = {
    'cidade:' :'Uberlândia',
    'estado:': 'Minas Gerais',
    'população_Milhões:': 0.8,
}

print(dados) # retorna o dicionário completo
print(dados.keys) # retorna uma lista com todas as chaves do dicionário
print(dados.values) # retorna uma lista de todos os valores do dicionário
print(dados.items) # retorna uma LISTA de TUPLAS com todos os pares (chave,valor)

dados.get('cidade') # acessa o valor da chave dada, porém, caso não exista tal chave,  retorna um valor nulo

dados['cidade:'] # acessa o valor da chave dada, porém, caso não exista tal chave, retorna um erro