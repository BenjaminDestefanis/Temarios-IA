### QUE ES SQL?

#### BASES DE DATOS RELACIONALES

Una base de datos relacional es un tipo de base de datos que almacena y organiza datos de forma estructurada. Utiliza una estructura que permite identificar y acceder a los datos en relación con otros datos de la base de datos. Los datos de una base de datos relacional se almacenan en varias tablas de datos, cada una de las cuales tiene una clave única que identifica cada fila.

Las bases de datos relacionales se componen de un conjunto de tablas con datos que encajan en una categoría predefinida. Cada tabla tiene al menos una categoría de datos en una columna y cada fila contiene una determinada instancia de datos para las categorías definidas en las columnas.

#### RELACIONES

El término "base de datos relacional" proviene del concepto de relación: un conjunto de tuplas que la base de datos organiza en filas y columnas. Cada fila de una tabla representa una relación entre un conjunto de valores.

Las bases de datos relacionales se utilizan keyspara crear enlaces entre tablas. A primary keyes un identificador único para una fila de datos. A foreign keyes una columna o combinación de columnas que se utiliza para establecer y aplicar un vínculo entre los datos de dos tablas.

En general, las bases de datos relacionales proporcionan un mecanismo poderoso para definir relaciones dentro de los datos y permitir una recuperación eficiente de los datos.

#### RBDMS (Sistema de Gestion de Bases de Datos Relacionales)

BENEFICIOS:
1. Datos Estructurados: permite el almacenamiento de datos de forma estructurada, utilizando filas y columnas en tablas. Esto facilita la manipulación de los datos mediante SQL (lenguaje de consulta estructurado), lo que garantiza un uso eficiente y flexible.
2. Propiedades de ACID : ACID significa Atomicidad, Consistencia, Aislamiento y Durabilidad. Estas propiedades garantizan una manipulación de datos confiable y segura en un RDBMS, lo que lo hace adecuado para aplicaciones de misión crítica.
3. Normalización : RDBMS admite la normalización de datos, un proceso que organiza los datos de una manera que reduce la redundancia de datos y mejora la integridad de los datos.
4. Escalabilidad : los RDBMS generalmente brindan buenas opciones de escalabilidad, lo que permite agregar más almacenamiento o recursos computacionales a medida que crecen los datos y la carga de trabajo.
5. Integridad de los datos : RDBMS proporciona mecanismos como restricciones, claves primarias y claves externas para hacer cumplir la integridad y coherencia de los datos, garantizando que los datos sean precisos y confiables.
6. Seguridad : los RDBMS ofrecen varias funciones de seguridad, como autenticación de usuario, control de acceso y cifrado de datos para proteger datos confidenciales.

LIMITACIONES Y DESVENTAJAS:
1. Complejidad : configurar y administrar un RDBMS puede ser complejo, especialmente para aplicaciones grandes. Requiere conocimientos y habilidades técnicos para gestionar, ajustar y optimizar la base de datos.
2. Costo : Los RDBMS pueden ser costosos, tanto en términos de tarifas de licencia como de recursos computacionales y de almacenamiento que requieren.
3. Esquema fijo : RDBMS sigue un esquema rígido para la organización de datos, lo que significa que cualquier cambio en el esquema puede llevar mucho tiempo y ser complicado.
4. Manejo de datos no estructurados : los RDBMS no son adecuados para manejar datos no estructurados como archivos multimedia, publicaciones en redes sociales y datos de sensores, ya que su estructura relacional está optimizada para datos estructurados.
5. Escalabilidad horizontal : los RDBMS no son tan fácilmente escalables horizontalmente como las bases de datos NoSQL. Escalar horizontalmente, lo que implica agregar más máquinas al sistema, puede ser un desafío en términos de costo y complejidad.

#### SQL vs noSQL

### Bases de datos SQL

(Lenguaje de consulta estructurado) son bases de datos relacionales.
Tienen un esquema predefinido y los datos se almacenan en tablas que constan de filas y columnas. Las bases de datos SQL siguen las propiedades ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad) para garantizar transacciones confiables. Algunas bases de datos SQL populares incluyen MySQL, PostgreSQL y Microsoft SQL Server.

**Ventajas de las bases de datos SQL:**

*Esquema predefinido* : Ideal para aplicaciones con una estructura fija.
*Transacciones ACID* : garantiza la coherencia y confiabilidad de los datos.
*Soporte para consultas complejas* : las consultas SQL enriquecidas pueden manejar relaciones de datos complejas y operaciones de agregación.
*Escalabilidad* : escalamiento vertical agregando más recursos al servidor (por ejemplo, RAM, CPU).

**Limitaciones de las bases de datos SQL:**

* *Esquema rígido* : las actualizaciones de la estructura de datos requieren mucho tiempo y pueden provocar tiempo de inactividad.
* *Escalado* : dificultades en el escalado horizontal y la fragmentación de datos en varios servidores.
* *No es muy adecuado para datos jerárquicos* : requiere varias tablas y JOIN para modelar estructuras en forma de árbol.

### Bases de datos noSQL

Las bases de datos NoSQL (no solo SQL) se refieren a bases de datos no relacionales, que no siguen un esquema fijo para el almacenamiento de datos. En su lugar, utilizan un formato flexible y semiestructurado como documentos JSON, pares clave-valor o gráficos. MongoDB, Cassandra, Redis y Couchbase son algunas bases de datos NoSQL populares.

**Ventajas de las bases de datos NoSQL:**

* *Esquema flexible* : se adapta fácilmente a los cambios sin interrumpir la aplicación.
* *Escalabilidad* : escalamiento horizontal mediante la partición de datos en múltiples servidores (fragmentación).
* *Rápido* : Diseñado para lecturas y escrituras más rápidas, a menudo con un lenguaje de consulta más simple.
* *Manejo de grandes volúmenes de datos* : más adecuado para gestionar big data y aplicaciones en tiempo real.
* *Soporte para varias estructuras de datos* : diferentes bases de datos NoSQL satisfacen diversas necesidades, como almacenes de documentos, gráficos o valores-clave.

**Limitaciones de las bases de datos NoSQL:**

* *Capacidades de consulta limitadas* : algunas bases de datos NoSQL carecen de soporte de agregación y consultas complejas o utilizan lenguajes de consulta específicos.
* *Coherencia más débil* : muchas bases de datos NoSQL siguen las propiedades BASE (básicamente disponible, estado suave, consistencia eventual) que brindan garantías de consistencia más débiles que las bases de datos compatibles con ACID.

### Mini-Guia mongoDB

[Intro-MongoDB](https://www.mongodb.com/resources/basics/databases/nosql-explained/nosql-vs-sql)


