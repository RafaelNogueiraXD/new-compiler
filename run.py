import subprocess
import os
from pathlib import Path

# Caminho dos testes e da main
PASTA_TESTES = Path("./exemplos/")
MAIN_SCRIPT = "main.py"

def testar_todos():
    arquivos = sorted(PASTA_TESTES.glob("*.txt"))

    if not arquivos:
        print("Nenhum arquivo de teste encontrado.")
        return

    for arquivo in arquivos:
        print("\n" + "="*50)
        print(f"Executando: {arquivo.name}")
        print("="*50 + "\n")
        
        resultado = subprocess.run(["python3", MAIN_SCRIPT, str(arquivo)], text=True)
        
        if resultado.returncode != 0:
            print(f"\n❌ Erro ao executar {arquivo.name}\n")

if __name__ == "__main__":
    testar_todos()
