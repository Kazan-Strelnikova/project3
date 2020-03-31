import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)

    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    jobs = orm.relation("Jobs", back_populates='user')