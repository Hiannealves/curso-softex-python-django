jogadores = {"Iza": 10,
             "Mary": 20,
             "Tonho": 15}

print(jogadores)

nome = input("Digite o nome do jogador: ")

if nome in jogadores:
    pontos = int(input("Digite o valor de pontos a adicionar: "))
    jogadores[nome] += pontos
    print(f"Pontos do Jogador atualizado. Novo valor de pontos {pontos}")

    if not nome in jogadores:
         nome = input("Digite o nome do novo jogador:  ")
         jogadores[nome] += jogadores
         jogadores[nome] = 0 
         print(f"Jogador Cadastrado com sucesso")

    else:
         print("Digite um nome válido!")     

print("Jogador"[nome])
print("Pontos"[pontos])