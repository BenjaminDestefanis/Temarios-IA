-- EJEMPLOS:

-- DELETE en SQL le ayuda a eliminar registros existentes de una base de datos. Sin embargo, !!!! tenga en cuenta que es una operación destructiva y puede borrar permanentemente datos de su base de datos !!!!.

-- 1.
DELETE FROM table_name;

-- La declaracion DELETE sin la clausula WHERE elimina todas las filas de una tabla. !! ESTA OPERACION ES IRREVERSIBLE!!!

-- 2.
DELETE FROM table_name WHERE condition;

-- Con la clausula WHERE, la declaracion DELETE borra filas especificas que cumplan con la condicion.

-- Es fundamental usarlo DELETEcon precaución porque tiene el potencial de borrar ciertas filas importantes o vaciar completamente la tabla.

-- Nota: La eliminación realizada mediante la declaración "DELETE" es permanente y no se puede deshacer. Asegúrese siempre de tener una copia de seguridad antes de ejecutar una consulta DELETE, especialmente cuando está en una base de datos de producción.