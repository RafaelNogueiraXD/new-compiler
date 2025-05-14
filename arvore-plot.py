import sys
import json
from graphviz import Digraph

def desenhar_arvore(ast, nome_arquivo='arvore', saida='arvore_output'):
    grafo = Digraph(name=nome_arquivo, format='png')
    contador = {'id': 0}

    def adicionar_no(no, pai=None):
        # Define o rótulo do nó
        if isinstance(no, dict):
            label = no.get('tipo', 'dict')
        elif isinstance(no, list):
            label = 'lista'
        else:
            label = str(no)

        node_id = str(contador['id'])
        contador['id'] += 1
        grafo.node(node_id, label)

        if pai is not None:
            grafo.edge(pai, node_id)

        # Processa filhos
        if isinstance(no, dict):
            for chave, valor in no.items():
                chave_id = str(contador['id'])
                contador['id'] += 1
                grafo.node(chave_id, chave)
                grafo.edge(node_id, chave_id)
                adicionar_no(valor, chave_id)

        elif isinstance(no, list):
            for item in no:
                adicionar_no(item, node_id)

        return node_id

    adicionar_no(ast)
    grafo.render(saida, view=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python visualizar_arvore.py <arquivo_json_ast>")
        sys.exit(1)

    caminho = sys.argv[1]

    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            ast = json.load(f)
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho}' não encontrado.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Erro ao ler JSON: {e}")
        sys.exit(1)

    desenhar_arvore(ast)
