from project.app.respositories.UserRepository import UserRepository
from project.app.schemas.UserSchema import UserSchema
from flask import jsonify
from http import HTTPStatus

class UserBLC:

    @staticmethod
    def add_user(args: dict):
        session = UserRepository.get_session()
        try:
            users = UserRepository.add_user(args, session)
            session.commit() 
            user_schema = UserSchema()
            result = user_schema.dump(users)
            return result
        except Exception as e:
            session.rollback()
            raise e
