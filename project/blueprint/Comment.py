from project.app.schemas.CommentSchema import CommentSchema
from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.bl.CommentBLC import CommentBLC

bp = Blueprint('comment', __name__)

@bp.route("/comments", methods = ['POST'])
@use_args(CommentSchema(), location='json')
def post_Comment(args):
    try:
        res = CommentBLC.add_comment(args)
        return jsonify({"message" : "comment added successfully!", "result" : res}),201
    except Exception as e:
        raise e
