#Pedido de um hamburguer e uma lanchonete
"""1 defina o preço de um hambrguer.
2 defina um codigo de cupom de desconto
3 o programa deve pedir ao cliente o nome do produto repetidamente até que o produto
correto seja digitado
4 apos a escolha , o programa deve perguntar se o cliente 
tem um cupom de desconto
5 se o cliente digitar  cupom corretamente, aplique o desconto
6 calcule o preço final e exiba o total a pagar
7 o programa deve encerrar apos o pedido ser finalizado"""

lanche = "burguer"
burguer =10.99
cod_desconto = "BEMVINDO01"
desconto= burguer * 0.9

while True:
    pedido=input("Digite seu pedido")
    if pedido==lanche:
        break
    else:
        print("Digite um pedido válido. Tente novamente.")

codigo=input("Entre com seu codigo de desconto").upper()
if cod_desconto==codigo:
    print("O valor d seu pedido é R$ ",desconto)
else:
    print("O valor do seu pedido é R$" ,burguer)    
