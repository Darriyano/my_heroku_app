from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.new_resourses import abort_if_news_not_found
from data.users import User
from data.reqparse import parser


def abort_if_users_not_found(user_id):
    session = db_session.create_session()
    news = session.query(User).get(user_id)
    if not news:
        abort(404, message=f"User {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify({
            'user':
                [users.to_dict(
                    only=('id', 'name', 'about', 'email', 'hashed_password', 'created_date', 'news'))
                ]
        }
        )

    def delete(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        news = session.query(User).get(id)
        session.delete(news)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify(
            {
                'user':
                    [item.to_dict(
                        only=('id', 'name', 'about', 'email', 'hashed_password', 'created_date', 'news'))
                        for item in users
                    ]
            }
        )

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            id=args['id'],
            name=args['name'],
            about=args['about'],
            email=args['email'],
            hashed_password=args['hashed_password'],
            created_date=args['created_date'],
            news=args['news']
        )
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})
