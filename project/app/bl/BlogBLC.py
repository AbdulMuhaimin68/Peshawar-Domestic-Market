from project.app.schemas.BlogSchema import BlogSchema
from project.app.respositories.BlogRepository import BlogRepository
from flask import Flask, jsonify
from sqlalchemy.orm import scoped_session

class BlogBLC:
    
    @staticmethod
    def add_blog(args):
        session = BlogRepository.get_session()
        try:
            blogs = BlogRepository.add_blog(args, session)
            session.commit()
            blogSchema = BlogSchema()
            res = blogSchema.dump(blogs)
            return res
        except Exception as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_blogs_with_id(args:dict):
        id = args.get("blog_id")
        session = BlogRepository.get_session()
        try:
            blogs = BlogRepository.get_Blog_by_id(session, id)
            schema = BlogSchema()
            result = schema.dump(blogs)

            return {"message": "All data", "result": result}  # ✅ Return a dictionary, NOT jsonify()
        except Exception as e:
            return {"error": str(e)}  # ✅ Return a dictionary
        
    @staticmethod
    def get_all_blogs():
        session = BlogRepository.get_session()
        try:
            res = BlogRepository.get_all_blogs(session)
            return res
        except Exception as e:
            raise e
        
    @staticmethod
    def update_blog_by_id(args:dict):
        session = BlogRepository.get_session()
        try:
            blog = BlogRepository.get_Blog_by_id(session, args.get("blog_id"))
            
            result = BlogRepository.updated_blog(blog, args)
            session.add(result)
            session.commit()
            schema = BlogSchema()
            res = schema.dump(result)
            
            return jsonify({"message" : "blogs details updated" , "result" : res}),201
        except Exception as e:
            return jsonify({"error" : str(e)}),500
        
    @staticmethod
    def delete_blog_by_id(args:dict):
        session = BlogRepository.get_session()
        try:
            
            blog = BlogRepository.delete_blog(args, session)
            if blog:
                return blog
            else:
                return {"message" : "Blog not found"}
        except Exception as e:
            return {"error!" : str(e)}