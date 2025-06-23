from modulos.tabelaSimbolos import TabelaDeSimbolos
class AnalisadorSemantico:
    def __init__(self):
        self.tabela = TabelaDeSimbolos()
    def analisar(self, nodo):
        if isinstance(nodo, list):
            for n in nodo:
                self.analisar(n)
            return

        tipo = nodo[0]

        if tipo == 'programa':
            _, corpo = nodo
            self.analisar(corpo)

        elif tipo == 'funcao':
            _, nome, corpo = nodo
            self.tabela.entra_escopo()
            self.analisar(corpo)
            self.tabela.sai_escopo()

        elif tipo == 'declaracao_var':
            _, tipo_var, nome, valor = nodo
            self.tabela.declarar_variavel(nome, tipo_var)
            if valor is not None:
                self.inferir_tipo(valor)

        elif tipo == 'vetor_declaracao':
            _, nome, tamanho = nodo
            self.tabela.declarar_vetor(nome, 'flutuante', tamanho)  # ou tipo específico
        elif tipo == 'chamada_funcao':
            _, nome_funcao = nodo
        elif tipo == 'atribuicao':
            _, nome, expr = nodo
            self.verificar_atribuicao(nome, expr)

        elif tipo == 'vetor_atribuicao':
            _ = nodo
            # self.verificar_atribuicao(nome, expr)

        elif tipo == 'imprime':
            _, expr = nodo
            self.inferir_tipo(expr)

        elif tipo == 'retorna':
            _, expr = nodo
            self.inferir_tipo(expr)

        elif tipo == 'se':
            _, condicao, bloco = nodo
            self.inferir_tipo(condicao)
            self.analisar(bloco)

        elif tipo == 'se_senao':
            _, condicao, bloco_if, bloco_else = nodo
            self.inferir_tipo(condicao)
            self.analisar(bloco_if)
            self.analisar(bloco_else)

        elif tipo == 'enquanto':
            _, condicao, bloco = nodo
            self.inferir_tipo(condicao)
            self.analisar(bloco)

        else:
            self.tabela.errors.append(f"Nó desconhecido na análise semântica: {tipo}")      

    def verificar_atribuicao(self, nome, expressao):
        simbolo = self.tabela.obter_simbolo(nome)
        tipo_variavel = simbolo['tipo']
        tipo_expressao = self.inferir_tipo(expressao)

        if tipo_variavel != tipo_expressao:
            self.tabela.errors.append(f"Erro semântico: atribuição incompatível '{tipo_variavel}' <- '{tipo_expressao}'")
            # raise Exception(f"Erro semântico: atribuição incompatível '{tipo_variavel}' <- '{tipo_expressao}'")

    def inferir_tipo(self, expressao):
        if isinstance(expressao, tuple):
            if expressao[0] == 'binop':
                tipo_esquerda = self.inferir_tipo(expressao[2])
                tipo_direita = self.inferir_tipo(expressao[3])

                if tipo_esquerda != tipo_direita:
                    self.tabela.errors.append(f"Erro semântico: operação entre tipos diferentes '{tipo_esquerda}' e '{tipo_direita}'")
                    # raise Exception(f"Erro semântico: operação entre tipos diferentes '{tipo_esquerda}' e '{tipo_direita}'")
                return tipo_esquerda

            elif expressao[0] == 'vetor_acesso':
                nome = expressao[1]
                simbolo = self.tabela.obter_simbolo(nome)
                if simbolo['categoria'] != 'vetor':
                    self.tabela.errors.append(f"Erro semântico: '{nome}' não é um vetor")
                    # raise Exception(f"Erro semântico: '{nome}' não é um vetor")
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
                    if simbolo is None:
                        return None
                    return simbolo['tipo']

        self.tabela.errors.append(f"Erro semântico: expressão desconhecida '{expressao}'")
        # raise Exception(f"Erro semântico: expressão desconhecida '{expressao}'")
    def verificar_acesso_vetor(self, nome, indice_expr):
        simbolo = self.tabela.obter_simbolo(nome)
        if simbolo['categoria'] != 'vetor':
            self.tabela.errors.append(f"Erro semântico: '{nome}' não é um vetor")
            # raise Exception(f"Erro semântico: '{nome}' não é um vetor")

        if isinstance(indice_expr, int):
            if not (0 <= indice_expr < simbolo['tamanho']):
                self.tabela.errors.append(f"Erro semântico: índice {indice_expr} fora dos limites de '{nome}'")
                # raise Exception(f"Erro semântico: índice {indice_expr} fora dos limites de '{nome}'")
        # Caso o índice seja uma variável, ignoramos por enquanto
