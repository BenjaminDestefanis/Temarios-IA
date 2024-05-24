"""
BREVE TEORIA

1. VECTORES Y ESPACIOS VECTORIALES

VECTOR: entidad matematica que tiene magnitud y direccion. En el contexto de
algebra lineal, se representa como un arreglo ordenado de numeros(Componentes)

EJ. : V = [v1, v2, ..., vn] en Rn 
    Vector      Componentes       R = puede representar espacio vectorial o dimesnion del vector

Operaciones con Vectores

Suma : U + V = [u1 + v1, u2 + u2, ..., un + vn]

MULTIPLICACION POR UN ESCALAR 

En el álgebra lineal, un escalar es un número real que se utiliza para multiplicar vectores. Los escalares no tienen dirección ni magnitud, solo un valor numérico.

EJ. : C * V = [c * V1, c * v2, ..., c * vn]
C = Escalar


RESTA : U - V = [u1 - v1, u2 - v2, ..., un - vn]


1.2 ESPACIOS VECTORIALES Y SUBESPACIOS

Un espacio vectorial es un copnjunto de vectores que se pueden sumar entre si, pueden multiplicar por escalares y cumplen ciertas propiedades

"""

# EJERCICIOS

#1. Calculo de magnitud y direccion de un vector : 
# Tenemos un vector (v = [2, -3, 4]). Debemos calcular la magnitud (modulo) y la direccion del vector.
# Sea otro vector (u = [-1, 5, 2] ). Debemos calcular el angulo entre u y el eje positivo.


#2. Verificacion de subespacio
# Recibiremos un conjunto de vectores en R^3, la funcion debe ferificar si estos forman un subespacio
# TIPS: Un conjunto de vectorers jforma un sibespacio si cumple con 3 condiciones:
# A. El Vector 0 esta en el conjunto. B.Esta cerrado bajo la suma de vectores. C. Esta cerrado bajo la multiplicacion por escalares

# SOLUCION [Recordad que las soluciones deben estar en otro documento]

# C

import numpy as np

def is_subspace(vectors):
    # Verificar si el vector cero está en el conjunto
    zero_vector = np.zeros_like(vectors[0])
    if not any((vector == zero_vector).all() for vector in vectors):
        return False

    # Verificar la cerradura bajo la suma de vectores
    for v1 in vectors:
        for v2 in vectors:
            if not any((v1 + v2 == v).all() for v in vectors):
                return False

    # Verificar la cerradura bajo la multiplicación por escalares
    for v in vectors:
        for scalar in range(-10, 10):
            if not any((scalar * v == v2).all() for v2 in vectors):
                return False

    return True
