from models import Model, next_id
from fields import StringField, BigintField


# 记录表
class Types(Model):
    __table__ = 'types'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    orders = BigintField(ddl='bigint(3)')
    created_at = BigintField(ddl='bigint(20)')
