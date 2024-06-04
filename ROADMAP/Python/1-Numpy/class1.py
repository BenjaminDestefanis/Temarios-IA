import numpy as np

# Estos array tambien se los conoce como vectores.
# Creacion de Array unifimensional.

vector_unidimensional = np.array([1,2,3,4,5])

# Array bidimensional

vector_bidimensional = np.array([[1,2,3], [4,5,6]])

# Array tridimensional

vector_tridimensional = np.array([[[1,2,3], [4,5,6]],[[7,8,9], [10,11,12]]])

print('Vector unidiemsional: ', vector_unidimensional,
      'Vector bidimensional:', vector_bidimensional,
      'Vector tridimensional', vector_tridimensional)


# Funciones o metodos array en NUMPY

# Array de ceros - zeros(cant. de arrays, cant. de valores)
zeros = np.zeros((2, 3))

print("'ZEROS:'", zeros)

# Array de unos - ones(cant. de arrays, cant. de valores)
ones = np.ones((3, 3))

print("'ONES:'", ones)

# Array con valores aleatorios - rand(cant. de arrays, cant. de valores)
random = np.random.rand(2, 2)

print("'RAND:'", random)

# Array con un rango de valores - range_array(numero inicial, numero final, intervalo)
range_array = np.arange(0, 10, 3)

print("'RANGE ARRAY:'", range_array)

# Array con valores equidistantes - profuncdizar
linspace_array = np.linspace(0, 1, 5)

print("'LINSPACE ARRAY:'", linspace_array)
