import os
from shutil import (
move, 

) 
from extensoes import categorias

archives = list()

sys = os.environ

user_path = input("Insira o caminho do diretório: ")
os.chdir(user_path)

for item in os.scandir():
    if (item.is_file):
        archives.append(item.name)

try:
    for k in categorias.keys():
        os.mkdir(k)

    os.mkdir("Outros")

except(e):
    print(e)

finally:
    print("Pastas já estão criadas")


for i in range(len(archives)):
    archive_ext = archives[i].split('.')
    ext = archive_ext[-1]
    moved = False

    for k, v in categorias.items():
        if ext in v:
            move(archives[i], k)
            moved = True

    if not moved:
        move(archives[i], "Outros")
