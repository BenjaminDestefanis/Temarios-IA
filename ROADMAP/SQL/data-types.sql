-- TIPOS DE DATOS

-- Los tipos de datos SQL definen el tipo de datos que se pueden almacenar en la columna de una tabla de base de datos. Dependiendo del DBMS, los nombres de los tipos de datos pueden diferir ligeramente. 

-- INT
-- Numeros enteros. EJ:

CREATE TABLE Employees (
    ID INT,
    Name VARCHAR(30)
);

-- DECIMAL
-- Numeros decimales y fraccionarios. EJ:

CREATE TABLE Items (
    ID INT,
    Price DECIMAL(5,2)
);


-- CHAR
-- Cadenas de lonjitud fija. EJ:

CREATE TABLE Employees (
    ID INT,
    Initial CHAR(1)
);

-- VARCHAR
-- Cadenas de longitud variable. EJ:

CREATE TABLE Employees (
    ID INT,
    Name VARCHAR(30)
);

-- DATE
-- Para fechas con formato ( YYYY-MM-DD ). EJ:

CREATE TABLE Employees (
    ID INT,
    BirthDate DATE
);

-- DATETIME
--  Para valores de fecha y hora formato ( YYYY-MM-DD  HH:MI:SS ). EJ:

CREATE TABLE Orders (
    ID INT,
    OrderDate DATETIME
);


-- BINARY
-- Para cadenas Binarias.

-- BOOLEAN
-- Valores Booleanos (true o false)

-- Recorda , la sintaxis específica para crear tablas y definir tipos de datos de columnas puede variar ligeramente según la base de datos SQL que esté utilizando (MySQL, PostgreSQL, SQL Server, SQLite, Oracle, etc.), pero el concepto general y la organización de los tipos de datos son multiplataforma.

