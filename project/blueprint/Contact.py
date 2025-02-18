from project.app.schemas.ContactSchema import ContactSchema, GetAllContacts
from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.bl.ContactBLC import ContactBLC
from marshmallow import fields

bp = Blueprint('contact', __name__)

@bp.route('/contact', methods = ['POST'])
@use_args(ContactSchema(), location='json')
def contact_post(args):
    
    try:
        res = ContactBLC.add_contact(args)
        return jsonify({"message" : "message sent successfully!", "result" : res}), 201
    except Exception as e:
        raise e
    
@bp.route("/contact", methods=['GET'])
@use_args({"contact_id": fields.Int()}, location='query')
def get_users(args):
    contact_id = args.get('contact_id')  # Extracts the integer correctly

    if contact_id:
        try:
            result = ContactBLC.get_contact_by_id(contact_id)  # Pass integer to get_contact_by_id
            return jsonify({"message": "Contact by id!", "result": result}), 200
        except Exception as e:
            return jsonify({"error!": str(e)}), 500
    else:
        try:
            result = ContactBLC.get_all_contacts()
            schema = GetAllContacts(many=True)
            res = schema.dump(result)
            return jsonify({"message": "All contacts", "result": res}), 200
        except Exception as e:
            return jsonify({"error!": str(e)}), 404

