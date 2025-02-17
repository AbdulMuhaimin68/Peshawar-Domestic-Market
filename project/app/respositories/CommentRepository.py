from project.app.db import db
from project.app.model.comment import Comment
from sqlalchemy.orm import scoped_session
from project.app.schemas.CommentSchema import CommentSchema

class CommentRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def post_comment(args: dict, session: scoped_session):
        try:
            comment = Comment(**args)
            session.add(comment)
            session.commit()
            return comment
        except Exception as e:
            session.rollback()
            raise e
            
    @staticmethod
    def get_comment_by_id(comment_id: int, session: scoped_session):
        try:
            return session.query(Comment).filter(Comment.comment_id == comment_id).first()
        except Exception as e:
            raise e
        
    @staticmethod
    def get_all_comments(session: scoped_session):
        try:
            return session.query(Comment).all() 
        except Exception as e:
            raise e


    @staticmethod
    def update_comment_by_id(comment: Comment, args: dict):
        try:
            comment.comment = args.get("comment", comment.comment)
            if "user_id" in args and args["user_id"] is not None:
                comment.user_id = args["user_id"]
            if "blog_id" in args and args["blog_id"] is not None:
                comment.blog_id = args["blog_id"]

            return comment
        except Exception as e:
            raise e
        
    @staticmethod
    def delete_comment_by_id(args: dict, session: scoped_session):
        comment_id = args.get("comment_id")
        
        try:
            comment = session.query(Comment).filter(Comment.comment_id == comment_id).first()
            if comment is None:
                return None  

            deleted_comment = CommentSchema().dump(comment)  
            session.delete(comment)
            session.commit()

            return deleted_comment 

        except Exception as e:
            session.rollback()
            raise e

