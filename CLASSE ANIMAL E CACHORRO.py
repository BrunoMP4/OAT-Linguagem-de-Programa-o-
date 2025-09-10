class Animal:
    def falar(self):
        print("O animal fez um som.")

class Cachorro(Animal):
    def falar(self):
        print("Au Au")

# ----------------------------
# Executando cada parte
# ----------------------------
if __name__ == "__main__":
    print("1) Soma de números:")
    somar_numeros()
    
    print("\n2) Autenticação:")
    autenticar()
    
    print("\n3) Números pares de 0 a 20:")
    imprimir_pares()
    
    print("\n4) Classe Aluno:")
    aluno = Aluno("Bruno", 9)
    print(f"Aluno: {aluno.nome}, Nota: {aluno.nota}")
    
    print("\n5) Classes Animal e Cachorro:")
    animal = Animal()
    cachorro = Cachorro()
    animal.falar()
    cachorro.falar()