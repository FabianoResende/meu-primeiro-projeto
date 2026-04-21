import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_lowercase

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += "!@#$%&*?"

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== Gerador de Senhas Seguras ===")
    tamanho = int(input("Digite o tamanho da senha (ex: 12): "))
    senha = gerar_senha(tamanho)
    print(f"\nSua senha gerada é:\n{senha}")

if __name__ == "__main__":
    main()
