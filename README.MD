# Proyecto tienda – Servicio web con Django

Este repositorio contiene un servicio web hecho con Django que implementa un catálogo de productos para una tienda. El proyecto permite consultar, agregar, modificar y eliminar productos usando una API REST y también mostrar el catálogo en una página web sencilla.

Para ver el proyecto, hay que tener instalado Python y Git. Primero hay que moverse a una carpeta de la computadora donde se quiera guardar el proyecto y clonar el repositorio desde GitHub. Después se entra a la carpeta del proyecto, se crea un entorno virtual de Python y se activa. Con el entorno virtual activo, se instala Django usando pip.

Una vez instalado Django, hay que ejecutar el servidor con el comando `python manage.py runserver` desde la raíz del proyecto. Al hacer esto, el proyecto queda corriendo en la dirección `http://127.0.0.1:8000/`.

Para consultar el catálogo en formato JSON, se puede entrar a `http://127.0.0.1:8000/api/productos/`. Si lo que se quiere es ver el catálogo de forma más visual, hay que entrar a `http://127.0.0.1:8000/api/catalogo/`, donde se muestra una tabla con los productos.

El CRUD del catálogo se puede probar con herramientas como Postman o Insomnia. Para agregar productos hay que usar el método POST, para modificar productos se utiliza PUT y para eliminar productos se usa DELETE, siempre trabajando sobre la ruta `/api/productos/` y enviando la información en formato JSON.

La base de datos utilizada es SQLite y ya incluye datos de prueba para poder trabajar con el sistema desde el primer momento. Este proyecto forma parte de un trabajo académico sobre desarrollo de servicios web usando Django.