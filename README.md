📦 Tienda Online – Sistema de Catálogo y Pedidos

Proyecto desarrollado con Django para Programación Backend, que permite mostrar un catálogo de productos, ver su detalle, realizar pedidos personalizados y gestionar los estados de pedido desde el panel de administración.

🚀 Características principales

Catálogo de productos con imágenes y vista de detalle.

Formulario de pedido web con carga de imágenes y datos del cliente.

Panel de administración para gestionar productos y pedidos.

Estados del pedido actualizables desde el administrador.

Visualización del pedido recibido con número de seguimiento generado automáticamente.

Manejo de archivos multimedia (imágenes del cliente).

🛠 Tecnologías utilizadas

Python 3.10+

Django 5.x

Bootstrap 5.3

SQLite3

📑 Requisitos previos

Asegúrate de tener instalados:

Python 3.10 o superior

Pip (gestor de paquetes de Python)

Virtualenv (opcional pero recomendado)

⚙️ Instalación del proyecto

Sigue estos pasos para levantar el proyecto localmente:

1️⃣ Clonar el repositorio git clone https://github.com/tu_usuario/tu_proyecto.git cd tu_proyecto

2️⃣ Crear un entorno virtual (opcional, recomendado) python -m venv venv

Activarlo:

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate

3️⃣ Instalar dependencias pip install -r requirements.txt

4️⃣ Aplicar migraciones python manage.py migrate

5️⃣ Crear el superusuario (para acceder al panel admin) python manage.py createsuperuser

6️⃣ Ejecutar el servidor python manage.py runserver

Luego entra a:

Página principal: http://127.0.0.1:8000/

Panel de Administración: http://127.0.0.1:8000/admin/

🗂 Estructura del Proyecto TiendaOnline/ │── mainApp/ │ ├── migrations/ │ ├── templates/ │ │ ├── home.html │ │ ├── catalogo.html │ │ ├── detalle_producto.html │ │ ├── pedido_web.html │ │ └── confirmacion_pedido.html │ ├── static/ │ ├── admin.py │ ├── models.py │ ├── forms.py │ ├── views.py │ └── urls.py │ ├── TiendaOnline/ ├── media/ ├── manage.py └── requirements.txt

📮 Funcionalidades

Catálogo de productos
Permite listar todos los productos disponibles con foto, nombre y precio base.

Vista de detalle

Muestra:

Galería de imágenes

Categoría

Descripción

Botón para iniciar pedido
Pedido Web

El cliente puede:

Completar formulario

Adjuntar hasta 3 imágenes

Recibir un número único de seguimiento
Administración

Desde /admin/ puedes:

Crear productos

Editar productos

Cambiar estados de los pedidos

Ver imágenes enviadas por el cliente
📦 Gestión de archivos multimedia

Este proyecto utiliza MEDIA_URL y MEDIA_ROOT configurados en settings.py.

Durante desarrollo se sirven con:

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Las imágenes se guardan en:

/media/pedidos/

🧑‍💻 Autor / Créditos

Proyecto desarrollado por Shaira Camacho como parte de un proyecto académico.

📜 Licencia

Este proyecto no posee licencia abierta por defecto.