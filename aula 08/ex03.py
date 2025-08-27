"""Codificar e decodificar frases
CRIE UM PROGRAMA QUE CODIFICA E DECODIFICA UMA FRASE, SEGUINDO AS REGRAS ABAIXO:
CADA VOGAL DEVE SER SUBSTITUIDA PELO NÚMERO CORRESPOMDENTE
A 1
E 2
I 3
O 4 
U 5 
O PROGRAMA DEVE :
1 LER UMA FRASE DIGITADA PEO USUARIO
2 EXIBIR FRASE CODIFICADA, TROCANDO AS VOGAIS POR NUMEROS
3 EXIBIR FRASE DECODIFICADA, TROCANDO NUMERO POR VOGAIS ORIGINAIS.

"""
frase = input("Digite uma frase").lower()

codificada = frase.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5") 
decodificada = codificada.replace("1","a").replace("2","e").replace("3","i").replace("4","o").replace("5","u") 
print(codificada)       
print(decodificada)    