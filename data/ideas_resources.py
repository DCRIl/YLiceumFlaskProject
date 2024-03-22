import datetime

from flask import jsonify
from flask_restful import Resource, abort, reqparse
from . import db_session
from .ideas import Ideas


class IdeasResource(Resource):
    def get(self, ideas_id):
        abort_if_ideas_not_found(ideas_id)
        session = db_session.create_session()
        ideas = session.query(Ideas).get(ideas_id)
        return jsonify({'ideas': ideas.to_dict(
            only=('title', 'content', 'user_id'))})

    def delete(self, ideas_id):
        abort_if_ideas_not_found(ideas_id)
        session = db_session.create_session()
        ideas = session.query(Ideas).get(ideas_id)
        session.delete(ideas)
        session.commit()
        return jsonify({'success': 'OK'})


class IdeasListResource(Resource):
    def get(self):
        session = db_session.create_session()
        ideas = session.query(Ideas).all()
        return jsonify({'ideas': [item.to_dict(
            only=('title', 'content', 'autor.name')) for item in ideas]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        ideas = Ideas(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            created_date=datetime.datetime.now()
        )
        session.add(ideas)
        session.commit()
        return jsonify({'id': ideas.id})


def abort_if_ideas_not_found(ideas_id):
    session = db_session.create_session()
    ideas = session.query(Ideas).get(ideas_id)
    if not ideas:
        abort(404, message=f"Ideas {ideas_id} not found")


parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('content', required=True)
parser.add_argument('user_id', required=True, type=int)
