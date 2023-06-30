def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

funciones = {
    "suma": suma,
    "resta": resta,
    "multiplicacion": multiplicacion,
    "division": division
}
resultado = funciones["suma"](2, 3)
print(resultado)    

resultado = funciones["division"](10, 2)
print(resultado)    

resultado = funciones["resta"](7, 4)
print(resultado)    
