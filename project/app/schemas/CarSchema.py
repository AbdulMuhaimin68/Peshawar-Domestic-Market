from marshmallow import fields,Schema, ValidationError, validates

class CarSchema(Schema):
    
    car_id = fields.Integer(dump_only = True)
    car_model = fields.String(required=True)
    car_price = fields.String(required=True)
    car_description = fields.String(required=True)
    image_url = fields.String(required=True)
    
class GetAllCars(CarSchema):
    pass

class UpdateCarDetailsById(CarSchema):
    car_id = fields.Integer(required = True)
    
class DeleteCarDetailsById(CarSchema):
    car_id = fields.Integer(required = True)