from marshmallow import fields, validates, Schema

class CommentSchema(Schema):
    
    content = fields.String(required=True)
    user_id = fields.Integer(required=True)
    blog_id = fields.Integer(required=True)