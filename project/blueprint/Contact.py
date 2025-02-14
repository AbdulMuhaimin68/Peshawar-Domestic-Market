from project.app.schemas.ContactSchema import ContactSchema
from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.bl.ContactBLC import ContactBLC

bp = Blueprint('contact', __name__)

@bp.route('/contact', methods = ['POST'])
@use_args(ContactSchema(), location='json')
def contact_post(args):
    
    try:
        res = ContactBLC.add_contact(args)
        return jsonify({"message" : "message sent successfully!", "result" : res}), 201
    except Exception as e:
        raise e