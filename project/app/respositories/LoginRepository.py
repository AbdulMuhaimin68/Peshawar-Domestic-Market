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
        
        if not user or not user.check_password(password):  # ✅ Fixed logic
            return {"message" : "Invalid email or password"}
        

        print(f"User logging in: {user.email}, Role: {user.role}")  # Debugging output
        
        access_token = create_access_token(identity=user.email, expires_delta=timedelta(days=30))
        
        return access_token

