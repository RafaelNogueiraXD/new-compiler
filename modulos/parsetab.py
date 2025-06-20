
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ABRE_CHAVE ABRE_COLCHETE ABRE_PARENTESE ATRIBUIR CORTE DIFERENTE DIVIDE DOIS_PONTOS ENQUANTO FECHA_CHAVE FECHA_COLCHETE FECHA_PARENTESE FLUTUANTE FLUTUANTE_TIPO FUNCAO IDENTIFICADOR IGUAL IMPRIME INTEIRO MAIOR MAIOR_IGUAL MENOR MENOR_IGUAL MENOS MULTIPLICA NUMERO PARA PEGA PONTO_E_VIRGULA RETORNA SE SE_NAO SOMA TENTA TEXTO TEXTO_TIPO VIRGULAprograma : declaracoesdeclaracoes : declaracao declaracoes\n                       | declaracao declaracao : tipo IDENTIFICADOR ATRIBUIR expressao PONTO_E_VIRGULA\n                    | tipo IDENTIFICADOR ABRE_COLCHETE NUMERO FECHA_COLCHETE PONTO_E_VIRGULA\n                    | comandotipo : INTEIRO\n                | FLUTUANTE_TIPO\n                | TEXTO_TIPOexpressao : NUMERO\n                     | FLUTUANTE\n                     | TEXTO\n                     | IDENTIFICADORcomandos : comandos comando\n                    | comandocomando : IDENTIFICADOR ABRE_COLCHETE expressao FECHA_COLCHETE ATRIBUIR expressao PONTO_E_VIRGULA\n                | IDENTIFICADOR ATRIBUIR expressao PONTO_E_VIRGULA\n                | IMPRIME ABRE_PARENTESE expressao FECHA_PARENTESE PONTO_E_VIRGULA\n                | FUNCAO IDENTIFICADOR ABRE_PARENTESE FECHA_PARENTESE DOIS_PONTOS ABRE_CHAVE declaracoes FECHA_CHAVE\n                | ENQUANTO ABRE_PARENTESE expressao FECHA_PARENTESE ABRE_CHAVE declaracoes FECHA_CHAVE\n                | SE ABRE_PARENTESE expressao FECHA_PARENTESE ABRE_CHAVE declaracoes FECHA_CHAVE\n                | SE ABRE_PARENTESE expressao FECHA_PARENTESE ABRE_CHAVE declaracoes FECHA_CHAVE SE_NAO ABRE_CHAVE declaracoes FECHA_CHAVE\n                | RETORNA expressao PONTO_E_VIRGULA\n                | CORTE PONTO_E_VIRGULAbloco : ABRE_CHAVE comandos FECHA_CHAVEexpressao : expressao MENOR expressao\n                    | expressao MAIOR expressao\n                    | expressao MENOR_IGUAL expressao\n                    | expressao MAIOR_IGUAL expressao\n                    | expressao IGUAL expressao\n                    | expressao DIFERENTE expressaoexpressao : expressao SOMA expressao\n                    | expressao MENOS expressao\n                    | expressao MULTIPLICA expressao\n                    | expressao DIVIDE expressao\n                    | expressao '>' expressao\n                    | expressao '<' expressao\n                    | expressao ATRIBUIR expressaoexpressao : IDENTIFICADOR ABRE_COLCHETE expressao FECHA_COLCHETE"
    
