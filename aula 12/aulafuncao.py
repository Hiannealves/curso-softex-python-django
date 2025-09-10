def diga_oi():
    print("Oi! Tudo bem.")

diga_oi()

def sauda_com_idade(nome:str, idade:int):
    """tipagem, boas praticas explicar o que minha função faz"""
    print(f"Olá {nome}, você tem {idade}!")

sauda_com_idade("anderson", 42)

def exibir_pedido(item: str, *extras: str, **observacoes: str) -> None:
    print(f"Item Principal: {item}")
    print(f"Extras: {extras}")
    print(f"Observações: {observacoes}")


exibir_pedido( "Pizza","Queijo extra","Bacon", borda="recheada", ingrediente="tomate")

"""Conceito
Palavra-chave/Símbolo
O que faz?
Definir Função
def
Cria uma função.

Chamar Função
nome ()
Executa a função.

Devolver Valor
return
Devolve um valor e encerra a função.

Args Variáveis
*
Empacota argumentos em uma tupla.

Kwargs Variáveis
**
Empacota argumentos nomeados em um dicionário.

Função Anônima
lambda
Cria uma função de uma linha."""