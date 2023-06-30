def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero = numero // 10
    return suma

print(suma_digitos(12345))    
print(suma_digitos(9876))     
