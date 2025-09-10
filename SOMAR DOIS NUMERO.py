import hashlib

# ----------------------------
# 1) Programa que soma dois números
# ----------------------------
def somar_numeros():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        print(f"A soma é: {num1 + num2}")
    except ValueError:
        print("Por favor, digite apenas números inteiros.")