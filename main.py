from modulos.parser import Parser
from modulos.tac import GeradorTAC
from pprint import pprint
import json
import sys


if __name__ == "__main__":
    # codigo = """
    # funcao main():{
    #     inteiro variante = 10;
    #     imprime("hello world");
    #     enquanto (variante < 10){
    #         imprime("ola mundo");
    #         variante = variante - 1;
    #     } 
    #     se (variante > 0) {
    #         imprime("positivo");
    #     } se_nao {
    #         imprime("negativo ou zero");
    #     }
    #     inteiro numeros[5];
    #     numeros[0] = 10;
    #     imprime(numeros[0]);
    # }
    # """

    codigo = """
    funcao teste():{
        flutuante recebe = 10;
        flutuante recebe2[10];
        imprime("ola mundo"); #comentario
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
        
