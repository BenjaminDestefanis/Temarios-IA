import numpy as np
import colorama
colorama.init()

f = colorama.Fore
rs = colorama.Style.RESET_ALL
 
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

print(f"{f.MAGENTA}ZEROS: {rs}{zeros} \n")

# Array de unos - ones(cant. de arrays, cant. de valores)
ones = np.ones((3, 3))

print(f"{f.MAGENTA}ONES: {rs}{ones} \n")

# Array con valores aleatorios - rand(cant. de arrays, cant. de valores)
random = np.random.rand(2, 2)

print(f"{f.MAGENTA}RANDOM: {rs}{random} \n " )

# Array con un rango de valores - range_array(numero inicial, numero final, intervalo)
range_array = np.arange(0, 10, 3)

print(f"{f.MAGENTA}RANGE ARRAY: {rs}{range_array} \n")

# Array con valores equidistantes - profuncdizar
linspace_array = np.linspace(0, 1, 5)

print(f"{f.MAGENTA}LINSPACE ARRAY: {rs}{linspace_array} \n")


#  Experiemtando con Arrays - TENER EN CUENTA - LOS ARRAYS SON MUTABLES

my_array = np.array([1,2,3,4,5,6])
print(f"{f.CYAN}ARRAY:{rs}{my_array} \n")
my_array[2] = 50
print(f"{f.CYAN}ARRAY:{rs}{my_array} \n")

second_array = my_array[2:4]
print(f"{f.GREEN}SECOND ARRAY:{rs}{second_array} \n")
second_array[1] = 94
print(f"{f.GREEN}SECOND ARRAY:{rs}{second_array} \n")

# El cambio del segundo array, llega a alterar el primero array

print(f"{f.CYAN}ARRAY:{rs}{my_array} \n")

# ATRIBUTOS DE ARRAY

a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(a)
numero_de_dimensiones = a.ndim  # Retorna el numero de dimensiones (Profundidad)
print(f"{f.BLUE}{numero_de_dimensiones}{rs}")




