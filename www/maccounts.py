from models import Model, next_id
from fields import StringField, BigintField


# 记录表
class Account(Model):
    __table__ = 'accounts'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    uid = StringField(ddl='varchar(50)')
    created_at = BigintField(ddl='bigint(20)')
