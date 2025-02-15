from project.app.db import db
from project.app.model.blog import Blog
from sqlalchemy.orm import scoped_session

class BlogRepository:
    
    @staticmethod
    def get_session():
        return db.session()
    
    @staticmethod
    def add_blog(args:dict, session:scoped_session):
        try:
            blog = Blog(
                **args
            )
            session.add(blog)
            session.commit()
            return blog
        except Exception as e:
            raise e
        
    @staticmethod
    def get_Blog_by_id(session:scoped_session, id: int):
        if not id:
            return {"error" : "id not found"}
        res = session.query(Blog).filter(Blog.blog_id == id).first()
        return res
    
    @staticmethod
    def get_all_blogs(session:scoped_session):
        try:
            query = session.query(Blog)
            blogs = query.all()
            return blogs
        except Exception as e:
            raise e
    
    @staticmethod
    def updated_blog(blog, args:dict):
        blog.title = args.get("title", blog.title)
        blog.content = args.get("content", blog.content)
        blog.image_url = args.get("image_url", blog.image_url)
        
        return blog