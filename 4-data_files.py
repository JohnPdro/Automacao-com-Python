from pathlib import Path
from datetime import datetime

path = Path('files', 'dados2', 'teste.txt')

stats = path.stat() # Mostra todos os metadados(informações) do arquivo

second_created = stats.st_birthtime # Pega o metadado de tempo que referencia quando o arquivo foi criado 'st_ctime'
print(second_created)

date_created = datetime.fromtimestamp(second_created) # Utilizando a bibilioteca datetime.fromtimestamp formata o metadado para um formato de data padrão
print(date_created)

date_created_str = date_created.strftime('%Y-%m-%d_%H_%M_%S') # Formata a exibição da data
print(date_created_str)

print(path.stat())
