from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database.config import init_db, close_db
from app.routers import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Inicializar base de datos
    await init_db()

    # IMPORTANTE: Poblar datos iniciales si no existen
    await poblar_datos_iniciales()

    yield

    # Shutdown: Cerrar conexiones
    await close_db()


app = FastAPI(title="Lista de Asistencia API", version="1.0.0", lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(users.router)


async def poblar_datos_iniciales():
    """Poblar datos iniciales si no existen"""
    from app.models.user import User

    nombres = [
        "JOCELYN GARCIA BAUTISTA",
        "FELICITAS BAUTISTA",
        "XOCHITL ALEJANDRA REYES MARTINEZ",
        "ISABEL IRASEMA AVILÉS TORRES",
        "GABRIELA LOPEZ CARDEL",
        "DIANA LAURA REYES GONZALES",
        "MARTHA PATRICIA ARRIAGA MARTINEZ",
        "YOLANDA SEVERINO LORENZO",
        "ARLETH HERNANDEZ GONZALEZ",
        "MARIA DEL ROSARIO ROMERO PEREZ",
        "JEESNIA ADALAY CRUZ UC",
        "ROSA CHALCHI JIMENEZ",
        "VERONICA CUENCA GONZALEZ",
        "ALEJANDRA LAURA MEDINA BARRON",
        "ELOISA ELENE RODRIGUEZ HERNANDEZ",
        "RUBEN RAMOS HERNANDEZ",
        "SANDRA RIVERA NAJERA",
        "ALONDRA TRINIDAD PEREZ",
        "JUAN MANUEL GONZALEZ SANTOS",
        "IVONNE FRIAS DE LA BARCA",
        "PATRICIA GOMEZ HERNANDEZ",
        "MARTHA PATRICIA ARAGON GUERRERO",
        "URIEL LUNA GOMEZ",
        "NORMA ELIZABETH VARELA RUBIO",
        "PEDRO MENDEZ LUGO",
    ]

    for nombre in nombres:
        # Solo crear si no existe
        user_exists = await User.filter(nombre=nombre).exists()
        if not user_exists:
            await User.create(nombre=nombre)
