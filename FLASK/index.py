from flask import Flask # Importamos la clase Flask , q sera nuestra aplicacion WSGI.

app = Flask(__name__) # Creamos una instancia de la clase. Primer argumento: nombre del modulo o paquete de la app. __name__ es un atajo conveniente, que es apropiado para la mayoria de los casos. Esto indica a Flask donde buscar recursos como plantillas y archivos estaticos.

@app.route('/') # Le indica a Flask que URL debe activar la funcion
def hello_world():
    return "<p>hello Flask!</p>"

"""
Para correrlo

$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

 
 SERVIDOR VISIBLE EXTERNAMENTE:

 Si ejecuta el servidor, notará que solo se puede acceder al servidor desde su propia computadora, no desde ninguna otra en la red. Esto es así por defecto porque en el modo de depuración un usuario de la aplicación puede ejecutar código Python arbitrario en su computadora.

Si tiene el depurador deshabilitado o confía en los usuarios de su red, puede hacer que el servidor esté disponible públicamente simplemente agregando --host=0.0.0.0a la línea de comando:

$ flask run --host=0.0.0.0

Esto le dice a su sistema operativo que escuche en todas las IP públicas.

MODO DEPURACION

El comando puede hacer más que simplemente iniciar el servidor de desarrollo. Al habilitar el modo de depuración, el servidor se recargará automáticamente si el código cambia y mostrará un depurador interactivo en el navegador si ocurre un error durante una solicitud.flask run

Enrutamiento 

Las aplicaciones web modernas utilizan URL significativas para ayudar a los usuarios. Es más probable que les guste una página y vuelvan si la página utiliza una URL significativa que puedan recordar y utilizar para visitarla directamente.

"""

@app.route('/index')
def index():
    return 'Index Page'

@app.route('/second')
def second():
    return 'Second index'

"""
Reglas variables

Acceso a variables de la URL

Puede agregar secciones variables a una URL marcando las secciones con <variable_name>. Luego, su función recibe el <variable_name> como argumento de palabra clave. Opcionalmente, puede usar un convertidor para especificar el tipo de argumento como <converter:variable_name>.


"""

from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"



"""
Convertidores:
string - (predeterminado) sin "/"
int -
float -
path - como string pero tambien barras "/"
uuid - cadenas UUID

"""

"""

URL únicas / Comportamiento de redireccionamiento 
Las siguientes dos reglas difieren en el uso de la barra diagonal final.

"""

@app.route('/projects/')
def projects():
    return 'The project page'


"""

La URL canónica del projectspunto final tiene una barra diagonal al final. Es similar a una carpeta en un sistema de archivos. Si accede a la URL sin una barra diagonal al final ( /projects), Flask lo redirecciona a la URL canónica con la barra diagonal al final ( /projects/).

La URL canónica del aboutpunto de conexión no tiene una barra diagonal final. Es similar a la ruta de acceso de un archivo. Acceder a la URL con una barra diagonal final ( /about/) produce un error 404 "No encontrado". Esto ayuda a mantener las URL únicas para estos recursos, lo que ayuda a los motores de búsqueda a evitar indexar la misma página dos veces.

"""


# CREACION DE URL


"""
Para crear una URL para una función específica, utilice la url_for()función. Acepta el nombre de la función como su primer argumento y cualquier cantidad de argumentos de palabras clave, cada uno correspondiente a una parte variable de la regla de URL. Las partes variables desconocidas se agregan a la URL como parámetros de consulta.

¿Por qué querrías crear URL utilizando la función de inversión de URL url_for()en lugar de codificarlas en tus plantillas?

La inversión suele ser más descriptiva que la codificación rígida de las URL.

* Puedes cambiar tus URL de una sola vez en lugar de tener que recordar cambiar manualmente las URL codificadas.

* La creación de URL maneja el escape de caracteres especiales de forma transparente.

* Las rutas generadas son siempre absolutas, evitando comportamientos inesperados de rutas relativas en los navegadores.

* Si su aplicación se ubica fuera de la raíz de la URL, por ejemplo, en en /myapplicationlugar de /, url_for()lo manejará adecuadamente por usted.

Por ejemplo, aquí usamos el test_request_context()método para probar url_for(). test_request_context() le dice a Flask que se comporte como si estuviera manejando una solicitud incluso mientras usamos un shell de Python. Ver Variables locales de contexto .

"""

from flask import url_for

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))