import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=False)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    picture = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    is_admin = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False, default=False)

    user_ideas = orm.relationship("Ideas", back_populates='autor')
    # like = orm.relationship("Ideas", back_populates='likes')
    phone_number = sqlalchemy.Column(sqlalchemy.String, default=None)
    count_likes = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)