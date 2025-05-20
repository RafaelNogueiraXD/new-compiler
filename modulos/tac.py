class GeradorTAC:
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0
        self.codigo = []

    def novo_temp(self):
        nome = f"t{self.temp_count}"
        self.temp_count += 1
        return nome

    def novo_label(self):
        nome = f"L{self.label_count}"
        self.label_count += 1
        return nome

    def gerar(self, nodo):
        kind = nodo[0]

        if kind == 'programa':
            _, decls = nodo
            for d in decls:
                self.gerar(d)

        elif kind == 'funcao':
            _, nome, corpo = nodo
            self.codigo.append(f"func {nome}:")
            for instr in corpo:
                self.gerar(instr)
            self.codigo.append(f"endfunc {nome}")
        
        elif kind == 'declaracao_var':
            _, tipo, nome, valor = nodo
            temp = self.gerar_literal(valor)
            self.codigo.append(f"{nome} = {temp}    # tipo {tipo}")

        elif kind == 'vetor_declaracao':
            _, nome, tamanho = nodo
            self.codigo.append(f"{nome} = alloc_array {tamanho}")

        elif kind == 'imprime':
            _, expr = nodo
            temp = self.gerar_literal(expr)
            self.codigo.append(f"print {temp}")

        else:
            raise Exception(f"TAC: nó não suportado: {nodo}")

    def gerar_literal(self, lit):
        # Se for número
        if isinstance(lit, (int, float)):
            return str(lit)
        # Se for string
        return f"\"{lit}\""

    def imprimir(self):
        for linha in self.codigo:
            print(linha)


if __name__ == "__main__":
    ast = ('programa',
        [('funcao',
        'teste',
        [('declaracao_var', 'flutuante', 'recebe', 10),
        ('vetor_declaracao', 'recebe2', 10),
        ('imprime', 'ola mundo')])])

    gen = GeradorTAC()
    gen.gerar(ast)
    gen.imprimir()