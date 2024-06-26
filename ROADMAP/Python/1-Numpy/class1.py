import numpy as np
import colorama
colorama.init()

fore  = colorama.Fore
reset_style = colorama.Style.RESET_ALL
 
# Estos array tambien se los conoce como vectores.
# Creacion de Array unifimensional.

vector_unidimensional = np.array([1,2,3,4,5])

# Array bidimensional

vector_bidimensional = np.array([[1,2,3], [4,5,6]])

# Array tridimensional

vector_tridimensional = np.array([[[1,2,3], [4,5,6]],[[7,8,9], [10,11,12]]])

print( f"Vector unidiemsional: {vector_unidimensional} \n Vector bidimensional: {vector_bidimensional} \n Vector tridimensional: {vector_tridimensional} ")


# Funciones o metodos array en NUMPY

# Array de ceros - zeros(cant. de arrays, cant. de valores)
zeros = np.zeros((2, 3))

print(f"ZEROS: {zeros} \n")

# Array de unos - ones(cant. de arrays, cant. de valores)
ones = np.ones((3, 3))

print(f"ONES: {ones} \n")

# Array con valores aleatorios - rand(cant. de arrays, cant. de valores)
random = np.random.rand(2, 2)

print(f"{fore.MAGENTA}RANDOM: {reset_style}{random} \n " )

# Array con un rango de valores - range_array(numero inicial, numero final, intervalo)
range_array = np.arange(0, 10, 3)

print(f"RANGE ARRAY: {range_array} \n")

# Array con valores equidistantes - profuncdizar
linspace_array = np.linspace(0, 1, 5)

print(f"LINSPACE ARRAY: {linspace_array} \n")
