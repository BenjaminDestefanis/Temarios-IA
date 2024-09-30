#1 Numero par o impar
def es_par(n):
    # Tu codigo aqui : 
    # return n % 2 == 0
    return 0

#2 Es polindromo ?
def es_palindromo(cadena):
    return cadena == cadena[::-1]

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 4 Conteo de palabras

def contar_palabras(cadena):
    return len(cadena.split())

