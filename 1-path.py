from pathlib import Path

p1 = Path('dados', 'teste.txt') # Cria um caminho com base nas informçaões passadas, neste caso ficará 'dados\teste.txt'
print(p1) # 'dados\teste.txt'
print(type(p1)) # Mostra o tipo da variavel p1 que no caso é um classe Pathlib
print(p1.name) # Mostra o nome do arquivo completo com tipo
print(p1.stem) # Mostra apenas o nome do arquivo
print(p1.suffix) # Mostra apenas o tipo do arquivo
print(p1.exists()) # Verifica se o arquivo existe 

if p1.exists() : # Verifica se o arquivo existe 
    with open(p1, 'r', encoding='utf-8') as file : # Inicia o processo de abertura do arquivo para leitura
        print(file.read()) # Faz a leitura

p2 = Path('dados')
print(list(p2.iterdir())) # Fica iterando dentro da pasta alvo e exibindo os arquivos dentro da pasta