
def analisar_frase(frase):
    # Remove espaços extras
    frase = frase.strip()

    # Contagem de palavras
    palavras = frase.split()
    num_palavras = len(palavras)

 
    vogais = "aeiouáéíóúâêîôûãõAEIOUÁÉÍÓÚÂÊÎÔÛÃÕ"
    num_vogais = 0
    num_consoantes = 0

    for letra in frase:
        if letra.isalpha():
            if letra in vogais:
                num_vogais += 1
            else:
                num_consoantes += 1

    # Verifica se é palíndromo (ignora espaços e maiúsculas)
    frase_simplificada = ''.join(c.lower() for c in frase if c.isalnum())
    eh_palindromo = frase_simplificada == frase_simplificada[::-1]

    # Exibe o resultado
    print("\n--- Resumo da Análise ---")
    print(f"Palavras: {num_palavras}")
    print(f"Vogais: {num_vogais}")
    print(f"Consoantes: {num_consoantes}")
    print(f"É um palíndromo? {'Sim' if eh_palindromo else 'Não'}")


# execução
frase = input("Digite uma frase para analisar: ")
analisar_frase(frase)
