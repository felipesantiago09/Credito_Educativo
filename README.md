# Crédito Educativo

Sistema de gestión de crédito educativo desarrollado en Pytho, PostgreSQL, Kivy para la interfaz gráfica.
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
* Kivy
* Git y GitHub

---


## Estructura del proyecto


CreditoEducativo/
├── main.py                           # Punto de entrada: crea tablas y arranca la UI
├── secret_config_sample.py           # Plantilla de configuración 
├── requirements.txt
├── pytest.ini
├── .gitignore
├── src/
│   ├── model/
│   │   ├── connection.py             # Función get_connection() → psycopg2
│   │   ├── estudiante_model.py       # Clase Estudiante 
│   │   └── logica_Credito.py         # Lógica de negocio: cuotas, intereses
│   ├── controller/
│   │   └── estudiante_controller.py  
│   └── view/
│       └── gui/
│           └── credito_gui.py        # Interfaz gráfica Kivy (3 pantallas)
└── tests/
    ├── conftest.py                   # Fixture de conexión a BD de test (_test)
    ├── test_crud_estudiantes.py      # Tests CRUD con pytest + psycopg2
    └── tests_Credito.py              # Tests de lógica de crédito (unittest)


---

---
# Funcionalidades implementadas

## Base de datos

* Conexión a PostgreSQL mediante Render.
* Creación automática de tablas.

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


## 1. Requisitos previos

- Python 3.10 o superior
- PostgreSQL instalado y corriendo (local o en la nube: Render, Railway, etc.)

---

## 2. Instalar dependencias

bash
pip install -r requirements.txt


---

## 3. Configurar la base de datos

1. Copia el archivo de muestra:
   bash
   cp secret_config_sample.py secret_config.py
   
2. Abre secret_config.py y rellena tus datos:
   python
   PG_USER     = "tu_usuario"
   PG_PASSWORD = "tu_contraseña"
   PG_HOST     = "localhost"
   PG_PORT     = "5432"
   PG_DATABASE = "credito_db"
   
   en este caso los datos ya estan rellenados
3. Crea la base de datos en PostgreSQL:
   sql
   CREATE DATABASE credito_db;
   

> secret_config.py está en .gitignore y *nunca* debe subirse al repositorio.
Aun no lo pondremos en el git ignore pero proximamente estara 

---

## 4. Ejecutar la interfaz gráfica

bash
python main.py


Esto:
- Crea automáticamente la tabla estudiantes en PostgreSQL si no existe.
- Abre la ventana con tres pantallas:
  - *Crédito* — calcula cuota mensual, total a pagar e intereses.
  - *Estudiantes* — inserta y lista estudiantes.
  - *Gestión* — elimina y actualiza estudiantes por ID.

---

## 5. Ejecutar los tests

Los tests usan una base de datos separada llamada credito_db_test (se crea automáticamente). Necesitas tener PostgreSQL activo y secret_config.py configurado.

bash
pytest


Para ver detalle:

bash
pytest -v


---

## 6. Reglas de negocio del crédito

| Parámetro              | Restricción                        |
|------------------------|------------------------------------|
| Valor del crédito      | Mayor que 0                        |
| Tasa de interés mensual | Entre 0 % y 4 % (máximo de usura) |
| Número de cuotas       | Entre 1 y 96                       |

---

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| No se encontró secret_config.py | Falta el archivo de credenciales | Copia secret_config_sample.py → secret_config.py y rellénalo |
| could not connect to server | PostgreSQL no está corriendo | Inicia el servicio de PostgreSQL |
| ModuleNotFoundError: No module named 'src' | Corres pytest fuera de la raíz | Ejecuta pytest desde la carpeta raíz del proyecto |

El proyecto incluye pruebas para validar:

* Inserción de datos.
* Consulta de registros.
* Actualización de información.
* Eliminación de registros.

---

# Buenas prácticas implementadas

* Arquitectura MVC.
* Variables de entorno protegidas.
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
