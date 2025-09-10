lass Aluno:
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