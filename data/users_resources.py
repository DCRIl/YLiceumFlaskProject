from flask import jsonify
from flask_restful import Resource, abort, reqparse
from . import db_session
from .users import User


class UserResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        return jsonify({"user": user.to_dict(only=("name", "email", "is_admin", "phone_number"))})

class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('name', 'email', 'is_admin')) for item in users]})

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        user = User(
            name=args['name'],
            email=args['email'],
            picture="standart.png"
        )
        user.set_password(args["password"])
        db_sess.add(user)
        db_sess.commit()
        return jsonify({'id': user.id})


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    news = session.query(User).get(user_id)
    if not news:
        abort(404, message=f"User {user_id} not found")


parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('email', required=True)
parser.add_argument('password', required=True)
