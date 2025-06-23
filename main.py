from modulos.parser import Parser
from modulos.tac import GeradorTAC
from modulos.assembly import GeradorAssembly
from pprint import pprint
import json
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.txt>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]

    if not os.path.exists(caminho_arquivo):
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        sys.exit(1)

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        codigo = f.read()

    print(f"\n>> Código recebido de '{caminho_arquivo}':\n")
    print(codigo)
    print("\n>> Analisando...\n")

    parser = Parser()
    resultado = parser.parse(codigo)

    with open('ast_output.json', 'w') as f:
        json.dump(resultado, f, indent=2)

    pprint(resultado, sort_dicts=False)

    print("\n\n>> Gerando código intermediário (TAC):\n")
    gen = GeradorTAC()
    gen.gerar(resultado)
    gen.imprimir()

    asm_gen = GeradorAssembly(gen.codigo)
    asm_gen.gerar()
    asm_gen.imprimir()

