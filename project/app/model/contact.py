from project.app.db import db
from sqlalchemy import Enum
from sqlalchemy.sql import func

class Contact(db.Model):
    __tablename__ = "contact"
    
    contact_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    user = db.relationship("User", back_populates="contact")

    car_id = db.Column(db.Integer, db.ForeignKey("car.car_id"), nullable=False)
    car = db.relationship("Car", back_populates="contact")
