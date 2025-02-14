from marshmallow import fields, Schema, validates, ValidationError

class ContactSchema(Schema):
    
    message = fields.String(required=True)
    user_id = fields.Integer(required=True)
    car_id = fields.Integer(required=True)