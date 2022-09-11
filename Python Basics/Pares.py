# Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n = 0
contador = 0
for n in range(20):
        if (numeros[n] % 2 == 0):
            contador = contador+1

print("Nesta lista há: ", contador, " números pares.")
