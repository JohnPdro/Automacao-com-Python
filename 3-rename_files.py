from pathlib import Path

root_dir = Path('files')
# Forma 1
# file_paths = root_dir.interdir() 
# for path in file_paths :
#     print(path)
#     for filepath in path.interdir() :
#         print(filepath)

# Forma 2
file_paths = root_dir.glob('**/*') # Glob é util para quando eu quero pegar os arquivos de uma pasta que pussi várias pastas dentro
for path in file_paths :
    
    if path.is_file() :
        # print(path)
        # print(path.parts) # Transforma o caminho em uma tupla
        parent_folder = path.parts[-2]
        new_filename = f'{parent_folder}-{path.name}'
        print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)