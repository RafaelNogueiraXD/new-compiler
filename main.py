from modulos.parser import Parser
from modulos.tac import GeradorTAC
from pprint import pprint
import json
import sys


if __name__ == "__main__":

    codigo = """
    funcao teste():{
        flutuante recebe = 10.0;
        recebe = 10.0;
        se(recebe < 10){
            imprime("ola");
        }
        flutuante recebe2[10];
        imprime("ola mundo"); #comentario
        retorna 5;
    }
    """
    parser = Parser()
    resultado = parser.parse(codigo)
    with open('ast_output.json', 'w') as f:
        json.dump(resultado, f, indent=2)
    pprint(resultado, sort_dicts=False)
    print("\n\n\n\n \t Mostrando ")
    gen = GeradorTAC()
    gen.gerar(resultado)
    gen.imprimir()
        
