import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Tasks(SqlAlchemyBase):
    __tablename__ = 'tests'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    test_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("test.id"))
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ans1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ans2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ans3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ans4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    correct_answer = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    user = orm.relation('Tests')