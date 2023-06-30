def tiene_duplicados(lista):
    if len(lista) != len(set(lista)):
        return True
    else:
        return False

print(tiene_duplicados([1, 2, 3, 4, 5]))        
print(tiene_duplicados([1, 2, 3, 2, 4, 5]))