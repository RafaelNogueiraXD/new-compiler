from modulos.parser import Parser
from pprint import pprint
import json


if __name__ == "__main__":
    codigo = """
    funcao saudacao():{
        inteiro variante = 10;
        imprime("hello world");
    }
    """

    parser = Parser()
    resultado = parser.parse(codigo)
    with open('ast_output.json', 'w') as f:
        json.dump(resultado, f, indent=2)
    pprint(resultado, sort_dicts=False)
