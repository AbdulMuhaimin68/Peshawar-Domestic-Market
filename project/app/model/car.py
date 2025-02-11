from project.app.db import db
from sqlalchemy import Enum
from sqlalchemy.sql import func

class Car(db.Model):
    __tablename__ = "car"
    
    car_id = db.Column(db.Integer, primary_key=True)
    car_model = db.Column(db.String(100), nullable=False)
    car_price = db.Column(db.String(100), nullable=False)
    car_description = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    user = db.relationship("User", back_populates="car")
    contact = db.relationship("Contact", back_populates="car")
