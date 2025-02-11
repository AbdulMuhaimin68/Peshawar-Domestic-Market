from project.app.db import db
from sqlalchemy.sql import func

class Comment(db.Model):
    __tablename__ = "comment"
    
    comment_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    user = db.relationship("User", back_populates="comment")

    blog_id = db.Column(db.Integer, db.ForeignKey("blog.blog_id"), nullable=False)
    blog = db.relationship("Blog", back_populates="comment")
