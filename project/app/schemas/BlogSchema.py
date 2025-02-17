from marshmallow import fields, Schema, ValidationError

class BlogSchema(Schema):
    
    blog_id = fields.Integer(dump_only = True)
    title = fields.String(required = True)
    content = fields.String(required=True)
    image_url = fields.String(required=True)
    user_id = fields.Integer(required=True)
    
class GetAllBlogs(BlogSchema):
    pass

class UpdateCarDetailsById(BlogSchema):
    blog_id = fields.Integer(required = True)
    
class DeleteBlogById(BlogSchema):
    blog_id = fields.Integer(required = True)