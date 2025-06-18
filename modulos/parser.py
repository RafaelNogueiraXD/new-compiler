import ply.yacc as yacc
from modulos.lexer import Lexer
from modulos.semantico import AnalisadorSemantico

class Parser:
    tokens = Lexer.tokens

    def __init__(self):
        self.lexer = Lexer()
        self.lexer.build()
        self.analisador_semantico = AnalisadorSemantico()
        self.parser = yacc.yacc(module=self)

    # --- Regras de gramática ---
    def p_programa(self, p):
        '''programa : declaracoes'''
        p[0] = ('programa', p[1])

    def p_declaracoes(self, p):
        '''declaracoes : declaracao declaracoes
                       | declaracao '''
        if len(p) == 3:
            p[0] = [p[1]] + p[2]
        else:
            p[0] = [p[1]]

    def p_declaracao(self, p):
        '''declaracao : tipo IDENTIFICADOR ATRIBUIR expressao PONTO_E_VIRGULA
                    | tipo IDENTIFICADOR ABRE_COLCHETE NUMERO FECHA_COLCHETE PONTO_E_VIRGULA
                    | comando'''
        if len(p) == 6 and p[2] != '[':
            
            self.analisador_semantico.tabela.declarar_variavel(p[2], p[1])
            p[0] = ('declaracao_var', p[1], p[2], p[4])
        elif len(p) == 7:
            self.analisador_semantico.tabela.declarar_vetor(p[2], p[1], p[4])
            p[0] = ('vetor_declaracao', p[2], p[4])
        else:
            p[0] = p[1]

    def p_tipo(self, p):
        '''tipo : INTEIRO
                | FLUTUANTE_TIPO
                | TEXTO_TIPO'''
        p[0] = p[1]

    def p_expressao(self, p):
        '''expressao : NUMERO
                     | FLUTUANTE
                     | TEXTO
                     | IDENTIFICADOR'''
        p[0] = p[1]
    def p_comandos(self, p):
        '''comandos : comandos comando
                    | comando'''
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1]]    


    def p_comando(self, p):
        '''comando : IDENTIFICADOR ABRE_COLCHETE expressao FECHA_COLCHETE ATRIBUIR expressao PONTO_E_VIRGULA
                | IDENTIFICADOR ATRIBUIR expressao PONTO_E_VIRGULA
                | IMPRIME ABRE_PARENTESE expressao FECHA_PARENTESE PONTO_E_VIRGULA
                | FUNCAO IDENTIFICADOR ABRE_PARENTESE FECHA_PARENTESE DOIS_PONTOS ABRE_CHAVE declaracoes FECHA_CHAVE
                | ENQUANTO ABRE_PARENTESE expressao FECHA_PARENTESE ABRE_CHAVE declaracoes FECHA_CHAVE
                | SE ABRE_PARENTESE expressao FECHA_PARENTESE ABRE_CHAVE declaracoes FECHA_CHAVE
                | SE ABRE_PARENTESE expressao FECHA_PARENTESE ABRE_CHAVE declaracoes FECHA_CHAVE SE_NAO ABRE_CHAVE declaracoes FECHA_CHAVE
                | RETORNA expressao PONTO_E_VIRGULA
                | CORTE PONTO_E_VIRGULA'''
                
        if len(p) == 8 and p[2] == '[':
            # Atribuição em vetor
            self.analisador_semantico.verificar_atribuicao(p[1], p[3])
            p[0] = ('vetor_atribuicao', p[1], p[3], p[6])
        elif p[1] == 'imprime':
            p[0] = ('imprime', p[3])
        elif p[1] == 'funcao':
            self.analisador_semantico.tabela.entra_escopo()
            p[0] = ('funcao', p[2], p[7])
            # self.analisador_semantico.tabela.sai_escopo()
        elif p[1] == 'enquanto':
            p[0] = ('enquanto', p[3], p[6])
        elif p[1] == 'se':
            if len(p) == 8:
                p[0] = ('se', p[3], p[6])
            else:
                p[0] = ('se_senao', p[3], p[6], p[10])
        elif p[1] == 'retorna':
            p[0] = ('retorna', p[2])
        elif p[1] == 'corte':
            p[0] = ('corte',)
        else:
            # Caso IDENTIFICADOR = expressao;
            self.analisador_semantico.verificar_atribuicao(p[1], p[3])
            p[0] = ('atribuicao', p[1], p[3])

    def p_error(self, p):
        if p:
            print(f"Erro de sintaxe na linha {p.lineno}, token inesperado: '{p.value}'")
        else:
            print("Erro de sintaxe: fim de arquivo inesperado")

    def parse(self, code):
        # return self.parser.parse(code, lexer=self.lexer.lexer)
        resultado = self.parser.parse(code, lexer=self.lexer.lexer)
        if self.analisador_semantico.tabela.errors:
            for erro in self.analisador_semantico.tabela.errors:
                print(f"[ERRO SEMÂNTICO] {erro}")
        self.analisador_semantico.tabela.print_symbol_table()
        
        self.analisador_semantico.tabela.sai_escopo()
        return resultado
        
    def p_bloco(self, p):
        '''bloco : ABRE_CHAVE comandos FECHA_CHAVE'''
        p[0] = p[2]
    
    def p_expressao_relacional(self, p):
        '''expressao : expressao MENOR expressao
                    | expressao MAIOR expressao
                    | expressao MENOR_IGUAL expressao
                    | expressao MAIOR_IGUAL expressao
                    | expressao IGUAL expressao
                    | expressao DIFERENTE expressao'''
        p[0] = ('relacional', p[2], p[1], p[3])


        
    def p_expressao_binaria(self, p):
        '''expressao : expressao SOMA expressao
                    | expressao MENOS expressao
                    | expressao MULTIPLICA expressao
                    | expressao DIVIDE expressao
                    | expressao '>' expressao
                    | expressao '<' expressao
                    | expressao ATRIBUIR expressao'''
        p[0] = ('binop', p[2], p[1], p[3])
    


    
    def p_expressao_vetor(self, p):
        '''expressao : IDENTIFICADOR ABRE_COLCHETE expressao FECHA_COLCHETE'''
        p[0] = ('vetor_acesso', p[1], p[3])
        p[0] = ('vetor_acesso', p[1], p[3])
        
