# modulos/assembly.py
class GeradorAssembly:
    def __init__(self, codigo_tac):
        self.codigo_tac = codigo_tac
        self.codigo_asm = []

    def gerar(self):
        for linha in self.codigo_tac:
            if linha.startswith("func "):
                nome = linha.split()[1][:-1]
                self.codigo_asm.append(f"{nome}:")
            elif linha.startswith("endfunc"):
                self.codigo_asm.append("")  # Espaço entre funções
            elif " = " in linha:
                dest, expr = linha.split(" = ", 1)
                self.codigo_asm.append(f"MOV {dest}, {expr}")
            elif linha.startswith("print"):
                _, valor = linha.split(" ", 1)
                self.codigo_asm.append(f"PRINT {valor}")
            elif linha.startswith("return"):
                _, valor = linha.split(" ", 1)
                self.codigo_asm.append(f"RET {valor}")
            elif linha.startswith("if_false"):
                # Exemplo: if_false t1 goto L1
                _, cond, _, label = linha.split()
                self.codigo_asm.append(f"CMP {cond}, 0")
                self.codigo_asm.append(f"JE {label}")
            elif linha.startswith("goto"):
                _, label = linha.split()
                self.codigo_asm.append(f"JMP {label}")
            elif linha.endswith(":"):
                self.codigo_asm.append(linha)
            elif linha.startswith("call"):
                _, nome_funcao = linha.split()
                self.codigo_asm.append(f"CALL {nome_funcao}")
            else:
                self.codigo_asm.append(f"; [TAC não reconhecido] {linha}")

    def imprimir(self):
        print("\n=== CÓDIGO ASSEMBLY ===")
        for linha in self.codigo_asm:
            print(linha)
        print("========================\n")
