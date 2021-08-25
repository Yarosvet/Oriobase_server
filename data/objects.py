import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase, create_session


class StoredObject(SqlAlchemyBase):
    __tablename__ = 'objects'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    fields = sqlalchemy.column(sqlalchemy.)
