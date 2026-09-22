# 🔐 Secure Cipher & Hash Manager

Um utilitário em Python via linha de comando para criptografia, descriptografia e validação de integridade de dados (Hash). Este projeto simula um cofre digital focado no estudo de algoritmos de substituição e estruturas matemáticas básicas de segurança da informação.

## 🚀 Funcionalidades

- **Criptografia Avançada de César:** Protege dados manipulando independentemente letras minúsculas (`a-z`), maiúsculas (`A-Z`) e dados numéricos (`0-9`), sem corromper caracteres especiais ou espaços.
- **Descriptografia Dinâmica:** Desfaz o processo de cifragem utilizando chaves inversas de rotação.
- **Assinatura Digital (Hash):** Sistema de verificação de integridade que impede colisões simples por meio de pesos posicionais (`ord(letra) * posição`).

## 🛠️ Tecnologias Utilizadas

- **Python 3** (Lógica estrutural, tratamento de strings e aritmética modular)
- **Git & GitHub** (Controle de versão)

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o Python instalado na sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com
   ```
3. Acesse a pasta do projeto:
   ```bash
   cd gerenciador-mensagens-seguras
   ```
4. Execute o script:
   ```bash
   python main.py
   ```

## 🧠 Conceitos Aplicados

- **Função `ord()` e `chr()`:** Manipulação direta de caracteres com base na tabela ASCII.
- **Aritmética Modular (`%`):** Criação do efeito "carrossel" para que os limites do alfabeto e dos números nunca estourem.
- **Tratamento de Colisões:** Implementação de indexação forçada no loop de rotação para blindar o gerador de hashes contra anagramas básicos (ex: impedir que "amor" e "roma" retornem o mesmo resultado).
