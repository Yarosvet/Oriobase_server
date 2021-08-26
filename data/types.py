import sqlalchemy
from .db_session import SqlAlchemyBase


class Object(SqlAlchemyBase):
    __tablename__ = 'objects'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)  # Name
    fields = sqlalchemy.Column(sqlalchemy.PickleType)  # [Field(...), Field(...)]
    relations = sqlalchemy.Column(sqlalchemy.PickleType)  # [Relation(...), Relation(...)]


class ObjectGroup(SqlAlchemyBase):
    __tablename__ = 'object_groups'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)  # Name of group
    description = sqlalchemy.Column(sqlalchemy.String)  # Description of the group
    objects_id = sqlalchemy.Column(sqlalchemy.PickleType)  # [1, 2, 3]


class Field:
    def __init__(self, field_type: str, name: str, data):
        self.field_type = field_type
        self.name = name
        self.data = data


class Relation:
    def __init__(self, name: str, target):
        self.name = name
        self.target_id = target.id
        if isinstance(target, Object):
            self.type = "Object"
        elif isinstance(target, ObjectGroup):
            self.type = "ObjectGroup"
