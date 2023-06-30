def calcular_area(figura, lado1, lado2=None):
    if figura == "triangulo":
        return (lado1 * lado2) / 2
    elif figura == "cuadrado":
        return lado1 ** 2

print(calcular_area("triangulo", 4, 6))    
print(calcular_area("cuadrado", 5))        
