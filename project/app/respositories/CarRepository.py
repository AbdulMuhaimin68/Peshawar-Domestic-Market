from project.app.db import db
from project.app.model.car import Car
from sqlalchemy.orm import scoped_session

class CarRepository:
    
    @staticmethod
    def get_session():
        return db.session
    
    def add_car(args:dict, session:scoped_session):
        try:
            car = Car(**args)
            session.add(car)
            session.commit()
            return car
        
        except Exception as e:
            raise e 
    
    @staticmethod
    def get_car_By_id(session:scoped_session, id:int):
        if not id:
            return {"error!" : "Car ID not found"}
        res = session.query(Car).filter(Car.car_id == id).first()
        return res
    
    @staticmethod
    def get_all_cars(session:scoped_session):
        try:
            query = session.query(Car)
            car = query.all()
            return car
        except Exception as e:
            raise e
    
    @staticmethod
    def update_car_details(car,args:dict):
        car.car_model = args.get("car_model", car.car_model)
        car.car_price = args.get("car_price", car.car_price)
        car.car_descrition = args.get("car_description", car.car_description)
        car.image_url = args.get("image_url", car.image_url)
        return car
    
    @staticmethod
    def delete_car_details(args, session: scoped_session):
        id = args.get("car_id")
        try:
            result = session.query(Car).filter(Car.car_id == id).first()

            if result is None:
                return {"error": "Car not found"}

            deleted_car = {
                "car_id": result.car_id,
                "car_model": result.car_model,
                "car_price": result.car_price,
                "image_url": result.image_url
            }

            session.delete(result)
            session.commit()
            session.flush()

            return deleted_car  
        except Exception as e:
            session.rollback()
            raise e
