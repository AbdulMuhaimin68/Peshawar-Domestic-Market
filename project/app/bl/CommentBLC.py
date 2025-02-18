from project.app.schemas.CommentSchema import CommentSchema
from project.app.respositories.CommentRepository import CommentRepository
from flask import jsonify

class CommentBLC:
    
    @staticmethod
    def add_comment(args):
        session = CommentRepository.get_session()
        try:
            comment = CommentRepository.post_comment(args, session)
            session.commit()
            return CommentSchema().dump(comment)
        except Exception as e:
            session.rollback()
            return {"error": str(e)}
        
    @staticmethod  
    def get_comments_by_id(args: dict):
        session = CommentRepository.get_session()
        comment_id = args.get("comment_id")  

        if not comment_id:
            return {"error": "Comment ID is required"}

        try:
            comment = CommentRepository.get_comment_by_id(comment_id, session)  
            if not comment:
                return None  
            return CommentSchema().dump(comment)
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def get_all_comments():
        session = CommentRepository.get_session()
        try:
            comments = CommentRepository.get_all_comments(session)
            return comments  
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def update_comment_by_id(args: dict):
        session = CommentRepository.get_session()
        comment_id = args.get("comment_id")

        if not comment_id:
            return {"error": "Comment ID is required"}

        try:
            comment = CommentRepository.get_comment_by_id(comment_id, session) 
            if not comment:
                return {"error": "Comment not found"}

            updated_comment = CommentRepository.update_comment_by_id(comment, args)
            session.commit()

            schema = CommentSchema()
            return {"message": "Comment updated successfully", "result": schema.dump(updated_comment)}

        except Exception as e:
            session.rollback()
            return {"error": str(e)}
        
    @staticmethod
    def comment_deletion(args: dict):
        session = CommentRepository.get_session()
        try:
            comment = CommentRepository.delete_comment_by_id(args, session)
            if comment:
                return {"message": "Comment deleted successfully!", "deleted_comment": comment}
            else:
                return {"error": "No comment with the given ID found"}, 404
        except Exception as e:
            return {"error": str(e)}, 500


