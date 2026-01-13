from pathlib import Path

ROOT_PATH = Path(__file__).parent
arquivo = open("meu_arquivo.py")

try: 
    arquivo = open(ROOT_PATH / "novo-diretorio")

except FileExistsError as exc:
    print("Arquivo não encontrado!")

except IsADirectoryError as exc:
    print(f"não foi possivel abrir um arquivo: {exc}")

except IOError as exc:
    print(f"Erro ao abrir um arquivo: {exc}")

except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")