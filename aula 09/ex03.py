numeros = [1,2,3,4,5,6,7,8,9]
primos = []

for num in numeros:
    eh_primo = True
    if num < 2:
        eh_primo = False
    else:
        for i in range (2, num):
            if num % i == 0:
              eh_primo = False
              break
    if eh_primo:                       
     primos.append(num)

print(primos)                                                                                                                                                                                                                                                                                                                                                        