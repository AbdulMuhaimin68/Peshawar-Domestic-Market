from marshmallow import Schema, fields, ValidationError, validates

from marshmallow import validates, ValidationError

class UserSchema(Schema):
    user_id = fields.Integer(dump_only = True)
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    role = fields.String(required=True)

    # @validates("password")
    # def validate_password(self, value):
    #     if not value and value.strip() == "":
    #         raise ValidationError("Password cannot be empty.")
        
class GetUserById(UserSchema):
    user_id = fields.Integer(required=True)

class GetAllUserSchema(UserSchema):  # Don't inherit UserSchema
    pass
