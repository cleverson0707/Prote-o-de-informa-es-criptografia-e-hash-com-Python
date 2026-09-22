import os

def calcula_hash(palavra):
    """Gera um hash numérico simples baseado na soma dos caracteres e suas posições."""
    hash_resultado = 0
    for indice, letra in enumerate(palavra):
        hash_resultado += ord(letra) * (indice + 1)  # Multiplica pela posição para evitar colisões simples (ex: amor/roma)
    return hash_resultado

def codifica(texto, chave):
    """Criptografa letras minúsculas, maiúsculas e números usando deslocamento."""
    resultado = ""
    for letra in texto:
        if "a" <= letra <= "z":
            posicao = ord(letra) - ord("a")
            nova_posicao = (posicao + chave) % 26
            resultado += chr(nova_posicao + ord("a"))
        elif "A" <= letra <= "Z":
            posicao = ord(letra) - ord("A")
            nova_posicao = (posicao + chave) % 26
            resultado += chr(nova_posicao + ord("A"))
        elif "0" <= letra <= "9":
            posicao = ord(letra) - ord("0")
            nova_posicao = (posicao + chave) % 10
            resultado += chr(nova_posicao + ord("0"))
        else:
            resultado += letra
    return resultado

def decodifica(texto, chave):
    """Decodifica o texto aplicando o deslocamento inverso."""
    return codifica(texto, -chave)

def menu():
    while True:
        print("\n" + "="*30)
        print(" 🔐 COFRE DIGITAL & CIPHER 🔐")
        print("="*30)
        print("[1] Criptografar Mensagem/Senha")
        print("[2] Descriptografar Mensagem/Senha")
        print("[3] Gerar Assinatura Digital (Hash)")
        print("[4] Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            texto = input("Digite o texto a ser protegido: ")
            chave = int(input("Digite a chave numérica de deslocamento: "))
            resultado = codifica(texto, chave)
            print(f"\n🔒 Texto Criptografado: {resultado}")
            
        elif opcao == "2":
            texto = input("Digite o texto criptografado: ")
            chave = int(input("Digite a chave original de deslocamento: "))
            resultado = decodifica(texto, chave)
            print(f"\n🔓 Texto Descriptografado: {resultado}")
            
        elif opcao == "3":
            texto = input("Digite a palavra para gerar o Hash de integridade: ")
            print(f"\n🔢 Hash gerado: {calcula_hash(texto)}")
            
        elif opcao == "4":
            print("\nFechando o cofre digital. Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
