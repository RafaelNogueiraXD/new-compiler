class TabelaDeSimbolos:
    def __init__(self):
        self.simbolos = {}
        self.errors = []
        self.escopos = [{}]
    
    def entra_escopo(self):
        self.escopos.append()
    
    def sai_escopo(self):
        self.escopos.pop()

    def declarar_variavel(self, nome, tipo, info_extra=None):
        escopo_atual = self.escopos[-1]
        if nome in escopo_atual:
            # raise Exception(f"Erro semântico: variável '{nome}' já declarada")
            self.errors.append(f"Erro semantico: variavel '{nome}' ja declarada")
        else:
            escopo_atual[nome] = {'tipo': tipo, 'categoria': 'variavel'}
            # self.simbolos[nome] = {'tipo': tipo, 'categoria': 'variavel'}

    def buscar(self, nome):
        for escopo in reversed(self.escopos):
            if nome in escopo:
                return escopo[nome]
        self.errors.append(f"Erro semântico: variável '{nome}' não declarada")
        
    def declarar_vetor(self, nome, tipo, tamanho):
        if nome in self.simbolos:
            self.errors.append(f"Erro semantico: variavel '{nome}' ja declarada")
            # raise Exception(f"Erro semântico: vetor '{nome}' já declarado")
        self.simbolos[nome] = {'tipo': tipo, 'categoria': 'vetor', 'tamanho': tamanho}

    def obter_simbolo(self, nome):
        if nome not in self.simbolos:
            self.errors.append(f"Erro semantico: variavel '{nome}' nao foi declarado")
            # raise Exception(f"Erro semântico: '{nome}' não foi declarado")
        return self.simbolos[nome]
    
    def print_symbol_table(self):
        print("\n=== TABELA DE SÍMBOLOS ===")
        print(f"{'Nome':<15} {'Tipo':<10} {'Categoria':<15} {'Tamanho':<10}")
        print("-" * 55)
        for name, info in self.simbolos.items():
            tipo = info.get('tipo', '')
            categoria = info.get('categoria', '')
            tamanho = str(info.get('tamanho', '')) if 'tamanho' in info else ''
            print(f"{name:<15} {tipo:<10} {categoria:<15} {tamanho:<10}")
        print("=" * 55 + "\n")