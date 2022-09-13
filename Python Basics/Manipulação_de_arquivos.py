import csv

usuario = input("O que você deseja?\n 1 - Arquivo todo\n 2 - Arquivo linha a linha\n 3 - Arquivo clone\n")

if usuario == "1":
#Abrindo o arquivo todo
    with open('Arquivo.csv', 'r', encoding='utf-8') as arquivo_csv:
        leitor = arquivo_csv.read()
        print(leitor)

#Abrindo o arquivo linha por linha
elif usuario == "2":

    with open('Arquivo.csv', 'r') as arquivoCSV:
        linha= arquivoCSV.readline()
        for linha in arquivoCSV:
            print(linha)


#Clonando o arquivo
import shutil
arquivo_csv = 'Arquivo.csv'
arquivoClone = 'Arquivo_Clone.csv'

shutil.copyfile(arquivo_csv, arquivoClone)
if usuario == "3":
    with open('Arquivo_Clone.csv', 'r') as arquivoClone:
        ler = arquivoClone.read()
        print(ler)

        
