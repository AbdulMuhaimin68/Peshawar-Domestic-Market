from marshmallow import Schema, fields

class CommentSchema(Schema):
    comment_id = fields.Integer()
    comment = fields.String(required=True)
    user_id = fields.Integer(required=True)
    blog_id = fields.Integer(required=True)

class GetCommentById(CommentSchema):
    pass

class GetAllComments(CommentSchema):
    pass

class UpdateCommentById(CommentSchema):
    comment_id = fields.Integer(required=True)