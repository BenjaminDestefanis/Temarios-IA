-- EJEMPLOS

-- 1.
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

-- Aqui se especifica tanto los nombres de las columnas como los valores que se insertarán.


-- 2.
INSERT INTO table_name
SET column1 = value1, column2 = value2, ...;

-- Con la palabra reservada SET , especificamos la culumna, y el valor para la columna

-- 3.
INSERT INTO table_name1 (col1, col2, col3, ...)
SELECT col1, col2, col3, ...
FROM table_name2
WHERE condition;

-- Aqui el SELECT se utiliza para selecionar datos de otra tabla, para insertarlos en otra tabla

-- En todos los casos, si inserta datos en una tabla donde algunas columnas tienen valores predeterminados, no necesita especificar esas columnas en su INSERT INTOdeclaración.

-- Nota: tenga cuidado al insertar datos en una base de datos ya que SQL no tiene un comando de confirmación. Entonces, una vez que ejecuta la instrucción de inserción, los registros se insertan y no puede deshacer la operación.