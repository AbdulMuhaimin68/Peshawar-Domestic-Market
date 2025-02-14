from project.app.schemas.CarSchema import CarSchema, GetAllCars, UpdateCarDetailsById, DeleteCarDetailsById
from flask import Blueprint , jsonify
from webargs.flaskparser import use_args
from project.app.bl.CarBLC import CarBLC
from marshmallow import fields

bp = Blueprint("car", __name__)

@bp.route("/car", methods = ['POST'])
@use_args(CarSchema(), location='json')
def car_post(args):
    try:
        res = CarBLC.add_car(args)
        return jsonify({"message" : "car added successfully!", "result" : res}), 201
    except Exception as e:
        raise e
    

@bp.route("/car", methods = ['GET'])
@use_args({"car_id" : fields.Int()}, location='query')
def get_car_by_id(args):
    
    id = args.get('id')
    if id:
        try:
            res = CarBLC.get_car_by_id(args)
            if res:
                schema = CarSchema()
                result = schema.dump(res)
                return jsonify({"message" : "Get car by id", "result" : result}),201
            else:
                return jsonify({"message" : "Car Id not found"}),404
        except Exception as e:
            return jsonify({"error!" : str(e)}),500
    else:
        res = CarBLC.get_all_cars()
        if res:
            schema = GetAllCars(many=True)
            result = schema.dump(res)
            return jsonify({"message" : "All Cars Data", "result" : result}),201
        else:
            return jsonify({"message" : "Car not found!"}),500
            

@bp.route("/car", methods=['PUT'])
@use_args(UpdateCarDetailsById(), location='json')
def update_cars(args):
    try:
        res = CarBLC.update_car_details_by_id(args)
        print(type(res))  # Debugging: Check the type
        results = dict(res)
        return jsonify({"message": "Car details updated successfully!", "results": results}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@bp.route("/car", methods=["DELETE"])
@use_args({"car_id": fields.Int()}, location='json')
def delete_car_details(args):
    try:
        res = CarBLC.delet_car_details_by_id(args)

        if "error" in res:
            return jsonify(res), 500  # If error exists, return with status 500

        return jsonify({"Message": "Car details removed", "result": res}), 201  # ✅ No nested jsonify()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
