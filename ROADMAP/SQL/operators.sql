-- OPERADORES

-- Los operadores SQL se utilizan para realizar operaciones como comparaciones y cálculos aritméticos. Son muy importantes a la hora de formular consultas. Los operadores SQL se dividen en los siguientes tipos:

-- Operadores Aritméticos : Se utilizan para realizar operaciones matemáticas. Aquí hay una lista de estos operadores:

-- +: Suma
-- -: Resta
-- *: Multiplicación
-- /: División
-- %: Módulo
-- Ejemplo:

SELECT product, price, (price * 0.18) as tax
FROM products;

-- Operadores de comparación : se utilizan en la cláusula donde para comparar una expresión con otra. Algunos de estos operadores son:

-- = : Igual
-- != o <> : No igual
-- > : Mas grande que
-- < : Menos que
-- >= : Mayor que o igual
-- <= : Menor o igual
Ejemplo:

SELECT name, age
FROM students
WHERE age > 18;

-- Operadores lógicos : se utilizan para combinar el conjunto de resultados de dos condiciones de componentes diferentes. Éstas incluyen:

-- AND: Devuelve verdadero si ambos componentes son verdaderos.
-- OR: Devuelve verdadero si alguno de los componentes es verdadero.
-- NOT: Devuelve el valor booleano opuesto de la condición.

-- Ejemplo:

SELECT * 
FROM employees
WHERE salary > 50000 AND age < 30;

-- Bitwise Operators (Booleanos) : realizan operaciones a nivel de bits en las entradas. Aquí hay una lista de estos operadores:

-- &: AND
-- |: OR
-- ^: XOR

-- Los operadores bit a bit se utilizan con mucha menos frecuencia en SQL que otros tipos de operadores.

-- Recorda, el tipo de datos del resultado depende de los tipos de operandos.