from flask import Blueprint, jsonify
from project.app.bl.UserBLC import UserBLC
from project.app.schemas.UserSchema import UserSchema
from webargs.flaskparser import use_args, parser
import logging

from flask import request
from marshmallow import ValidationError

bp = Blueprint("user", __name__)

@bp.route("/register", methods=["POST"])
@use_args(UserSchema(), location="json")
def register_user(args):
    
    try:
        res = UserBLC.add_user(args)
        # breakpoint()
        return jsonify({"message": "User added successfully", "result": res}), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

