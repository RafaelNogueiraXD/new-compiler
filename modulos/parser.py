import ply.yacc as yacc
from modulos.lexer import Lexer

class Parser:
    tokens = Lexer.tokens

    def __init__(self):
        self.lexer = Lexer()
        self.lexer.build()
        self.parser = yacc.yacc(module=self)

    # --- Regras de gramática ---
    def p_programa(self, p):
        '''programa : declaracoes'''
        p[0] = ('programa', p[1])

    def p_declaracoes(self, p):
        '''declaracoes : declaracao declaracoes
                       | declaracao'''
        if len(p) == 3:
            p[0] = [p[1]] + p[2]
        else:
            p[0] = [p[1]]

    def p_declaracao(self, p):
        '''declaracao : tipo IDENTIFICADOR ATRIBUIR expressao PONTO_E_VIRGULA
                      | comando'''
        if len(p) == 6:
            p[0] = ('declaracao_var', p[1], p[2], p[4])
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

    def p_comando(self, p):
        '''comando : IMPRIME ABRE_PARENTESE expressao FECHA_PARENTESE PONTO_E_VIRGULA
                   | FUNCAO IDENTIFICADOR ABRE_PARENTESE FECHA_PARENTESE DOIS_PONTOS ABRE_CHAVE declaracoes FECHA_CHAVE'''
        if p[1] == 'imprime':
            p[0] = ('imprime', p[3])
        else:
            p[0] = ('funcao', p[2], p[7])

    def p_error(self, p):
        if p:
            print(f"Erro de sintaxe na linha {p.lineno}, token inesperado: '{p.value}'")
        else:
            print("Erro de sintaxe: fim de arquivo inesperado")

    def parse(self, code):
        return self.parser.parse(code, lexer=self.lexer.lexer)
