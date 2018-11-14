from models import Model, next_id
from fields import StringField, BooleanField, BigintField, DoubleField


# 记录表
class Record(Model):
    __table__ = 'records'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    uid = StringField(ddl='varchar(50)')
    typeid = StringField(ddl='varchar(50)')
    tagid = StringField(ddl='varchar(50)')
    accountid = StringField(ddl='varchar(50)')
    type = BooleanField()
    money = DoubleField(ddl='double(10,2)')
    commnets = StringField(ddl='varchar(200)')
    created_at = BigintField(ddl='bigint(20)')
