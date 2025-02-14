from project.app.respositories.CarRepository import CarRepository
from project.app.schemas.CarSchema import CarSchema
from flask import jsonify

class CarBLC:
    
    @staticmethod
    def add_car(args:dict):
        session = CarRepository.get_session()
        try:
            car = CarRepository.add_car(args, session)
            session.commit()
            carSchema = CarSchema()
            res = carSchema.dump(car)
            return res
        except Exception as e:
            session.rollback()
            raise e
    
    @staticmethod
    def get_car_by_id(args):
        id = args.get('id')
        session = CarRepository.get_session()
        try:
            result = CarRepository.get_car_By_id(session, id)
            return result
        except Exception as e:
            raise e
        
    @staticmethod
    def get_all_cars():
        session = CarRepository.get_session()
        try:
            result = CarRepository.get_all_cars(session)
            return result
        except Exception as e:
            raise e
        
            
    @staticmethod
    def update_car_details_by_id(args:dict):
        session = CarRepository.get_session()
        try:
            car = CarRepository.get_car_By_id(session, args.get("car_id"))
            result = CarRepository.update_car_details(car, args)
            session.commit()
            schema = CarSchema()
            res = schema.dump(result)
            return jsonify({"message" : "car details updated", "results" : res}),201
        except Exception as e:
            raise e
    
    @staticmethod
    def delet_car_details_by_id(args: dict):
        session = CarRepository.get_session()
        # id = args.get("car_id")
        try:
            car = CarRepository.delete_car_details(args, session)
            if car:
                return car  
            else:
                return {"message": "Car ID not found!"}
        except Exception as e:
            return {"error": str(e)}  

