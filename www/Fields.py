# define default class for field
class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s: %s>' % (self.__class__.__name__, self.column_type, self.name)


# define string field by field
class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=False, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


# define boolean field by field
class BooleanField(Field):
    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)


# define double field by field
class DoubleField(Field):
    def __init__(self, name=None, default=None, ddl='double(10,2)'):
        super().__init__(name, ddl, False, default)


# define bigint field by field
class BigintField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='bigini(10)'):
        super().__init__(name, ddl, primary_key, default)
