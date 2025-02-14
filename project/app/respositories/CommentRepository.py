from project.app.db import db
from project.app.model.comment import Comment
from sqlalchemy.orm import scoped_session


class CommentRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def post_comment(args:dict, session:scoped_session):
        try:
            comment = Comment(
                **args
            )
            session.add(comment)
            session.commit()
            return comment
        
        except Exception as e:
            session.rollback()
            raise e
            