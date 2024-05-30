-- EJEMPLOS

-- UPDETE: Para actualizar dastos existente. Esta declaración es muy útil cuando necesita cambiar los valores asignados a campos específicos en una fila o conjunto de filas existente.

-- 1.
UPDATE table_name
SET col1 = val1, col2 = val2, ...
WHERE condition

-- table_name: El nombre de la tabla donde se realizará una actualización.
-- SET: Esta cláusula especifica el nombre de la columna y el nuevo valor al que debe actualizarse.
-- column1, column2, ...: Los nombres de las columnas de la tabla.
-- value1, value2, ...: Los nuevos valores que desea registrar en la base de datos.
-- WHERE: Esta cláusula especifica las condiciones que identifican qué filas actualizar.

-- A continuación se muestra un ejemplo que podría proporcionar cierta claridad. Para una Employeesmesa imaginaria:

/*  ID de empleado	    Nombre	    Posición	Salario
    1	                jane	    Gerente	    50000
    2	                John	    Oficinista	30000
    3	                Beto	    Ingeniero	40000 */
-- Si desea aumentar el salario de Bob en $5000, usaría:

UPDATE Employees
SET Salary = 45000
WHERE EmployeeID = 3;
-- Esto cambiaría permanentemente los datos de la Employeestabla:

/* ID de empleado	Nombre	Posición	Salario
1	jane	Gerente	50000
2	John	Oficinista	30000
3	Beto	Ingeniero	45000 */


-- !!!Tenga siempre cuidado con la declaracion UPDATE ; Si olvida la clausula WHERE , actualizará todas las filas de la tabla. !!! 