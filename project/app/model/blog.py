from project.app.db import db

class Blog(db.Model):
    __tablename__ = "blog"
    
    blog_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    user = db.relationship("User", back_populates="blog")
    
    comment = db.relationship("Comment", back_populates="blog")
