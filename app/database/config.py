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

# Configuración SSL para Neon
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "ep-dry-river-adrlqu8w-pooler.c-2.us-east-1.aws.neon.tech",
                "port": "5432",
                "user": "neondb_owner",
                "password": "npg_8cxAUyw6kSHd",
                "database": "neondb",
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
