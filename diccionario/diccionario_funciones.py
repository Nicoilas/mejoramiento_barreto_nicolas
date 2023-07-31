a= int(input("ingrese un numero: "))
b= int(input("ingrese un numero: "))
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
resultado = funciones["suma"](a,b)
print(resultado)    

resultado = funciones["division"](a,b)
print(resultado)    

resultado = funciones["resta"](a,b)
print(resultado)    
