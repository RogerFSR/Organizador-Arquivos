import os
from shutil import (
move, 

) 
from extensoes import categorias

sys = os.environ

user_path = input("Insira o caminho do diretório: ")
os.chdir(user_path)

for k, v in categorias.items():
    os.mkdir(k)
