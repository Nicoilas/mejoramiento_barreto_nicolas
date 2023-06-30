def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    if cadena == cadena[::-1]:
        return True
    else:
        return False

print(es_palindromo("anita lava la tina"))   
print(es_palindromo("hola mundo"))           
