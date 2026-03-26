import PyPDF2 as pdf
from PyPDF2 import PdfReader

# 1 - Versão e Métodos dessa Biblioteca
print(pdf.__version__)
print(dir(pdf))

# 2 - Importando o arquivo PDF
file = open('files/teste2.pdf', 'rb')
reader = PdfReader(file)
print(reader)
print(reader.metadata)
info = reader.metadata # Armazena os metadados do PDF

# 3 - Extraindo algumas informações
print(info.title) # Pega o titulo do PDF
print(info.author) # Pego o author do PDF
print(info.creator) # Pega o criador/gerador do PDF
print(info.subject) # 
print(len(reader.pages)) # Pega a quantidade de paginas do documento
print(reader.pages[0].extract_text()) # Pega o texto da página especificada no caso a primeira
print(reader.pages[1].extract_text()) # Pega o texto da página especificada no caso a segunda
