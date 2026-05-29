# Crédito Educativo Web

Aplicación web desarrollada en Python utilizando Flask y PostgreSQL para la gestión de créditos educativos. El sistema permite calcular créditos, registrar estudiantes, realizar búsquedas y administrar información desde una interfaz web.

---

# Integrantes del equipo

- Juan Felipe Santiago Pinzon
- Jhairo Esteban Muñetón Cortes
- Jerónimo Roldán Cardona
- Francisco Gómez

---

# Descripción del Proyecto

El proyecto consiste en una aplicación web basada en el patrón MVC (Modelo - Vista - Controlador) que permite:

- Calcular créditos educativos.
- Registrar estudiantes.
- Buscar estudiantes registrados.
- Gestionar información almacenada en PostgreSQL.
- Ejecutar la aplicación desde un navegador web.

La aplicación fue construida usando Flask con Blueprints para organizar las rutas y mantener una estructura limpia y escalable.

---

# Tecnologías Utilizadas

- Python 3.10+
- Flask
- PostgreSQL
- HTML5
- CSS
- Pytest
- Git y GitHub

---

# Arquitectura MVC

El proyecto está organizado siguiendo el patrón MVC:

## Model

Contiene toda la lógica de acceso a datos y conexión con PostgreSQL.

Ubicación:

```text
src/model/
```

Archivos principales:

- `connection.py` → conexión a la base de datos.
- `estudiante_model.py` → operaciones CRUD.
- `logica_Credito.py` → lógica de negocio para cálculos.
- `init_db.py` → creación de tablas.

---

## View

Contiene las vistas web y templates HTML.

Ubicación:

```text
src/view/
templates/
```

Archivos principales:

- `vista_credito.py` → Blueprint de Flask.
- `index.html`
- `crear_estudiante.html`
- `estudiante_buscado.html`
- `calcular_credito.html`

---

## Controller

Contiene la lógica que conecta la vista con el modelo.

Ubicación:

```text
src/controller/
```

Archivo principal:

- `estudiante_controller.py`

---

# Estructura del Proyecto

```text
Credito_Educativo/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── pytest.ini
├── secret_config.py
│
├── src/
│   ├── controller/
│   │   └── estudiante_controller.py
│   │
│   ├── model/
│   │   ├── connection.py
│   │   ├── estudiante_model.py
│   │   ├── init_db.py
│   │   └── logica_Credito.py
│   │
│   ├── view/
│   │   └── web/
│   │       └── vista_credito.py
│   │
│   └── gui/
│       ├── credito_gui.py
│       └── estudiantes_gui.py
│
├── templates/
│   ├── index.html
│   ├── crear_estudiante.html
│   ├── estudiante_buscado.html
│   └── calcular_credito.html
│
├── sql/
│   ├── CrearTabla.sql
│   ├── insertar.sql
│   ├── buscar.sql
│   ├── actualizar.sql
│   └── eliminarBorrar.sql
│
└── tests/
    ├── conftest.py
    ├── test_crud_estudiantes.py
    └── tests_Credito.py
```

---

# Funcionalidades Implementadas

## Funcionalidad Web Principal

La aplicación permite acceder desde el navegador a todas las funcionalidades principales del sistema.

---

## Funcionalidad Web para Buscar

El usuario puede buscar estudiantes registrados en la base de datos.

---

## Funcionalidad Web para Insertar

El sistema permite registrar nuevos estudiantes desde formularios web.

---

## Menú de Inicio

La aplicación cuenta con una página principal (`index.html`) desde donde el usuario puede acceder a:

- Crear estudiante.
- Buscar estudiante.
- Calcular crédito.

---

## Opción para Crear Tablas de la Base de Datos

El sistema crea automáticamente las tablas necesarias al ejecutar la aplicación.

También se incluyen scripts SQL dentro de la carpeta:

```text
sql/
```

---

# Configuración e Instalación

## 1. Clonar el Repositorio

```bash
git clone https://github.com/felipesantiago09/Credito_Educativo.git
```

---

## 2. Entrar al Proyecto

```bash
cd Credito_Educativo
```

---

## 3. Crear Entorno Virtual (Opcional pero recomendado)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Instalar Dependencias

```bash
pip install -r requirements.txt
```

---

# Configuración de la Base de Datos

## 1. Crear Base de Datos en PostgreSQL

```sql
CREATE DATABASE credito_db;
```

---

## 2. Configurar Credenciales

Editar el archivo:

```text
secret_config.py
```

Con los datos de PostgreSQL:

```python
PG_USER = "postgres"
PG_PASSWORD = "tu_password"
PG_HOST = "localhost"
PG_PORT = "5432"
PG_DATABASE = "credito_db"
```

---

# Ejecutar la Aplicación Web

## Iniciar Flask

```bash
python app.py
```

---

## Abrir en el Navegador

Ingresar a:

```text
http://127.0.0.1:5000/
```

---

# Base de Datos en Blanco

La aplicación puede ejecutarse con una base de datos vacía.

Al iniciar:

- Se establece automáticamente la conexión.
- Se crean las tablas necesarias si no existen.
- El sistema queda listo para insertar registros.

---

# Pruebas Unitarias

El proyecto incluye pruebas automáticas para validar:

- Inserción de estudiantes.
- Consulta de registros.
- Actualización de información.
- Eliminación de estudiantes.
- Lógica de cálculo de créditos.

## Ejecutar Tests

```bash
pytest
```

## Ejecutar Tests con Detalle

```bash
pytest -v
```

---

# Requisitos de Evaluación Cubiertos

## Funcionalidad Web Principal

✔ Aplicación accesible desde navegador.

## Funcionalidad Web para Buscar

✔ Implementada mediante formularios y consultas.

## Funcionalidad Web para Insertar

✔ Implementada mediante formularios web.

## Menú de Inicio

✔ Página principal con acceso a funcionalidades.

## Crear Tablas de la BD

✔ Tablas creadas automáticamente y scripts SQL incluidos.

## README con instrucciones completas

✔ Incluye instalación, configuración y ejecución local.

## Base de Datos en Blanco

✔ Compatible con base vacía.

## Pruebas Unitarias

✔ Tests funcionando con Pytest.

## Arquitectura MVC con Blueprints

✔ Implementada usando Flask Blueprints.

---

# Comandos Importantes

## Ejecutar aplicación

```bash
python app.py
```

## Ejecutar pruebas

```bash
pytest
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Posibles Errores y Soluciones

| Error | Posible causa | Solución |
|---|---|---|
| `ModuleNotFoundError` | Dependencias faltantes | Ejecutar `pip install -r requirements.txt` |
| Error de conexión PostgreSQL | PostgreSQL apagado | Iniciar servicio PostgreSQL |
| Credenciales incorrectas | Datos mal configurados | Revisar `secret_config.py` |
| Página no carga | Flask no iniciado | Ejecutar `python app.py` |

---

# Repositorio

Repositorio oficial del proyecto:

```text
https://github.com/felipesantiago09/Credito_Educativo
```
