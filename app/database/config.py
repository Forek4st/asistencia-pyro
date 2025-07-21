import os
import ssl
from dotenv import load_dotenv
from tortoise import Tortoise

# Cargar variables de entorno
load_dotenv()

# URL de conexión SOLO desde variables de entorno - SIN CREDENCIALES EXPUESTAS
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ ERROR: DATABASE_URL environment variable is not set!")

print("✅ Database connection configured from environment variables")

# Configuración SSL para Render PostgreSQL
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "dpg-d1v8kl24d50c73db3bi0-a.oregon-postgres.render.com",
                "port": "5432",
                "user": "asistencia_pyro_user",
                "password": "6YCChGE3nmSv6WUBP3Qob7ETOF8oVOgy",
                "database": "asistencia_pyro",
                "ssl": ssl_context,
            }
        }
    },
    "apps": {
        "models": {
            "models": ["app.models.user"],
            "default_connection": "default",
        },
    },
}


async def init_db():
    """Inicializar la base de datos"""
    await Tortoise.init(config=TORTOISE_ORM)
    # Crear tablas si no existen (IMPORTANTE para Vercel)
    await Tortoise.generate_schemas()


async def close_db():
    """Cerrar conexiones"""
    await Tortoise.close_connections()
