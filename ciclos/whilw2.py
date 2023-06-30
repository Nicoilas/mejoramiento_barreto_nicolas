def factorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

print(factorial(5))    
print(factorial(10))   
