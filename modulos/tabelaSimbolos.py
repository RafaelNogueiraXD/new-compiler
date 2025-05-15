class TabelaDeSimbolos:
    def __init__(self):
        self.simbolos = {}

    def declarar_variavel(self, nome, tipo):
        if nome in self.simbolos:
            raise Exception(f"Erro semântico: variável '{nome}' já declarada")
        self.simbolos[nome] = {'tipo': tipo, 'categoria': 'variavel'}

    def declarar_vetor(self, nome, tipo, tamanho):
        if nome in self.simbolos:
            raise Exception(f"Erro semântico: vetor '{nome}' já declarado")
        self.simbolos[nome] = {'tipo': tipo, 'categoria': 'vetor', 'tamanho': tamanho}

    def obter_simbolo(self, nome):
        if nome not in self.simbolos:
            raise Exception(f"Erro semântico: '{nome}' não foi declarado")
        return self.simbolos[nome]
