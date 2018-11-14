from models import Model, next_id
from fields import StringField, BooleanField, BigintField


# 用户表
class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    username = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    is_admin = BooleanField()
    image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    created_at = BigintField(ddl='bigint(20)')
