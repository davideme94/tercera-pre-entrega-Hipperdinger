Proyecto Django: Tienda Deportiva
Este proyecto es una aplicación web para la compra y venta de indumentaria deportiva. Está desarrollado con Django y dividido en varias aplicaciones para gestionar diferentes tipos de indumentaria, como camisetas, botines y shorts.

Pasos realizados:

Creación del entorno virtual: Se creó un entorno virtual para aislar las dependencias del proyecto y se inicializó un nuevo proyecto Django llamado tienda_deportiva.

Configuración inicial de URLs: Se agregaron las URLs básicas para la página de inicio (home) y para la página de indumentarias (indumentaria).

Creación de vistas básicas: Se agregaron las funciones homepage e indumentaria en views.py para manejar las peticiones de estas páginas.

Creación de HTMLs: Se crearon los archivos HTML correspondientes a homepage e indumentaria.

Personalización con CSS: Los HTMLs fueron personalizados utilizando CSS. Se configuró la ruta de archivos estáticos en settings.py agregando el directorio static.

Creación de la app indumentaria: Se creó una nueva aplicación llamada indumentaria y se agregó al arreglo INSTALLED_APPS en settings.py.

Configuración de URLs de la app: Se crearon las URLs específicas para la aplicación indumentaria y se añadieron a las URLs principales del proyecto.

Funciones de vistas para listas de indumentaria: Se crearon funciones en views.py para listar diferentes tipos de indumentaria y mostrar estos listados en la plantilla indumentaria_lista.html.

Creación de modelos: En models.py, se crearon tres clases que representan los objetos Camiseta, Botín, y Short. Cada clase incluye un método __str__ para mostrar el nombre del objeto en la terminal. Después, se ejecutaron las migraciones usando makemigrations y migrate. En el panel de administración de Django, se agregaron tres productos de ejemplo.

Creación de formularios: Se creó un archivo forms.py con tres clases de formularios para representar los objetos Camiseta, Short, y Botín. Luego, se añadieron las funciones correspondientes en views.py para manejar la creación de nuevos objetos a través de formularios, que se mostraron en las plantillas HTML con sus respectivas URLs. Estos formularios también fueron estilizados con CSS.

Implementación de la búsqueda: Se agregó un formulario en views.py para buscar indumentaria por tipo, es decir busca por tipo de prenda: short, camiseta o botín. Al buscar short, aparecerán los diferentes shorts agregados. Se configuraron las URLs correspondientes y se crearon los archivos HTML para la búsqueda y los resultados, ambos estilizados con CSS.

Inclusión de imágenes en los resultados de búsqueda: Se actualizó el HTML para mostrar las imágenes de los productos junto con sus detalles en los resultados de búsqueda.

admin: david
password : coder123
