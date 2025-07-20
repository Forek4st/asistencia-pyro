from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AsistenciaRequest(BaseModel):
    nombre: str
    dia: str
    asistio: bool = True  # Por defecto True, se puede cambiar a False


# Base de datos de asistencias usando diccionario - BÚSQUEDA O(1)
asistencias_db = {
    "JOCELYN GARCIA BAUTISTA": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "FELICITAS BAUTISTA": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "XOCHITL ALEJANDRA REYES MARTINEZ": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "ISABEL IRASEMA AVILÉS TORRES": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "GABRIELA LOPEZ CARDEL": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "DIANA LAURA REYES GONZALES": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "MARTHA PATRICIA ARRIAGA MARTINEZ": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "YOLANDA SEVERINO LORENZO": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "ARLETH HERNANDEZ GONZALEZ": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "MARIA DEL ROSARIO ROMERO PEREZ": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "JEESNIA ADALAY CRUZ UC": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "ROSA CHALCHI JIMENEZ": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "VERONICA CUENCA GONZALEZ": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "ALEJANDRA LAURA MEDINA BARRON": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "ELOISA ELENE RODRIGUEZ HERNANDEZ": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "RUBEN RAMOS HERNANDEZ": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "SANDRA RIVERA NAJERA": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "ALONDRA TRINIDAD PEREZ": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "JUAN MANUEL GONZALEZ SANTOS": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "IVONNE FRIAS DE LA BARCA": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "PATRICIA GOMEZ HERNANDEZ": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "MARTHA PATRICIA ARAGON GUERRERO": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "URIEL LUNA GOMEZ": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "NORMA ELIZABETH VARELA RUBIO": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
    "PEDRO MENDEZ LUGO": {
        "domingo": False,
        "lunes": False,
        "martes": False,
        "miercoles": False,
        "jueves": False,
        "viernes": False,
        "sabado": False,
    },
}


@app.get("/")
async def obtener_asistencias():
    """Obtiene todas las asistencias"""
    # Convertir diccionario a formato compatible con frontend
    asistencias_lista = []
    for nombre, dias in asistencias_db.items():
        persona = {"nombre": nombre}
        persona.update(dias)  # Agregar los días de asistencia
        asistencias_lista.append(persona)

    return {"asistencias": asistencias_lista}


@app.post("/")
async def manejar_asistencia(request: AsistenciaRequest):
    """Maneja tanto registro como actualización de asistencia"""
    # Buscar persona directamente en diccionario - O(1)

    if request.nombre.upper() not in asistencias_db:
        raise HTTPException(
            status_code=404, detail=f"Persona {request.nombre} no encontrada"
        )

    # Actualizar directo - sin búsqueda!
    asistencias_db[request.nombre.upper()][request.dia.lower()] = request.asistio

    return {
        "mensaje": f"Asistencia de {request.nombre.title()} {'registrada' if request.asistio else 'removida'} el día {request.dia.title()}"
    }
