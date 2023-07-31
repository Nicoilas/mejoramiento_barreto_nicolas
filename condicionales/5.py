def encontrar_valor_medio(num1, num2, num3):
   
    lista_numeros = [num1, num2, num3]

    if lista_numeros[0] > lista_numeros[1]:
        lista_numeros[0], lista_numeros[1] = lista_numeros[1], lista_numeros[0]
    if lista_numeros[0] > lista_numeros[2]:
        lista_numeros[0], lista_numeros[2] = lista_numeros[2], lista_numeros[0]

    if lista_numeros[1] > lista_numeros[2]:
        lista_numeros[1], lista_numeros[2] = lista_numeros[2], lista_numeros[1]

    
    valor_medio = lista_numeros[1]

    return valor_medio

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

valor_medio = encontrar_valor_medio(num1, num2, num3)
print(f"El valor del medio es: {valor_medio}")