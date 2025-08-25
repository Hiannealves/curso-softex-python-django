"""
Programa de banco
1-rodar loop infinito
2-ter conta e senha
3-encerrar sessão
4-cheque especial (limite de saldo negativo)
5- tentar 3 vezes a senha
6-opções (saque, deposito, transferencia)
7-mostrar saldo apos saque
8-alterar senha
9- boas vindas ao usuário 
10-pagar boleto
"""
# criar variavel definindo usuario e senha
cc = "123456-7" 
senha_usuário = "9999"
nome_de_usuário=("José")
saldo_atual = 0
limite_de_saque_negativo = 500

while True:
    for i in range(3)
         conta = input("Digite sua Conta corrente")
         senha = input("Digite sua senha")
         if conta==cc and senha==senha_usuário:
            print(f"Seja Bem vindo{nome_de_usuário}")
            acesso_permitido = True
            break
         else:
            print("Usuário ou senha inválido")
            acesso_permitido = False
    
    if not acesso_permitido:
        break         

    while True:
            opcao = input("Escolha uma opção:\n"\
            "1- Ver saldo.\n" \
            "2- Sacar Valor.\n" \
            "3- Depositar.\n" \    
            "4- Pagar Boleto.\n" \
            "5- Alterar senha.\n" \
            "6- Sair.\n")

            if opcao == "1":
                print(f"Seu saldo Atual é{saldo_atual},")

            elif opcao == "2":
                 valor_a_sacar = float(input("Digite o valor a ser sacado:"))
                 if valor_a_sacar<=(saldo_atual + limite_de_saque_negativo):
                     saldo-=valor_a_sacar
                     print("Saldo liberado, retire suas cédulas!")
                 else:
                     print("Saldo insuficiente")    

            elif opcao == "3":
                 depositar = float(input("Digite o valor a ser depositado"))
                 if depositar >0:
                     saldo += depositar
            else:
                print("Valor Inválido!")      
                  
            elif opcao == "4":
                boleto=float(input("Entre com o valor do boleto:"))
                if boleto <(saldo_atual+ limite_de_saque_negativo):
                    saldo-=boleto
                else:
                    print("Saldo insuficiente.")

            elif opcao == "5":
                senha_antiga = input("Digite sua senha antiga:")
                senha_nova1 = input("Digite sua nova senha:")
                senha_nova2 = input("Confirme sua nova senha:")
                if senha_antiga == senha_usuário and senha_nova1==senha_nova2:
                    senha_usuário=senha_nova1
                    print("Senha atuaizada com sucesso!")
                else:
                    print("Senha inválida") 
                                    
            elif opcao == "6":
               print("Atendimento Finalizado")
               break
            else:
                print("Opção inválida!")