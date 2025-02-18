from marshmallow import fields, Schema, validates, ValidationError

class ContactSchema(Schema):
    
    contact_id = fields.Integer(dump_key = True)
    message = fields.String(required=True)
    user_id = fields.Integer(required=True)
    car_id = fields.Integer(required=True)
    
class GetAllContacts(ContactSchema):
    pass