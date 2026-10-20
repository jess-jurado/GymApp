# 🏋️‍♂️ GymApp — Tu Entrenador Personal Inteligente

<div align="center">

![GymApp Banner](https://img.shields.io/badge/GymApp-Plataforma%20de%20Entrenamiento%20%26%20IA-10b981?style=for-the-badge&logo=google-fit&logoColor=white)

**Plataforma web y PWA integral para la planificación de entrenamientos, seguimiento de progreso y rutinas adaptativas impulsadas por Inteligencia Artificial.**

[![Live Demo](https://img.shields.io/badge/Demo%20en%20Vivo-jssgjurado.pythonanywhere.com-00a4e4?style=for-the-badge&logo=pythonanywhere&logoColor=white)](https://jssgjurado.pythonanywhere.com)
[![GitHub Repository](https://img.shields.io/badge/GitHub-jess--jurado%2FGymApp-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jess-jurado/GymApp)
[![Python Version](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![NVIDIA NIM](https://img.shields.io/badge/AI-NVIDIA%20NIM%20%7C%20Llama%203.3%2070B-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://build.nvidia.com/)
[![PWA Ready](https://img.shields.io/badge/PWA-Mobile--First-5A0FC8?style=for-the-badge&logo=pwa&logoColor=white)](#-progressive-web-app-pwa)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

</div>

---

## 🌐 Aplicación en Producción (Live Demo)

La aplicación se encuentra actualmente desplegada y 100% operativa para su uso en la nube:

👉 **[https://jssgjurado.pythonanywhere.com](https://jssgjurado.pythonanywhere.com)**

> 💡 *Puedes crear una cuenta de forma gratuita o explorar todas las funciones directamente desde tu navegador móvil o de escritorio.*

---

## 📑 Tabla de Contenidos

- [Descripción General](#-descripción-general)
- [Características Principales](#-características-principales)
  - [Inteligencia Artificial con NVIDIA NIM](#-inteligencia-artificial-con-nvidia-nim)
  - [Gestión de Rutinas y Entrenamientos](#-gestión-de-rutinas-y-entrenamientos)
  - [Seguimiento Antropométrico y Rendimiento](#-seguimiento-antropométrico-y-rendimiento)
  - [Progressive Web App (PWA)](#-progressive-web-app-pwa)
- [Stack Tecnológico](#-stack-tecnológico)
- [Arquitectura del Proyecto](#-arquitectura-del-proyecto)
- [Instalación y Configuración Local](#-instalación-y-configuración-local)
- [Variables de Entorno](#-variables-de-entorno)
- [Ejecución de Pruebas](#-ejecución-de-pruebas)
- [Despliegue en Servidores](#-despliegue-en-servidores)
- [Autor y Contacto](#-autor-y-contacto)
- [Licencia](#-licencia)

---

## 📖 Descripción General

**GymApp** es una solución integral orientada tanto a principiantes como a atletas experimentados que desean estructurar sus rutinas de ejercicio, registrar sus progresos en el gimnasio y recibir orientación personalizada en tiempo real. 

A diferencia de las aplicaciones genéricas, **GymApp combina el poder de un modelo de lenguaje de última generación (Meta Llama 3.3 70B Instruct vía NVIDIA NIM)** con un catálogo cerrado de ejercicios reales con soporte multimedia. La IA analiza los datos biométricos del usuario (somatotipo, IMC, nivel y disponibilidad) para sugerir rutinas coherentes y factibles sin "alucinaciones" ni inventar ejercicios fuera de tu gimnasio.

---

## ✨ Características Principales

### 🤖 Inteligencia Artificial con NVIDIA NIM
- **Onboarding Biométrico:** Evaluación inicial de composición corporal (edad, sexo, altura, peso, nivel de experiencia, días de entrenamiento disponibles, somatotipo y cálculo clínico automático de IMC).
- **Generación de Rutinas Personalizadas:** Motor de IA que toma exclusivamente los ejercicios disponibles en la base de datos para armar un plan semanal equilibrado según el perfil del usuario.
- **Entrenador Virtual con Guardarraíles de Seguridad:** Chatbot interactivo especializado en musculación, técnica de levantamiento y nutrición deportiva. Incorpora filtros estrictos (*guardrails*) que rechazan consultas fuera de contexto para garantizar respuestas precisas.
- **Sobrecarga Progresiva y Análisis de Rendimiento:** Algoritmo de sugerencias en vivo para aumentar cargas o repeticiones según el historial reciente de series.
- **Evaluaciones Periódicas Automatizadas:** Informes de evolución corporal y rendimiento físico generados automáticamente.

### 📋 Gestión de Rutinas y Entrenamientos
- **Catálogo Multimedia Clasificado:** Amplia biblioteca de ejercicios organizada por grupos musculares principales (Pecho, Espalda, Hombros, Pierna, Bíceps, Tríceps, Core, Cardio) con soporte fotográfico.
- **Planificador de Rutinas:** Creación, edición y asignación flexible de rutinas por día de la semana.
- **Registro en Vivo (Workout Tracker):** Registro durante la sesión de series, peso levantado (kg), repeticiones realizadas, duración de la sesión y estimación de gasto calórico.

### 📊 Seguimiento Antropométrico y Rendimiento
- Historial completo de entrenamientos realizados con fecha y hora.
- Gráficos y registro histórico de peso corporal para evaluar etapas de definición o volumen.
- Consulta de marcas históricas y récords personales por ejercicio.

### 📱 Progressive Web App (PWA)
- **Instalable:** Añádela como aplicación nativa a la pantalla de inicio en smartphones (Android, iOS) y escritorio.
- **Soporte Offline:** Service worker (`sw.js`) con estrategia de caché para carga ultrarrápida y navegación fluida.
- **Diseño Mobile-First:** Interfaz táctil, moderna y adaptativa optimizada para su uso cómodo durante los entrenamientos en sala.

---

## 🛠️ Stack Tecnológico

| Capa | Tecnología | Descripción |
| :--- | :--- | :--- |
| **Backend** | [Python](https://www.python.org/) 3.10+ | Lenguaje de desarrollo backend |
| **Framework Web** | [Flask](https://flask.palletsprojects.com/) 3.1 | Microframework modular basado en Blueprints |
| **Motor de IA** | [NVIDIA NIM](https://build.nvidia.com/) | API de inferencia de alto rendimiento |
| **Modelo LLM** | `meta/llama-3.3-70b-instruct` | Modelo de lenguaje avanzado para asesoría y generación |
| **SDK de IA** | [OpenAI Python SDK](https://github.com/openai/openai-python) | Cliente de conexión compatible con endpoints NVIDIA NIM |
| **Base de Datos** | SQLite3 / PostgreSQL | Almacenamiento relacional rápido y ligero |
| **Seguridad** | [Bcrypt](https://pypi.org/project/bcrypt/) & [PyJWT](https://pyjwt.readthedocs.io/) | Cifrado seguro de contraseñas y autenticación por tokens |
| **Frontend** | HTML5, CSS3, JavaScript ES6+ | Interfaz reactiva sin sobrecarga de frameworks pesados |
| **Capacidades PWA** | Web App Manifest & Service Worker | Soporte para instalación móvil y caché |
| **Gestión Multimedia** | Cloudinary & Almacenamiento Local | Gestión optimizada de imágenes de ejercicios |
| **Servidor de Producción** | Gunicorn & WSGI | Servidor HTTP WSGI para entornos Linux/PythonAnywhere |

---

## 📁 Arquitectura del Proyecto

```plaintext
GymApp/
├── Assets_gymApp/          # Imágenes clasificadas por grupo muscular y ejercicios
│   └── Imagenes/
│       ├── Pecho/
│       ├── Espalda/
│       ├── Pierna/
│       └── ...
├── models/                 # Modelos de datos y definiciones de esquemas
├── routes/                 # Blueprints modulares de la aplicación
│   ├── auth_routes.py      # Autenticación, registro, login y confirmación
│   ├── auth_utils.py       # Decoradores y validación de tokens JWT
│   ├── ai_routes.py        # Rutas del entrenador IA, onboarding y chat
│   ├── rutina_routes.py    # Gestión de rutinas y dashboard principal
│   ├── user_routes.py      # Perfil de usuario y ajustes
│   ├── workout_routes.py   # Registro y ejecución de entrenamientos
│   └── utils.py            # Utilidades generales
├── services/               # Lógica de negocio externa e integraciones
│   └── ai.py               # Conexión con NVIDIA NIM y prompts del entrenador
├── static/                 # Archivos estáticos servidos al navegador
│   ├── css/                # Hojas de estilo y diseño responsive
│   ├── js/                 # Lógica interactiva en cliente
│   ├── img/                # Iconos del sistema y logo PWA
│   ├── manifest.json       # Manifiesto de la Progressive Web App
│   └── sw.js               # Service Worker para capacidades PWA
├── templates/              # Plantillas Jinja2
│   ├── base.html           # Layout común y barra de navegación
│   ├── index.html          # Landing page de bienvenida
│   ├── login.html          # Inicio de sesión
│   ├── register.html       # Registro de nuevos usuarios
│   ├── onboarding.html     # Asistente de perfil inicial IA
│   ├── dashboard.html      # Panel principal del usuario
│   ├── crear_rutina.html   # Creador interactivo de rutinas
│   ├── detalle_ejercicio.html # Vista detallada y ficha de ejercicio
│   ├── evaluaciones.html   # Reportes y evaluaciones de progreso
│   └── workout.html        # Modo entrenamiento en tiempo real
├── tests/                  # Suite de pruebas unitarias
│   ├── test_ai_system.py   # Tests del cálculo de IMC, tablas y guardarraíles
│   └── test_db_connection.py # Verificación de conectividad a base de datos
├── .env.example            # Plantilla de variables de entorno
├── app.py                  # Punto de entrada de la aplicación Flask
├── config.py               # Configuración centralizada y conexión a BD
├── init_db.py              # Script de inicialización y poblado de la base de datos
├── requirements.txt        # Dependencias fijadas del proyecto
└── render.yaml             # Especificación de despliegue para Render (opcional)
```

---

## 🚀 Instalación y Configuración Local

Sigue estos sencillos pasos para poner en marcha el proyecto en tu entorno local:

### 1. Prerrequisitos
- **Python 3.9** o superior instalado en el sistema.
- **Git** instalado.

### 2. Clonar el Repositorio
```bash
git clone https://github.com/jess-jurado/GymApp.git
cd GymApp
```

### 3. Crear y Activar el Entorno Virtual

- **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **En Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 4. Instalar Dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configurar las Variables de Entorno
Crea una copia del archivo `.env.example` y nómbralo `.env`:

```bash
cp .env.example .env
```

Edita el archivo `.env` con tus credenciales:
```env
SECRET_KEY=clave_secreta_super_segura_para_desarrollo
NVIDIA_API_KEY=tu_api_key_de_nvidia_nim
```
> 🔑 *Puedes obtener una clave gratuita para NVIDIA NIM registrándote en [NVIDIA Build](https://build.nvidia.com/).*

### 6. Inicializar y Poblar la Base de Datos
Ejecuta el script de inicialización para crear las tablas SQLite y cargar automáticamente el catálogo completo de ejercicios desde las carpetas de imágenes:

```bash
python init_db.py
```

### 7. Ejecutar el Servidor de Desarrollo
```bash
python app.py
```

Abre tu navegador y accede a:
👉 **[http://localhost:5001](http://localhost:5001)**

---

## ⚙️ Variables de Entorno

| Variable | Requerida | Valor por Defecto | Descripción |
| :--- | :---: | :--- | :--- |
| `SECRET_KEY` | **Sí** | `mi_clave_secreta_por_defecto` | Clave para cifrar sesiones y firmas JWT |
| `NVIDIA_API_KEY` | **Sí** (para IA) | Ninguno | API Key de NVIDIA NIM para las funciones de IA |
| `SMTP_SERVER` | No | `smtp.gmail.com` | Host SMTP para envío de correos de verificación |
| `SMTP_PORT` | No | `587` | Puerto del servidor SMTP |
| `SMTP_USER` | No | Ninguno | Usuario/Correo de la cuenta emisora |
| `SMTP_PASS` | No | Ninguno | Contraseña de aplicación para SMTP |
| `CLOUDINARY_CLOUD_NAME` | No | Ninguno | Nombre del cloud de Cloudinary (si aplica) |
| `CLOUDINARY_API_KEY` | No | Ninguno | API Key de Cloudinary |
| `CLOUDINARY_API_SECRET` | No | Ninguno | API Secret de Cloudinary |

---

## 🧪 Ejecución de Pruebas

El proyecto cuenta con pruebas automatizadas con el framework estándar `unittest` de Python:

```bash
python -m unittest discover tests/
```

Las pruebas cubren:
- Conectividad e integridad de la base de datos.
- Existencia y coherencia de las tablas principales (`PerfilUsuario`, `HistorialPeso`, `Evaluaciones`).
- Cálculo biométrico y estados clínicos de IMC.
- Guardarraíles y control de contexto del Asistente de IA.

---

## ☁️ Despliegue en Servidores

### Despliegue en PythonAnywhere
La aplicación está actualmente alojada en **PythonAnywhere**:

1. Sube el código o clona el repositorio desde la consola Bash de PythonAnywhere:
   ```bash
   git clone https://github.com/jess-jurado/GymApp.git
   ```
2. Crea el entorno virtual con Python 3.10 e instala los requerimientos:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 gymapp-env
   pip install -r requirements.txt
   ```
3. En la pestaña **Web** de PythonAnywhere:
   - Configura la ruta del virtualenv: `/home/jssgjurado/.virtualenvs/gymapp-env`
   - Configura el archivo WSGI importando la aplicación:
     ```python
     import sys
     import os

     path = '/home/jssgjurado/GymApp'
     if path not in sys.path:
         sys.path.append(path)

     from app import app as application
     ```
   - Configura las rutas estáticas (`/static/` a `/home/jssgjurado/GymApp/static` y `/imagenes/` a `/home/jssgjurado/GymApp/Assets_gymApp/Imagenes`).
   - Añade tu archivo `.env` en la raíz del proyecto.
4. Reinicia la aplicación web con el botón verde **Reload**.

---

## 👤 Autor y Contacto

Desarrollado con dedicación y enfoque profesional por:

- **Jess Jurado** — [@jess-jurado](https://github.com/jess-jurado)
- **Repositorio:** [https://github.com/jess-jurado/GymApp](https://github.com/jess-jurado/GymApp)
- **Web en Vivo:** [https://jssgjurado.pythonanywhere.com](https://jssgjurado.pythonanywhere.com)

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT**. Consulta el archivo `LICENSE` para más información.
