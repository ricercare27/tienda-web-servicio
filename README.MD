Este repositorio contiene un servicio web desarrollado con Django que implementa un catálogo de productos para una tienda. El proyecto permite consultar un catálogo desde una página web, ver el detalle de cada producto y administrar productos mediante usuarios con distintos privilegios.

Para ver el proyecto, hay que tener instalado Python y Git. Primero hay que moverse a una carpeta de la computadora donde se quiera guardar el proyecto y clonar el repositorio desde GitHub. Después hay que entrar a la carpeta del proyecto, que es donde se encuentra el archivo manage.py.

Desde la raíz del proyecto, hay que crear un entorno virtual de Python y activarlo. Con el entorno virtual activo, hay que instalar Django usando pip.

Una vez instalado Django, hay que crear la base de datos del proyecto. Esto se hace ejecutando las migraciones desde la misma carpeta donde está manage.py. Este paso crea automáticamente las tablas necesarias, aunque inicialmente estarán vacías.

Después de crear la base de datos, hay que poblarla con productos de ejemplo. Para esto, se utiliza la consola interactiva de Django. Desde la raíz del proyecto se entra al shell y se ejecuta el siguiente código, que crea varios productos similares a los usados durante el desarrollo del proyecto.

Para poblar, ejecutar:

python manage.py shell

from catalogo.models import Producto

productos = [
    Producto(nombre="Arroz 1 kg", descripcion="Arroz blanco de grano largo", precio=28.50, existencia=50),
    Producto(nombre="Frijol negro 900 g", descripcion="Frijol negro seleccionado", precio=32.00, existencia=40),
    Producto(nombre="Frijol bayo 900 g", descripcion="Frijol bayo", precio=34.00, existencia=35),
    Producto(nombre="Azúcar 1 kg", descripcion="Azúcar estándar", precio=26.00, existencia=60),
    Producto(nombre="Aceite vegetal 1 L", descripcion="Aceite vegetal comestible", precio=45.00, existencia=30),
    Producto(nombre="Sal 1 kg", descripcion="Sal refinada", precio=12.00, existencia=80),
    Producto(nombre="Harina de trigo 1 kg", descripcion="Harina para todo uso", precio=22.00, existencia=45),
    Producto(nombre="Harina de maíz 1 kg", descripcion="Harina nixtamalizada", precio=18.00, existencia=55),
    Producto(nombre="Pasta espagueti", descripcion="Pasta de trigo duro", precio=14.00, existencia=70),
    Producto(nombre="Pasta fusilli", descripcion="Pasta tipo fusilli", precio=16.00, existencia=65),
    Producto(nombre="Atún en lata", descripcion="Atún en agua 140 g", precio=19.00, existencia=90),
    Producto(nombre="Sardinas en lata", descripcion="Sardinas en tomate", precio=21.00, existencia=50),
    Producto(nombre="Leche entera 1 L", descripcion="Leche pasteurizada", precio=24.00, existencia=40),
    Producto(nombre="Leche deslactosada 1 L", descripcion="Leche deslactosada", precio=26.00, existencia=35),
    Producto(nombre="Café soluble 200 g", descripcion="Café soluble clásico", precio=68.00, existencia=25),
    Producto(nombre="Chocolate en polvo", descripcion="Chocolate para bebida", precio=38.00, existencia=30),
    Producto(nombre="Galletas maría", descripcion="Galletas tradicionales", precio=17.00, existencia=75),
    Producto(nombre="Galletas saladas", descripcion="Galletas tipo cracker", precio=18.00, existencia=70),
    Producto(nombre="Mayonesa 390 g", descripcion="Mayonesa tradicional", precio=32.00, existencia=45),
    Producto(nombre="Catsup 340 g", descripcion="Salsa de tomate", precio=28.00, existencia=50),
    Producto(nombre="Mostaza 220 g", descripcion="Mostaza amarilla", precio=20.00, existencia=40),
    Producto(nombre="Salsa picante", descripcion="Salsa picante roja", precio=15.00, existencia=60),
    Producto(nombre="Avena 400 g", descripcion="Avena en hojuelas", precio=23.00, existencia=55),
    Producto(nombre="Cereal de maíz", descripcion="Cereal de desayuno", precio=48.00, existencia=35),
    Producto(nombre="Detergente 1 kg", descripcion="Detergente en polvo", precio=52.00, existencia=25),
    Producto(nombre="Jabón de tocador", descripcion="Jabón corporal", precio=10.00, existencia=100),
    Producto(nombre="Papel higiénico 4 rollos", descripcion="Papel higiénico básico", precio=36.00, existencia=40),
    Producto(nombre="Servilletas", descripcion="Paquete de servilletas", precio=14.00, existencia=60),
    Producto(nombre="Cloro 1 L", descripcion="Cloro multiusos", precio=18.00, existencia=45),
    Producto(nombre="Desinfectante", descripcion="Desinfectante aromatizante", precio=22.00, existencia=35),
]

Producto.objects.bulk_create(productos)


Una vez cargados los datos, se puede salir del shell y ejecutar el servidor de desarrollo desde la raíz del proyecto con el comando python manage.py runserver.

El proyecto se puede ver en el navegador entrando a http://127.0.0.1:8000/, donde aparece la página de inicio. Desde ahí se puede acceder al catálogo de productos y ver el detalle de cada uno. El acceso al panel de administración se realiza desde http://127.0.0.1:8000/admin/, utilizando un usuario de gestión creado previamente.

Este proyecto forma parte de un trabajo académico sobre desarrollo de servicios web usando Django y arquitectura basada en cliente-servidor.