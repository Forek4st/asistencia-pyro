from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    nombre: str
    domingo: bool = False
    lunes: bool = False
    martes: bool = False
    miercoles: bool = False
    jueves: bool = False
    viernes: bool = False
    sabado: bool = False


class UserResponse(BaseModel):
    id: int
    nombre: str
    domingo: bool
    lunes: bool
    martes: bool
    miercoles: bool
    jueves: bool
    viernes: bool
    sabado: bool

    class Config:
        from_attributes = True


class AsistenciaRequest(BaseModel):
    nombre: str
    dia: str
    asistio: bool = True


class UserUpdate(BaseModel):
    nombre: str = None
    domingo: bool = None
    lunes: bool = None
    martes: bool = None
    miercoles: bool = None
    jueves: bool = None
    viernes: bool = None
    sabado: bool = None
