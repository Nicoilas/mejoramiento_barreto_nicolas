def verificar_signo(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"

print(verificar_signo(5))   
print(verificar_signo(-2))  
print(verificar_signo(0))   
