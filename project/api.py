# from project.app.models.User import User
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask import Flask,jsonify
from datetime import timedelta
from project.app.db import db
from project.blueprint.User import bp as user_bp
# from project import config

# from project.blueprint.employee import bp as employee_bp


# from project.blueprints.admin import bp as admin_bp
# from project.blueprints.rooms import bp as rooms_bp


def create_app():
    
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{config.DB_USER}:{config.DB_PWD}@{config.DB_URL}:{config.DB_PORT}/{config.DB_NAME}"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:smartforum123@localhost/pdm"
    # app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
    app.config["JWT_SECRET_KEY"] = "khanmuhain"
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=30)
    
    migrate = Migrate()
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app=app, db=db) 
    jwt = JWTManager(app)
    
    # @jwt.user_lookup_loader
    # def user_lookup(jwt_header: dict, jwt_payload: dict):
    #     username = jwt_payload.get("sub")
    #     user = User.query.filter(User.username == username).first() 
    #     return user
        
    # @jwt.additional_claims_loader
    # def adding_additional_claims(identity):
    #     user = ... # fetch user
        
    #     return {"role": user.role}
    
    @app.errorhandler(422)
    def webargs_error_handler(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code
        
    # app.register_blueprint(employee_bp)
    app.register_blueprint(user_bp)
    # app.register_blueprint(posts_bp)
    with app.app_context():
        db.create_all()

    return app