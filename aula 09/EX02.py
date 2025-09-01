"encontrando elementos comuns"

lista_1 = ["azul"," amarelo","vermelho","verde"]
lista_2 = ["roxo", "azul", "laranja","vermelho"]

comuns = []
for item in lista_1:
    if item in lista_2 and item not in comuns:
        comuns.append(item)

print(comuns)