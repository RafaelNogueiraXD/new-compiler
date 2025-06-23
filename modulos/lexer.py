import ply.lex as lex


class Lexer:
    # Lista de tokens
    tokens = [
        'NUMERO', 'FLUTUANTE', 'TEXTO', 'IDENTIFICADOR', 'ATRIBUIR',
        'SOMA', 'MENOS', 'MULTIPLICA', 'DIVIDE', 'ABRE_PARENTESE',
        'FECHA_PARENTESE', 'ABRE_CHAVE', 'FECHA_CHAVE', 'PONTO_E_VIRGULA',
        'DOIS_PONTOS', 'VIRGULA', 'SE', 'SE_NAO', 'ENQUANTO', 'PARA',
        'RETORNA', 'IMPRIME', 'FUNCAO', 'TENTA', 'PEGA', 'INTEIRO', 'FLUTUANTE_TIPO', 'TEXTO_TIPO',
        'MENOR', 'MAIOR', 'IGUAL', 'DIFERENTE', 'MENOR_IGUAL', 'MAIOR_IGUAL',
        'ABRE_COLCHETE', 'FECHA_COLCHETE','CORTE'
        
    ]

    # Palavras reservadas
    keywords = {
        'se': 'SE',
        'se_nao': 'SE_NAO',
        'enquanto': 'ENQUANTO',
        'para': 'PARA',
        'retorna': 'RETORNA',
        'imprime': 'IMPRIME',
        'funcao': 'FUNCAO',
        'tenta': 'TENTA',
        'pega': 'PEGA',
        'inteiro': 'INTEIRO',
        'flutuante': 'FLUTUANTE_TIPO',
        'texto': 'TEXTO_TIPO',
        'corte': 'CORTE'
    }
    t_ABRE_COLCHETE = r'\['
    t_FECHA_COLCHETE = r'\]'
    # Tokens simples
    t_ignore = ' \t'
    t_SOMA = r'\+'
    t_MENOS = r'-'
    t_MULTIPLICA = r'\*'
    t_DIVIDE = r'/'
    t_ATRIBUIR = r'='
    t_ABRE_PARENTESE = r'\('
    t_FECHA_PARENTESE = r'\)'
    t_ABRE_CHAVE = r'\{'
    t_FECHA_CHAVE = r'\}'
    t_PONTO_E_VIRGULA = r';'
    t_DOIS_PONTOS = r':'
    t_VIRGULA = r','
    
    t_MENOR = r'<'
    t_MAIOR = r'>'
    t_IGUAL = r'=='
    t_DIFERENTE = r'!='
    t_MENOR_IGUAL = r'<='
    t_MAIOR_IGUAL = r'>='
    

    def t_FLUTUANTE(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_NUMERO(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_TEXTO(self, t):
        r'\".*?\"'
        # t.value = t.value[1:-1]
        return t

    def t_IDENTIFICADOR(self, t):
        r'[a-zA-Z_]\w*'
        t.type = self.keywords.get(t.value, 'IDENTIFICADOR')
        return t

    def t_COMENTARIO(self, t):
        r'\#.*'
        pass

    def t_NOVA_LINHA(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Erro léxico: caractere inesperado '{t.value[0]}' na linha {t.lineno}")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def input(self, data):
        self.lexer.input(data)

    def token(self):
        return self.lexer.token()
