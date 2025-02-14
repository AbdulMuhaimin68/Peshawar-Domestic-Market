from project.app.schemas.CommentSchema import CommentSchema
from project.app.respositories.CommentRepository import CommentRepository

class CommentBLC:
    
    @staticmethod
    def add_comment(args):
        session = CommentRepository.get_session()
        try:
            comments = CommentRepository.post_comment(args, session)
            session.commit()
            commentSchema = CommentSchema()
            res = commentSchema.dump(comments)
            return res
        except Exception as e:
            session.rollback()
            raise e