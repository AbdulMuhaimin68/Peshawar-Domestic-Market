from project.app.model.user import User
from project.app.db import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session
from werkzeug.security import generate_password_hash

class UserRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_user(args: dict, session: scoped_session):
        try:
            hashed_password = generate_password_hash(args['password'])

            user = User(
                username=args['username'], 
                email=args['email'], 
                password=hashed_password, 
                role=args['role']
            )
            
            session.add(user)
            session.commit()  

            return user
        except IntegrityError as e:
            session.rollback()
            raise ValueError("User with this email or username already exists.")
        except Exception as e:
            session.rollback()
            raise e
