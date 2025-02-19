from project.app.model.user import User
from project.app.db import db
from flask_jwt_extended import create_access_token
from datetime import date, timedelta

class LoginRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    
    @staticmethod
    def login(args, session):
        email = args.get('email')
        password = args.get('password')
        
        user = session.query(User).filter(User.email == email).first()
        
        if not user and user.check_password(password):
            # breakpoint()
            return {"message" : "Invalid email or password"}
        
        access_token = create_access_token(identity=email, expires_delta=timedelta(days = 30))
        return access_token
