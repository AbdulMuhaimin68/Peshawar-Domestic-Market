from marshmallow import Schema, fields, ValidationError, validates

from marshmallow import validates, ValidationError

class UserSchema(Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    role = fields.String(required=True)

    @validates("username")
    def validate_password(self, value):
        if not value and value.strip() == "":
            raise ValidationError("Password cannot be empty.")

