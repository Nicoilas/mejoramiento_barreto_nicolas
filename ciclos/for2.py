def contar_pares(lista):
    contador = 0
    for num in lista:
        if num % 2 == 0:
            contador += 1
    return contador

print(contar_pares([1, 2, 3, 4, 5]))        
print(contar_pares([2, 4, 6, 8, 10]))       
