/* SQL emplea una serie de palabras clave de comando estándar que son esenciales para interactuar con las bases de datos. Las palabras clave en SQL proporcionan instrucciones sobre qué acción se debe realizar. */

Estas son algunas de las principales palabras clave de SQL:

SELECT : esta palabra clave recupera datos de una base de datos. Por ejemplo,

SELECT * FROM Customers;

-- En la declaración anterior '*' se indica que todos los registros deben recuperarse de la tabla Customers.

-- FROM : Se utiliza junto con SELECT para especificar la tabla de la que recuperar datos.

-- WHERE : Se utiliza para filtrar registros. Al incorporar una cláusula WHERE, puede especificar las condiciones que deben cumplirse. Por ejemplo,

SELECT * FROM Customers WHERE Country='Germany';

-- INSERT INTO : este comando se utiliza para insertar nuevos datos en una base de datos.

INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal','Tom B. Erichsen','Skagen 21','Stavanger','4006','Norway');

-- UPDATE : esta palabra clave actualiza los datos existentes dentro de una tabla. Por ejemplo,

UPDATE Customers SET ContactName='Alfred Schmidt', City='Frankfurt' WHERE CustomerID=1;

-- DELETE : este comando elimina uno o más registros de una tabla. Por ejemplo,

DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';

-- CREATE DATABASE : Como lo implica su nombre, esta palabra clave crea una nueva base de datos.

CREATE DATABASE mydatabase;

-- ALTER DATABASE , DROP DATABASE , CREATE TABLE , ALTER TABLE , DROP TABLE : Estas palabras clave se utilizan para modificar bases de datos y tablas.

-- Recuerde que SQL no distingue entre mayúsculas y minúsculas, lo que significa que las palabras clave se pueden escribir en minúsculas. La convención es escribirlos TODO EN MAYÚSCULAS para facilitar la lectura. Hay muchas más palabras clave en SQL, pero estas son algunas de las más comunes.

-- TUTOTIALES EXTRA

https://mode.com/sql-tutorial
https://www.sqltutorial.org/