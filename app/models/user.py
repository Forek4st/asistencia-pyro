from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=255, unique=True)
    domingo = fields.BooleanField(default=False)
    lunes = fields.BooleanField(default=False)
    martes = fields.BooleanField(default=False)
    miercoles = fields.BooleanField(default=False)
    jueves = fields.BooleanField(default=False)
    viernes = fields.BooleanField(default=False)
    sabado = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "asistencias"

    def __str__(self):
        return self.nombre
