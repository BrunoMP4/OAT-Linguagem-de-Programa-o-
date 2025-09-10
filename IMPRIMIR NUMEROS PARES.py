def imprimir_pares():
    for i in range(21):
        if i % 2 != 0:  # Se for ímpar, pula
            continue
        print(i, end=" ")
    print()  # quebra de linha

# ----------------------------
# 4) Classe Aluno com property
# ----------------------------
class Aluno:
    def __init__(self, nome, nota):
        self.__nome = nome
        self.__nota = None
        self.nota = nota  # usa o setter
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            raise ValueError("A nota deve estar entre 0 e 10.")