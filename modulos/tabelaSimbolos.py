class TabelaDeSimbolos:
    def __init__(self):
        self.simbolos = {}
        self.errors = []
        self.escopos = [{}]
    
    def entra_escopo(self):
        self.escopos.append({})
    
    def sai_escopo(self):
        self.escopos.pop()

    def declarar_variavel(self, nome, tipo, info_extra=None):
        escopo_atual = self.escopos[-1]
        if nome in escopo_atual:
            # raise Exception(f"Erro semântico: variável '{nome}' já declarada")
            self.errors.append(f"Erro semantico: variavel '{nome}' ja declarada")
        else:
            escopo_atual[nome] = {
                'tipo': tipo,
                'categoria': 'variavel'}
            self.simbolos[nome] = {'tipo': tipo, 'categoria': 'variavel'}

            

    def buscar(self, nome):
        print("DEBUG buscar:", repr(nome))
        for escopo in reversed(self.escopos):
            if nome in escopo:
                return escopo[nome]
        self.errors.append(f"Erro semântico: variável '{nome}' não declarada")
        
    def declarar_vetor(self, nome, tipo, tamanho):
        escopo_atual = self.escopos[-1]
        if nome in escopo_atual:
            self.errors.append(f"Erro semantico: variavel '{nome}' ja declarada")
        else:
            escopo_atual[nome] = {'tipo': tipo, 'categoria': 'vetor', 'tamanho': tamanho}
        
    # def declarar_vetor(self, nome, tipo, tamanho):
    #     escopo_atual = self.escopos[-1]
    #     if nome in escopo_atual:
    #         self.errors.append(f"Erro semantico: vetor '{nome}' ja declarado")
    #     else:
    #         escopo_atual[nome] = {
    #             'tipo': tipo,
    #             'categoria': 'vetor',
    #             'tamanho': tamanho}
            
    def obter_simbolo(self, nome):
        simbolo = self.buscar(nome)
        if simbolo is None:
            self.errors.append(f"Erro semantico: variavel '{nome}' nao foi declarada")
            return None
        return simbolo
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


    def print_tabela(self):
        print("\n=== TABELA DE SÍMBOLOS POR ESCOPO ===")
        for i, escopo in enumerate(self.escopos):
            print(f"Escopo {i}:")
            for nome, info in escopo.items():
                tipo = info.get('tipo', '')
                categoria = info.get('categoria', '')
                tamanho = info.get('tamanho', '')
                print(f"  {nome:<12} {tipo:<10} {categoria:<10} {tamanho}")
        print("=" * 40 + "\n")