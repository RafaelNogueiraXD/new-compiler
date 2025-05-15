from modulos.tabelaSimbolos import TabelaDeSimbolos
class AnalisadorSemantico:
    def __init__(self):
        self.tabela = TabelaDeSimbolos()

    def verificar_atribuicao(self, nome, expressao):
        simbolo = self.tabela.obter_simbolo(nome)
        tipo_variavel = simbolo['tipo']
        tipo_expressao = self.inferir_tipo(expressao)

        if tipo_variavel != tipo_expressao:
            raise Exception(f"Erro semântico: atribuição incompatível '{tipo_variavel}' <- '{tipo_expressao}'")

    def inferir_tipo(self, expressao):
        if isinstance(expressao, tuple):
            if expressao[0] == 'binop':
                tipo_esquerda = self.inferir_tipo(expressao[2])
                tipo_direita = self.inferir_tipo(expressao[3])

                if tipo_esquerda != tipo_direita:
                    raise Exception(f"Erro semântico: operação entre tipos diferentes '{tipo_esquerda}' e '{tipo_direita}'")
                return tipo_esquerda

            elif expressao[0] == 'vetor_acesso':
                nome = expressao[1]
                simbolo = self.tabela.obter_simbolo(nome)
                if simbolo['categoria'] != 'vetor':
                    raise Exception(f"Erro semântico: '{nome}' não é um vetor")
                return simbolo['tipo']

            elif expressao[0] == 'relacional':
                # Relacionais sempre retornam booleano (inteiro no seu caso)
                return 'inteiro'
        else:
            if isinstance(expressao, int):
                return 'inteiro'
            elif isinstance(expressao, float):
                return 'flutuante'
            elif isinstance(expressao, str):
                if expressao.startswith('"') and expressao.endswith('"'):
                    return 'texto'
                else:
                    simbolo = self.tabela.obter_simbolo(expressao)
                    return simbolo['tipo']

        raise Exception(f"Erro semântico: expressão desconhecida '{expressao}'")
    def verificar_acesso_vetor(self, nome, indice_expr):
        simbolo = self.tabela.obter_simbolo(nome)
        if simbolo['categoria'] != 'vetor':
            raise Exception(f"Erro semântico: '{nome}' não é um vetor")

        if isinstance(indice_expr, int):
            if not (0 <= indice_expr < simbolo['tamanho']):
                raise Exception(f"Erro semântico: índice {indice_expr} fora dos limites de '{nome}'")
        # Caso o índice seja uma variável, ignoramos por enquanto
