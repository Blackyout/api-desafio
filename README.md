# Desafío: Microservicio Django + Postgres

Microservicio RESTful desarrollado con **Django** y **Django REST Framework**, diseñado para ser escalable, contenerizado y listo para producción. Gestiona entidades de `Personas` y `Productos` utilizando identificadores UUID y una base de datos PostgreSQL.

## 🛠️ Tech Stack

*   **Lenguaje:** Python 3.11+
*   **Framework:** Django 4.2 + DRF
*   **Base de Datos:** PostgreSQL 15
*   **Documentación:** OpenAPI 3.0 (drf-spectacular)
*   **Infraestructura:** Docker & Docker Compose
*   **Servidor WSGI:** Gunicorn
*   **Testing:** Pytest

## 🚀 Inicio Rápido (Docker)

Esta es la forma recomendada de ejecutar el proyecto, ya que orquesta la API y la Base de Datos automáticamente.

### Prerrequisitos
*   Docker
*   Docker Compose

### Pasos

1.  **Clonar el repositorio:**
    ```bash
    git clone <url-del-repo>
    cd backend
    ```

2.  **Configurar variables de entorno:**
    Crea un archivo `.env` basado en el ejemplo:
    ```bash
    cp .env.example .env
    ```

3.  **Construir y levantar servicios:**
    Utilizamos un `Makefile` para simplificar los comandos:
    ```bash
    make build
    make up
    ```
    *(Si no tienes `make`, usa: `docker-compose up --build -d`)*

4.  **Aplicar migraciones:**
    ```bash
    make migrate
    ```

5.  **Verificar instalación:**
    Accede a la documentación automática en tu navegador:
    *   **Redoc (Vista recomendada):** [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
    *   **OpenAPI Schema (YAML):** [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

---

## ⚙️ Variables de Entorno

El proyecto se configura mediante el archivo `.env`. **No subir este archivo al control de versiones.**

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `DJANGO_SETTINGS_MODULE` | Entorno (dev/prod) | `core.settings.dev` |
| `SECRET_KEY` | Llave criptográfica de Django | `super-secret-key...` |
| `DEBUG` | Modo debug (False en prod) | `True` |
| `ALLOWED_HOSTS` | Hosts permitidos | `localhost,127.0.0.1` |
| `DATABASE_URL` | String de conexión a DB | `postgres://user:pass@db:5432/db` |
| `CORS_ALLOWED_ORIGINS` | Orígenes para Frontend | `http://localhost:4200` |

---

## 📡 Endpoints Principales

Todos los endpoints están prefijados con `/api/v1/`.

### Personas (`/persons/`)
*   `GET /persons/`: Listar personas (paginado).
    *   Filtros: `?email=...`, `?last_name=...`
    *   Orden: `?ordering=-created_at`
*   `POST /persons/`: Crear persona.

### Productos (`/products/`)
*   `GET /products/`: Listar productos.
    *   Filtros: `?sku=...`, `?price__gte=10`, `?price__lte=100`
    *   Búsqueda: `?search=nombre`
*   `POST /products/`: Crear producto.

### Health Checks (Ops)
Endpoints para monitoreo de kubernetes/docker:
*   `GET /healthz`: Verifica que la App responda (Liveness).
*   `GET /readyz`: Verifica conexión a Base de Datos (Readiness).

---

## 🧪 Tests y Calidad de Código

El proyecto incluye tests automatizados con `pytest` y utiliza `ruff`/`black` para el formato.

### Ejecutar Tests
```bash
make test
# O manualmente: docker-compose exec backend pytest"# api-desafio" 
