-- LENGUAJE DE DEFINICION DE DATOS (DDL)

-- Es un subconjunto de SQL. Su funcion principal es CREAR, MODIFICAR y ELIMINAR estructuras de bases de datos, PERO NO DATOS. Veamos sus comandos:

-- 1.CREATE

-- Para crear Baes de Datos o sus Objetos (EJ: Tablas, indices, funcion, vistas, procedimiento de almacenamiento y activadores)

CREATE TABLE table_name (
column1 data_type(size),
column2 data_type(size),
...
);

-- 2.DROPE

-- Para eliminar bases de datos o tablas existentes

DROP TABLE table_name;

-- 3.ALTER

ALTER TABLE table_name ADD column_name datatype;
ALTER TABLE table_name DROP COLUMN column_name;
ALTER TABLE table_name MODIFY COLUMN column_name datatype(size);

-- Para ALTERAR la estructura de la base de datos. Sirve para AGREGAR(ADD), ELIMINAR(DELETE-DROP) o MODIFICAR(MODIFY) columnas existentes.

-- 4.TRUNCATE

-- Sirve para eleminar todos los registros de una tabla, incluidos todos los espacios asignados para los registros que se eliminan.

-- 5.RENAME

-- To rename a table
ALTER TABLE table_name
RENAME TO new_table_name;

-- to rename a column
ALTER TABLE table_name
RENAME COLUMN name_colum TO new_column_name;

-- Para cambiar el nombre de un objeto en la base de datos.

-- Recuerde: en las operaciones DDL, las declaraciones COMMIT y ROLLBACK no se pueden realizar porque el motor MySQL confirma automáticamente los cambios.

-- Recuerde reemplazar table_name, column_name, datatype(size), old_table_namey new_table_nameen los ejemplos anteriores con los nombres reales de las tablas, los nombres de las columnas, los tipos y tamaños de datos, y los nombres de las tablas nuevas o antiguas que desee especificar.