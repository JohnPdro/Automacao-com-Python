from pathlib import Path

root_dir = Path('dados') # Caminho da pasta raiz
file_paths = root_dir.iterdir() # Itera sobre a pasta raiz pegando e armazenando em uma variavel
# print(list(file_paths)) 

for path in file_paths : # Loop para acessar cada arquivo dentro de file_paths
    
    new_filename = f'new-{path.stem}{path.suffix}' # Altero o nome de cada arquivo adicionando 'new' no inicio
    print(new_filename)
    
    new_filepath = path.with_name(new_filename) # Cria um novo caminho com o memsmo diretorio, mas com outro nome
    path.rename(new_filepath) # Altera o nome do Path para o novo