from tortoise import Tortoise, fields
from tortoise.models import Model

async def init_db():
    await Tortoise.init(
        db_url='postgres://<username>:<password>@<host>:<port>/<database>',
        modules={'models': ['app.models.user']}
    )
    await Tortoise.generate_schemas()

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)