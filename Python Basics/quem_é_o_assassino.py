from ast import While
from tkinter import E
# Questionário para identificar o assassino.Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos, necessitando outras investigações. Valores iguais ou abaixo de 1 são liberados.



print("Questionário suspeito de assassinato: ")

a = input("Mora Perto da Vítima? ")
b = input("Já trabalhou com a vítima? ")
c = input("Telefonou para a vítima? ")
d = input("Esteve no local do crime? ")
e = input("Devia para a vítima? ")

respostas = [a,b,c,d,e]
contador = 0
n = 0

for n in range(5):
    if (respostas[n] == "sim"):
        contador = contador+1
n = n+1
    
if contador == 5:
    print("Você é o assassino!")
elif 3 <= contador <= 4:
    print("Vocês são cúmplices!")
elif contador == 2:
    print("Você é suspeito.")
else:
    print("Você está liberado!")


