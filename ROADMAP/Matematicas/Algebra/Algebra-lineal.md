Álgebra Lineal
│
├── Fundamentos
│   ├── Vectores
│   │   ├── Definición
│   │   ├── Operaciones (suma, resta, multiplicación por escalar)
│   │   └── Espacios vectoriales
│
├── Matrices
│   ├── Definición
│   ├── Tipos (cuadradas, rectangulares, diagonales)
│   ├── Operaciones (suma, resta, multiplicación)
│   └── Determinantes
│
├── Sistemas de Ecuaciones Lineales
│   ├── Métodos de solución (eliminación gaussiana, matrices aumentadas)
│   ├── Interpretación geométrica
│   └── Soluciones (única, infinitas, ninguna)
│
├── Transformaciones Lineales
│   ├── Definición
│   ├── Propiedades
│   ├── Núcleo y Recorrido
│   └── Aplicaciones (transformaciones lineales en el plano, en el espacio)
│
└── Valores y Vectores Propios
    ├── Definición
    ├── Cálculo de valores y vectores propios
    ├── Diagonalización de matrices
    └── Aplicaciones en análisis de sistemas dinámicos y teoría de grafos



Vectores => objeto que tiene magnitud y dirección. Se representa típicamente mediante una flecha en un espacio euclidiano, donde la longitud de la flecha representa la magnitud del vector y la dirección de la flecha indica la dirección del vector.

Componentes: Los vectores pueden descomponerse en componentes, que son cantidades escalares que representan la contribución del vector a lo largo de diferentes direcciones. En un espacio euclidiano tridimensional, un vector puede expresarse como una combinación de sus componentes en las direcciones de los ejes x, y, y z.

Operaciones: Los vectores admiten varias operaciones, como la suma, la resta, la multiplicación por un escalar y el producto punto. Estas operaciones obedecen a ciertas reglas algebraicas que definen las propiedades de los vectores.

Espacios vectoriales: Los vectores forman la base de los espacios vectoriales, que son estructuras matemáticas más generales que incluyen conjuntos de vectores cerrados bajo la suma y la multiplicación por escalares, y que cumplen ciertas propiedades como la conmutatividad, asociatividad y distributividad.

En resumen, los vectores son herramientas matemáticas fundamentales que se utilizan para representar magnitudes con dirección en diversos contextos, como la física, la ingeniería, la informática, entre otros.

Ejemplos de Vectores utilizando IA

Representación de palabras: En el procesamiento del lenguaje natural (NLP), las palabras y frases se pueden representar como vectores numéricos. Por ejemplo, usando técnicas como Word2Vec o GloVe, cada palabra en un vocabulario se asigna a un vector en un espacio vectorial de alta dimensión. Estos vectores capturan información semántica y contextual sobre las palabras, lo que permite a los algoritmos de IA entender y procesar el lenguaje humano de manera más efectiva.

Imágenes: En el reconocimiento de imágenes, las imágenes se pueden representar como matrices de píxeles, donde cada píxel tiene valores numéricos que representan intensidades de color. Estas matrices de píxeles se pueden aplanar en vectores unidimensionales y luego procesar mediante técnicas de aprendizaje automático para tareas como clasificación de imágenes, detección de objetos, segmentación semántica, entre otras.

Embeddings de usuarios y productos: En sistemas de recomendación, como en plataformas de streaming de música o películas, los usuarios y los productos (como canciones, películas o productos de comercio electrónico) se pueden representar como vectores en un espacio de características. Estos vectores de embeddings capturan las preferencias y características de los usuarios y los productos, lo que permite a los algoritmos de recomendación encontrar coincidencias entre ellos y generar recomendaciones personalizadas.

Redes Neuronales: En las redes neuronales, los pesos de las conexiones entre neuronas se representan como matrices de pesos. Durante el entrenamiento de la red neuronal, estos pesos se actualizan iterativamente para minimizar una función de pérdida, lo que permite que la red neuronal aprenda a realizar tareas específicas, como reconocimiento de patrones, clasificación o generación de contenido.

EJERCICIOS : 

1. SUMA DE VECTORES BIDIMENSIONALES Y TRIDIMEMNCIONALES .

EJ : // Definición de los vectores
var vector1 = { x: 2, y: 3, z: 4 };
var vector2 = { x: -1, y: 5, z: 2 };

// seria tridimencional 

// Función para sumar dos vectores
function sumarVectores(v1, v2) {
    var resultado = {
        x: v1.x + v2.x,
        y: v1.y + v2.y,
        z: v1.z + v2.z
    };
    return resultado;
}

// Suma de los vectores
var resultadoSuma = sumarVectores(vector1, vector2);

// Mostrar el resultado
console.log("Resultado de la suma de vectores:", resultadoSuma);


2. RESTA DE VECTORES BIDIMENSIONALES Y TRIDIMENSIONALES
3. VECTORES MULTIPLICADOS POR ESCALAR
4. NORAMALIZACION DE VECTOR, MULTIPLICANDO POR EL INVERSOR DE SU MAGNITUD.