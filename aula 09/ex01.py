"""CONTANDO OCORRÊNCIAS"""
#CRIE UM PROGRAMA QUE CONTEM QUANTAS VEZES UM NÚMERO ESPECÍFICO APARECE NA LISTA.
#ENTRADA: UMA LISTA DE NÚMEROS PARA SER PROCURADA.
#SAÍDA: UM NÚMERO INTEIRO QUE REPRESENTA A QUANTIDADE DE VEZES QUE O NÚMERO PROCURADO APARECE NA LISTA.

numero = [2,5,6,9,4,8,9,4,9]
numero_procurado = 9
contador = 0

for num in numero: 
    if num == numero_procurado:
        contador+=1

print("O número aparece",contador, "vezes!")