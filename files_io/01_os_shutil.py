import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent #"deixa o caminho dinamico

#os.mkdir(ROOT_PATH / "novo-diretorio")

arquivo = open(ROOT_PATH / "Novo.txt", "w")
arquivo.close()

os.rename(ROOT_PATH / "Novo.txt", ROOT_PATH / "alterado.txt") #Renomeia um arquivo
os.remove(ROOT_PATH / "Novo.txt") #Remove um arquivo

