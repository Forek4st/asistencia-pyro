from pydantic import BaseModel


class AsistenciaRequest(BaseModel):
    nombre: str
    dia: str
    asistio: bool = True
