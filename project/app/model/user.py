from project.app.db import db
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    __tablename__ = "user"
    
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')
    
    # Relationships
    car = db.relationship("Car", back_populates="user")
    contact = db.relationship("Contact", back_populates="user")
    blog = db.relationship("Blog", back_populates="user")
    comment = db.relationship("Comment", back_populates="user")
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