_lr_action_items = {'INTEIRO':([0,3,6,29,38,56,75,78,80,81,83,85,88,90,91,92,94,96,],[7,7,-6,-24,-23,-17,-4,-18,7,7,-5,7,-16,-20,-21,-19,7,-22,]),'FLUTUANTE_TIPO':([0,3,6,29,38,56,75,78,80,81,83,85,88,90,91,92,94,96,],[8,8,-6,-24,-23,-17,-4,-18,8,8,-5,8,-16,-20,-21,-19,8,-22,]),'TEXTO_TIPO':([0,3,6,29,38,56,75,78,80,81,83,85,88,90,91,92,94,96,],[9,9,-6,-24,-23,-17,-4,-18,9,9,-5,9,-16,-20,-21,-19,9,-22,]),'IDENTIFICADOR':([0,3,4,6,7,8,9,11,14,18,19,20,22,23,29,30,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56,75,77,78,80,81,83,85,88,90,91,92,94,96,],[5,5,17,-6,-7,-8,-9,21,28,28,28,28,28,28,-24,28,-23,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-17,-4,28,-18,5,5,-5,5,-16,-20,-21,-19,5,-22,]),'IMPRIME':([0,3,6,29,38,56,75,78,80,81,83,85,88,90,91,92,94,96,],[10,10,-6,-24,-23,-17,-4,-18,10,10,-5,10,-16,-20,-21,-19,10,-22,]),'FUNCAO':([0,3,6,29,38,56,75,78,80,81,83,85,88,90,91,92,94,96,],[11,11,-6,-24,-23,-17,-4,-18,11,11,-5,11,-16,-20,-21,-19,11,-22,]),'ENQUANTO':([0,3,6,29,38,56,75,78,80,81,83,85,88,90,91,92,94,96,],[12,12,-6,-24,-23,-17,-4,-18,12,12,-5,12,-16,-20,-21,-19,12,-22,]),'SE':([0,3,6,29,38,56,75,78,80,81,83,85,88,90,91,92,94,96,],[13,13,-6,-24,-23,-17,-4,-18,13,13,-5,13,-16,-20,-21,-19,13,-22,]),'RETORNA':([0,3,6,29,38,56,75,78,80,81,83,85,88,90,91,92,94,96,],[14,14,-6,-24,-23,-17,-4,-18,14,14,-5,14,-16,-20,-21,-19,14,-22,]),'CORTE':([0,3,6,29,38,56,75,78,80,81,83,85,88,90,91,92,94,96,],[15,15,-6,-24,-23,-17,-4,-18,15,15,-5,15,-16,-20,-21,-19,15,-22,]),'$end':([1,2,3,6,16,29,38,56,75,78,83,88,90,91,92,96,],[0,-1,-3,-6,-2,-24,-23,-17,-4,-18,-5,-16,-20,-21,-19,-22,]),'FECHA_CHAVE':([3,6,16,29,38,56,75,78,83,86,87,88,89,90,91,92,95,96,],[-3,-6,-2,-24,-23,-17,-4,-18,-5,90,91,-16,92,-20,-21,-19,96,-22,]),'ABRE_COLCHETE':([5,17,28,],[18,31,52,]),'ATRIBUIR':([5,17,24,25,26,27,28,32,33,34,36,37,53,55,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[19,30,51,-10,-11,-12,-13,51,51,51,51,51,51,77,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-39,51,]),'ABRE_PARENTESE':([10,12,13,21,],[20,22,23,35,]),'NUMERO':([14,18,19,20,22,23,30,31,39,40,41,42,43,44,45,46,47,48,49,50,51,52,77,],[25,25,25,25,25,25,25,54,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'FLUTUANTE':([14,18,19,20,22,23,30,39,40,41,42,43,44,45,46,47,48,49,50,51,52,77,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'TEXTO':([14,18,19,20,22,23,30,39,40,41,42,43,44,45,46,47,48,49,50,51,52,77,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'PONTO_E_VIRGULA':([15,24,25,26,27,28,33,53,57,61,62,63,64,65,66,67,68,69,70,71,72,73,76,82,84,],[29,38,-10,-11,-12,-13,56,75,78,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,83,-39,88,]),'MENOR':([24,25,26,27,28,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[39,-10,-11,-12,-13,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-39,39,]),'MAIOR':([24,25,26,27,28,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[40,-10,-11,-12,-13,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-39,40,]),'MENOR_IGUAL':([24,25,26,27,28,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[41,-10,-11,-12,-13,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-39,41,]),'MAIOR_IGUAL':([24,25,26,27,28,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[42,-10,-11,-12,-13,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-39,42,]),'IGUAL':([24,25,26,27,28,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[43,-10,-11,-12,-13,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-39,43,]),'DIFERENTE':([24,25,26,27,28,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[44,-10,-11,-12,-13,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-39,44,]),'SOMA':([24,25,26,27,28,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[45,-10,-11,-12,-13,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-39,45,]),'MENOS':([24,25,26,27,28,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[46,-10,-11,-12,-13,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-39,46,]),'MULTIPLICA':([24,25,26,27,28,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[47,-10,-11,-12,-13,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-39,47,]),'DIVIDE':([24,25,26,27,28,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[48,-10,-11,-12,-13,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-39,48,]),'>':([24,25,26,27,28,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[49,-10,-11,-12,-13,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-39,49,]),'<':([24,25,26,27,28,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,84,],[50,-10,-11,-12,-13,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-39,50,]),'FECHA_COLCHETE':([25,26,27,28,32,54,61,62,63,64,65,66,67,68,69,70,71,72,73,74,82,],[-10,-11,-12,-13,55,76,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,82,-39,]),'FECHA_PARENTESE':([25,26,27,28,34,35,36,37,61,62,63,64,65,66,67,68,69,70,71,72,73,82,],[-10,-11,-12,-13,57,58,59,60,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,]),'DOIS_PONTOS':([58,],[79,]),'ABRE_CHAVE':([59,60,79,93,],[80,81,85,94,]),'SE_NAO':([91,],[93,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaracoes':([0,3,80,81,85,94,],[2,16,86,87,89,95,]),'declaracao':([0,3,80,81,85,94,],[3,3,3,3,3,3,]),'tipo':([0,3,80,81,85,94,],[4,4,4,4,4,4,]),'comando':([0,3,80,81,85,94,],[6,6,6,6,6,6,]),'expressao':([14,18,19,20,22,23,30,39,40,41,42,43,44,45,46,47,48,49,50,51,52,77,],[24,32,33,34,36,37,53,61,62,63,64,65,66,67,68,69,70,71,72,73,74,84,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> declaracoes','programa',1,'p_programa','parser.py',16),
  ('declaracoes -> declaracao declaracoes','declaracoes',2,'p_declaracoes','parser.py',20),
  ('declaracoes -> declaracao','declaracoes',1,'p_declaracoes','parser.py',21),
  ('declaracao -> tipo IDENTIFICADOR ATRIBUIR expressao PONTO_E_VIRGULA','declaracao',5,'p_declaracao','parser.py',28),
  ('declaracao -> tipo IDENTIFICADOR ABRE_COLCHETE NUMERO FECHA_COLCHETE PONTO_E_VIRGULA','declaracao',6,'p_declaracao','parser.py',29),
  ('declaracao -> comando','declaracao',1,'p_declaracao','parser.py',30),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','parser.py',42),
  ('tipo -> FLUTUANTE_TIPO','tipo',1,'p_tipo','parser.py',43),
  ('tipo -> TEXTO_TIPO','tipo',1,'p_tipo','parser.py',44),
  ('expressao -> NUMERO','expressao',1,'p_expressao','parser.py',48),
  ('expressao -> FLUTUANTE','expressao',1,'p_expressao','parser.py',49),
  ('expressao -> TEXTO','expressao',1,'p_expressao','parser.py',50),
  ('expressao -> IDENTIFICADOR','expressao',1,'p_expressao','parser.py',51),
  ('comandos -> comandos comando','comandos',2,'p_comandos','parser.py',54),
  ('comandos -> comando','comandos',1,'p_comandos','parser.py',55),
  ('comando -> IDENTIFICADOR ABRE_COLCHETE expressao FECHA_COLCHETE ATRIBUIR expressao PONTO_E_VIRGULA','comando',7,'p_comando','parser.py',63),
  ('comando -> IDENTIFICADOR ATRIBUIR expressao PONTO_E_VIRGULA','comando',4,'p_comando','parser.py',64),
  ('comando -> IMPRIME ABRE_PARENTESE expressao FECHA_PARENTESE PONTO_E_VIRGULA','comando',5,'p_comando','parser.py',65),
  ('comando -> FUNCAO IDENTIFICADOR ABRE_PARENTESE FECHA_PARENTESE DOIS_PONTOS ABRE_CHAVE declaracoes FECHA_CHAVE','comando',8,'p_comando','parser.py',66),
  ('comando -> ENQUANTO ABRE_PARENTESE expressao FECHA_PARENTESE ABRE_CHAVE declaracoes FECHA_CHAVE','comando',7,'p_comando','parser.py',67),
  ('comando -> SE ABRE_PARENTESE expressao FECHA_PARENTESE ABRE_CHAVE declaracoes FECHA_CHAVE','comando',7,'p_comando','parser.py',68),
  ('comando -> SE ABRE_PARENTESE expressao FECHA_PARENTESE ABRE_CHAVE declaracoes FECHA_CHAVE SE_NAO ABRE_CHAVE declaracoes FECHA_CHAVE','comando',11,'p_comando','parser.py',69),
  ('comando -> RETORNA expressao PONTO_E_VIRGULA','comando',3,'p_comando','parser.py',70),
  ('comando -> CORTE PONTO_E_VIRGULA','comando',2,'p_comando','parser.py',71),
  ('bloco -> ABRE_CHAVE comandos FECHA_CHAVE','bloco',3,'p_bloco','parser.py',117),
  ('expressao -> expressao MENOR expressao','expressao',3,'p_expressao_relacional','parser.py',121),
  ('expressao -> expressao MAIOR expressao','expressao',3,'p_expressao_relacional','parser.py',122),
  ('expressao -> expressao MENOR_IGUAL expressao','expressao',3,'p_expressao_relacional','parser.py',123),
  ('expressao -> expressao MAIOR_IGUAL expressao','expressao',3,'p_expressao_relacional','parser.py',124),
  ('expressao -> expressao IGUAL expressao','expressao',3,'p_expressao_relacional','parser.py',125),
  ('expressao -> expressao DIFERENTE expressao','expressao',3,'p_expressao_relacional','parser.py',126),
  ('expressao -> expressao SOMA expressao','expressao',3,'p_expressao_binaria','parser.py',132),
  ('expressao -> expressao MENOS expressao','expressao',3,'p_expressao_binaria','parser.py',133),
  ('expressao -> expressao MULTIPLICA expressao','expressao',3,'p_expressao_binaria','parser.py',134),
  ('expressao -> expressao DIVIDE expressao','expressao',3,'p_expressao_binaria','parser.py',135),
  ('expressao -> expressao > expressao','expressao',3,'p_expressao_binaria','parser.py',136),
  ('expressao -> expressao < expressao','expressao',3,'p_expressao_binaria','parser.py',137),
  ('expressao -> expressao ATRIBUIR expressao','expressao',3,'p_expressao_binaria','parser.py',138),
  ('expressao -> IDENTIFICADOR ABRE_COLCHETE expressao FECHA_COLCHETE','expressao',4,'p_expressao_vetor','parser.py',145),
]
