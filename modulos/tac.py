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
        if isinstance(nodo, (int, float, str)):
            return self.gerar_literal(nodo)
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

        elif kind == 'vetor_atribuicao':
            _, nome, indice, valor = nodo
            idx_temp = self.gerar_literal(indice)
            val_temp = self.gerar_literal(valor)
            self.codigo.append(f"{nome}[{idx_temp}] = {val_temp}")

        elif kind == 'imprime':
            _, expr = nodo
            temp = self.gerar_literal(expr)
            self.codigo.append(f"print {temp}")
            
            
        elif kind == 'retorna':
            _, expr = nodo
            if isinstance(expr, tuple):
                temp = self.gerar(expr)
            else:
                temp = self.gerar_literal(expr)
            self.codigo.append(f"return {temp}")
      
            
            
        elif kind == 'se':
            _, condicao, bloco = nodo
            cond = self.gerar(condicao)
            label_fim = self.novo_label()
            self.codigo.append(f"if_false {cond} goto {label_fim}") 
            for instr in bloco:
                self.gerar(instr)
            self.codigo.append(f"{label_fim}:")
        elif kind == 'se_senao':
            _, condicao, bloco_if, bloco_else = nodo
            cond = self.gerar(condicao)
            label_else = self.novo_label()
            label_fim = self.novo_label()

            self.codigo.append(f"if_false {cond} goto {label_else}")
            for instr in bloco_if:
                self.gerar(instr)
            self.codigo.append(f"goto {label_fim}")
            self.codigo.append(f"{label_else}:")
            for instr in bloco_else:
                self.gerar(instr)
            self.codigo.append(f"{label_fim}:")
            
        elif kind == 'enquanto':
            _, condicao, bloco = nodo
            label_inicio = self.novo_label()
            label_fim = self.novo_label()

            self.codigo.append(f"{label_inicio}:")
            cond = self.gerar(condicao)
            self.codigo.append(f"if_false {cond} goto {label_fim}")
            for instr in bloco:
                self.gerar(instr)
            self.codigo.append(f"goto {label_inicio}")
            self.codigo.append(f"{label_fim}:")


        elif kind == 'chamada_funcao':
            _, nome_funcao = nodo
            self.codigo.append(f"call {nome_funcao}")

        
        elif kind == 'relacional':
            _, op, left, right = nodo
            temp = self.novo_temp()
            left_temp = self.gerar_literal(left)
            right_temp = self.gerar_literal(right)
            self.codigo.append(f"{temp} = {left_temp} {op} {right_temp}")
            return temp
            
        elif kind == 'binop':
            _, op, left, right = nodo
            temp = self.novo_temp()
            left_temp = self.gerar_literal(left)
            right_temp = self.gerar_literal(right)
            self.codigo.append(f"{temp} = {left_temp} {op} {right_temp}")
            return temp
            
        elif kind == 'atribuicao':
            _, var, expr = nodo
            expr_temp = self.gerar(expr)
            self.codigo.append(f"{var} = {expr_temp}")
        else:
            raise Exception(f"TAC: nó não suportado: {nodo}")

    def gerar_literal(self, lit):
        if isinstance(lit, (int, float)):
            return str(lit)
        elif isinstance(lit, str):
            if lit.startswith('"') and lit.endswith('"'):
                return lit
            return f'"{lit}"'
        else:
            return lit

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
    
    print("Teste de IF: ")
    
    teste = ('programa', [
        ('funcao', 'teste', [
            ('se', ('relacional', '>', 'x', 0), [
                ('imprime', 'x')
            ])
        ])
    ])
    teste_if = GeradorTAC()
    teste_if.gerar(teste)
    teste_if.imprimir()
    
    print("Teste de WHILE: ")

    testeWhile1 = ('programa', [
        ('funcao', 'teste', [
            ('enquanto', ('relacional', '>', 'x', 0), [
                ('imprime', 'x'),
                ('atribuicao', 'x', ('binop', '-', 'x', 1))
            ])
        ])
    ])
    testeWhile = GeradorTAC()
    testeWhile.gerar(testeWhile1)
    testeWhile.imprimir()