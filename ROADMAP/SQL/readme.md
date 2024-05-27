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

### SQL

