from marshmallow import fields,Schema, ValidationError, validates

class CarSchema(Schema):
    
    car_model = fields.String(required=True)
    car_price = fields.String(required=True)
    car_description = fields.String(required=True)
    image_url = fields.String(required=True)