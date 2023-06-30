def encontrar_max_min(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

numeros = [10, 5, 8, 3, 9]
maximo, minimo = encontrar_max_min(numeros)
print("Máximo:", maximo)    
print("Mínimo:", minimo)    
