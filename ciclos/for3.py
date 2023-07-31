def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores
try:
    numero = int(input("Ingrese un número entero: "))
    if numero <= 0:
        print("Por favor, ingrese un número entero positivo.")
    else:
        resultado = encontrar_divisores(numero)
        print(f"Los divisores de {numero} son: {resultado}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
