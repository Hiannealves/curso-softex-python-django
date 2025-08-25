""" EX 3 MENU DE COMANDOS PARA UM ROBÔ
CRIE UM PROGRAMA QUE SIMULA O CONTROLE DE UM ROBÔ SIMPLES COM UM MENU DE COMANDOS.
1 O ROBO PODE ESTAR EM UMA POSIÇÃO INICIAL(VOCê PODE USAR UMA VARIÁVEL PARA ISSO, POR EXEMPLO , A POSIÇÃO 0)
2 O PROGRAMA DEVE EXIBIR UM MENU COM AS SEGUINTE OPÇÕES:
    1 AVANÇAR
    2 RECUAR
    3 STATUS
    4 DESLIGAR
3 PEÇA AO USUARIO PARA ESCOLHER UM COMANDO:
4 COM BASE NA ESCOLHA , EXECUTE A AÇÃO CORRESPONDENTE:
    * AVANÇAR : ADICIONE UM VALOR A POSIÇÃO DO ROBÔ.
    * RECUAR : SUBTRAIA UM VALOR DA POSIÇÃO DO ROBÔ.
    * STATUS : MOSTRE A POSIÇÃO ATUAL DO ROBÔ.
    * DESLIGAR : ENCERRE O PROGRAMA.
5 O MENU DEVE CONTINUAR APARECENDO APÓS CADA COMANDO, ATÉ QUE O USUARIO ESCOLHA A OPÇÃO DESLIGAR.
6 SE O USUÁRIO DIGITAR UM COMANDO INVÁLIDO, EXIBA MENSAGEM DE ERRO."""

posicao = 0

while True:
    print(" Menu do Robô :) ")
    opcao=input("Escolha uma ação:\n"
            "1- Avançar\n" 
            "2- Recuar\n" 
            "3- Status\n"    
            "4- Desligar\n")

    if opcao == "1":
        posicao+=1
        print("Robô: Você avançou!" , posicao)

    elif opcao == "2":
        posicao-=1
        print("Robô: Você recuou!" , posicao) 

    elif opcao == "3":
        print(" Posição atual", posicao)

    elif opcao == "4":
        print("Robô: Sistema desligado, até breve!") 
        break 

    else:
        print("Opção inválida")             

