from pathlib import Path
from datetime import datetime

root_dir = Path('files')

for path in root_dir.glob('**/*') : # Itera sobre todos os caminhos dentro da pasta e de suas subpastas
    if path.is_file() : # Se for um arquivo faça
        stats = path.stat() # pega os metadados do arquivo
        
        second_created = stats.st_birthtime # Armazena o timestamp da data de criação do arquivo em segundos
        
        date_created = datetime.fromtimestamp(second_created) # Converte o timestamp em um objeto datetime
        
        date_created_str = date_created.strftime('%Y-%m-%d_%H_%M_%S') # Formata o datetime como texto no padrão ano-mês-dia_hora_minuto_segundo
        
        new_filename = f'{date_created_str}-{path.name}' # Cria o novo nome do arquivo
        
        new_filepath = path.with_name(new_filename) # Cria um novo caminho com o mesmo diretório, mas com o novo nome
        
        path.rename(new_filepath) # Atualiza o nome do arquivo

