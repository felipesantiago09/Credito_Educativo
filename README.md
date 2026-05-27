# Crédito Educativo

Sistema de gestión de crédito educativo desarrollado en Python utilizando arquitectura MVC, PostgreSQL, SQLAlchemy ORM y Kivy para la interfaz gráfica.
---
##  Integrantes del equipo

- **Jhairo Esteban Muñeton Cortes**
- **Juan Felipe Santiago Pinzacho**





- **Jerónimo Roldán Cardona**
- **Francisco Gómez**

---

##  Características

- Cálculo de cuota mensual  
- Cálculo del total de intereses  
- Registro de abonos realizados  
- Visualización de resultados en una interfaz gráfica amigable  
- Implementación basada en Kivy  

---

# Tecnologías utilizadas

* Python 3.12
* PostgreSQL
* Render
* SQLAlchemy ORM
* Kivy
* python-dotenv
* Git y GitHub

---

## Estructura

```txt
Credito_Educativo/
│
├── src/
│   ├── controller/
│   ├── model/
│   └── view/
│       └── gui/
│
├── tests/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

---
# Funcionalidades implementadas

## Base de datos

* Conexión a PostgreSQL mediante Render.
* Creación automática de tablas.
* Uso de SQLAlchemy ORM.

## CRUD completo

### CREATE

Inserción de estudiantes en la base de datos.

### READ

Consulta de estudiantes registrados.

### UPDATE

Actualización de información de estudiantes.

### DELETE

Eliminación de estudiantes.

## Interfaz gráfica

* Interfaz desarrollada con Kivy.
* Integración con el sistema CRUD.
* Gestión visual de estudiantes.

## Seguridad

* Uso de archivo `.env` para proteger credenciales.
* Uso de `.gitignore` para evitar subir datos sensibles.

---


##  Instrucciones para ejecutar la GUI


## 1. Clonar el repositorio

```bash
git clone https://github.com/felipesantiago09/Credito_Educativo.git
```

---

## 2. Entrar a la carpeta del proyecto

```bash
cd Credito_Educativo
```

---

## 3. Crear entorno virtual

```bash
py -3.12 -m venv .venv
```

---

## 4. Activar entorno virtual

### Windows PowerShell

```bash
.venv\Scripts\Activate.ps1
```

---

## 5. Instalar dependencias


---
# Ejecución del proyecto

```bash
python main.py
```

---

# Modelo implementado

## Estudiante

Campos:

* id
* nombre
* correo
* carrera

---

# ORM utilizado

El proyecto utiliza SQLAlchemy ORM para:

* Crear tablas automáticamente.
* Mapear clases Python a tablas PostgreSQL.
* Gestionar consultas SQL mediante objetos.

---

# Base de datos

La base de datos está desplegada en Render utilizando PostgreSQL.

---

# Pruebas

El proyecto incluye pruebas para validar:

* Inserción de datos.
* Consulta de registros.
* Actualización de información.
* Eliminación de registros.

---

# Buenas prácticas implementadas

* Arquitectura MVC.
* Variables de entorno protegidas.
* Uso de ORM.
* Separación de responsabilidades.
* Repositorio GitHub.
* Control de versiones con Git.

---

# Requisitos

* Python 3.12
* PostgreSQL
* Conexión a internet

---

##  Notas adicionales

- Mantener la estructura de carpetas para evitar errores en las importaciones.  
- Si Kivy presenta problemas, revisar instalación o dependencias del sistema.
- Si eliminas un estudiante tienes que cerrar y volver a abrir para que se actualice
