
## Sistema de tareas hecho con Django + HTMX

## 📌 Descripción

Este proyecto es una simple aplicación de tareas (to-do list / task manager) construida usando Django + HTMX. Permite manejar tareas desde el backend de Django con interacciones dinámicas en frontend sin necesidad de una SPA completa.

## 🧰 Tecnologías

- Python  
- Django  
- HTMX  
- HTML (templates de Django)  

## 🚀 Cómo ejecutar el proyecto localmente

Sigue estos pasos:

1. Clona el repositorio  
   ```bash
   git clone https://github.com/harveyspecter001/django-htmx-notes.git
   cd django-htmx-notes
Crea y activa un entorno virtual (recomendado)

bash
Copiar código
python -m venv .venv
# En Windows
.venv\\Scripts\\activate
# En UNIX / macOS
source .venv/bin/activate
Instala las dependencias (si las defines en un requirements.txt; si no, asegúrate de tener Django instalado)

bash
Copiar código
pip install django
Aplica migraciones

bash
Copiar código
python manage.py migrate
Ejecuta el servidor de desarrollo

bash
Copiar código
python manage.py runserver
📂 Estructura del proyecto
bash
Copiar código
django-htmx-notes/
│
├── app/            # Aplicación principal Django con la lógica de tareas  
├── config/         # Configuración del proyecto Django (settings, urls, etc.)  
├── manage.py       # Script de administración de Django  
└── db.sqlite3      # Base de datos SQLite (para desarrollo)  
✅ Funcionalidades
Crear nuevas tareas.

Ver lista de tareas.

Marcar tareas como completadas / pendientes.

El frontend reacciona dinámicamente gracias a HTMX — sin recargar toda la página.

🔧 Por qué Django + HTMX
Usar Django + HTMX permite construir aplicaciones web interactivas sin la complejidad de un frontend SPA completo. HTMX añade a HTML atributos que permiten hacer peticiones AJAX simples, actualizar partes del DOM, y lograr una experiencia fluida. 
Wikipedia

ℹ️ Notas
Actualmente la base de datos es db.sqlite3 — ideal para desarrollo o pruebas. Para producción deberías cambiar a una base más robusta.

Puedes adaptar los templates, estilos y lógica según tus necesidades.

Si quieres añadir autenticación, filtros, estados avanzados u otras features — Django + HTMX es flexible para extender.

✨ Contribuciones
Si quieres mejorar el proyecto, estás invitado a:

limpiar o mejorar la estructura de carpetas;

agregar mejores estilos (CSS / framework);

añadir autenticación de usuario;

mejorar la experiencia UX;

refactorizar código.
