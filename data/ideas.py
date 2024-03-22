import datetime
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase

user_likes = sqlalchemy.Table("user_likes", SqlAlchemyBase.metadata,
                              sqlalchemy.Column("users", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
                              sqlalchemy.Column("ideas", sqlalchemy.Integer, sqlalchemy.ForeignKey("ideas.id")))


class Ideas(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'ideas'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    autor = orm.relationship('User')
    likes = orm.relationship("User", secondary="user_likes", backref="ideas.id")