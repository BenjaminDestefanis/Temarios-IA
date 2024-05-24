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

# Con NUMPY

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

# Sin NUMPY 

def is_subspace(vectors):
    # Verificar si el vector cero está en el conjunto
    zero_vector = [0]*len(vectors[0])
    if not any(vector == zero_vector for vector in vectors):
        return False

    # Verificar la cerradura bajo la suma de vectores
    for v1 in vectors:
        for v2 in vectors:
            if not any(v1[i] + v2[i] == v[i] for i in range(len(v1)) for v in vectors):
                return False

    # Verificar la cerradura bajo la multiplicación por escalares
    for v in vectors:
        for scalar in range(-10, 10):
            if not any(scalar * v[i] == v2[i] for i in range(len(v)) for v2 in vectors):
                return False

    return True



# 3. Base de un Subespacio
# Recibimos un conjunto de vectores R^3 ,y la funcion debe encontrar una base para el subspacio que generan.
# TIP: Se puede utilizar el teorema de GRAM-SHMIDT
# El teorema de Gram-Schmidt asegura que dado un conjunto de vectores linealmente independientes en un espacio vectorial real con un producto interior dado, podemos encontrar otros vectores que ahora sean ortonormales, que generen lo mismo y que además «apunten hacia un lado similar» a los vectores originales

def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        w = v - sum(np.dot(v, b)*b for b in basis)
        if (w > 1e-10).any():  
            basis.append(w/np.linalg.norm(w))
    return np.array(basis)

# 4. Dimension de un subespacio
# Una ves mas recibimos un conjunto de vectores R^3. ya nuestra funcion debe encontrar el subespacio que generan. 
# TIP: La dimension de un subespacio es igual numero de vectores en su base. Aqui tambien debemos utilizar el algoritmo de GRAM-SCHMIDT para encontrar una base y luego contar el numero de vectores en ella.

def subspace_dimensions(vectors):
    basis = gram_schmidt(vectors)
    return len(basis)

# 5. Interseccion de subspacios
# Dados 2 subspacios en R^3, la funcion debe encontrar un vector que este en la interseccion de ambos, y si lo encuentra debe retornar el vector, si no debe retornar false.
# Nuestro algoritmo debe recorrer todos los vectores en el primer subspacio y verificar si tambien estan en el segundo subespacio

def interseccion(subspace1, subspace2):
    for v1 in subspace1:
        if any(v1 == v2 for v2 in subspace2):
            return v1
        else:
            return False
        

# 6. Suma directa de subspacios
# Recibiendo 2 subespacios en R^3, la funcion debe verificar si su suma es directa
# En caso de que sea dea directa , debe retornar True, caso contrario, retorna False
# TIPS: la suma de 2 subspacios es directa si la interseccion de ambos es solo el vector cero 
