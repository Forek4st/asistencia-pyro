import os
from dotenv import load_dotenv
from tortoise import Tortoise

# Cargar variables de entorno
load_dotenv()

# URL de conexión SOLO desde variables de entorno - SIN CREDENCIALES EXPUESTAS
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ ERROR: DATABASE_URL environment variable is not set!")

print("✅ Database connection configured from environment variables")

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models.user", "aerich.models"],
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
