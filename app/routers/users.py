from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist
from app.models.user import User
from app.schemas.user import AsistenciaRequest

router = APIRouter()


@router.get("/")
async def obtener_asistencias():
    """Obtiene todas las asistencias"""
    users = await User.all()
    asistencias_lista = []

    for user in users:
        asistencias_lista.append(
            {
                "nombre": user.nombre,
                "domingo": user.domingo,
                "lunes": user.lunes,
                "martes": user.martes,
                "miercoles": user.miercoles,
                "jueves": user.jueves,
                "viernes": user.viernes,
                "sabado": user.sabado,
            }
        )

    return {"asistencias": asistencias_lista}


@router.post("/")
async def manejar_asistencia(request: AsistenciaRequest):
    """Maneja tanto registro como actualización de asistencia"""
    try:
        user = await User.get(nombre__iexact=request.nombre)
    except DoesNotExist:
        raise HTTPException(
            status_code=404, detail=f"Persona {request.nombre} no encontrada"
        )

    # Actualizar el día específico
    dia_lower = request.dia.lower()
    setattr(user, dia_lower, request.asistio)
    await user.save()

    return {
        "mensaje": f"Asistencia de {request.nombre.title()} {'registrada' if request.asistio else 'removida'} el día {request.dia.title()}"
    }
