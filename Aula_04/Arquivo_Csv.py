import csv
from pathlib import Path

ROOT_PACH = Path(__file__).parent

try:
    with open(ROOT_PACH / "usuario.csv", "w", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id" , "Nome"])
        escritor.writerow(["1", "brunno"])
        escritor.writerow(["2", "Guilherme"])
except IOError as esx:
    print(f"Error ao criar o arquivo. {exc}")
