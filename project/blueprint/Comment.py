from project.app.schemas.CommentSchema import CommentSchema, GetAllComments, UpdateCommentById
from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.bl.CommentBLC import CommentBLC
from marshmallow import fields
from flask_jwt_extended import jwt_required

bp = Blueprint('comment', __name__)

@bp.route("/comments", methods = ['POST'])
@use_args(CommentSchema(), location='json')
@jwt_required()
def post_Comment(args):
    try:
        res = CommentBLC.add_comment(args)
        return jsonify({"message" : "comment added successfully!", "result" : res}),201
    except Exception as e:
        raise e

@bp.route("/comments", methods=['GET'])
@use_args({"comment_id": fields.Int()}, location='query')
def get_comment(args):
    id = args.get("comment_id")
    
    try:
        if id:
            res = CommentBLC.get_comments_by_id(args)
            if not res:
                return jsonify({"error": "Comment not found"}), 404
            return jsonify({"message": "Comment found", "result": res}), 200
        else:
            res = CommentBLC.get_all_comments()
            if res:
                schema = GetAllComments(many=True)
                return jsonify({"message": "All comments", "result": schema.dump(res)}), 200
            return jsonify({"error": "No comments found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route("/comments", methods=['PUT'])
@use_args(UpdateCommentById(), location='json')
def update_comment(args):
    try:
        res = CommentBLC.update_comment_by_id(args) 
        if "error" in res:
            return jsonify(res), 404 
        return jsonify(res), 200 
    except Exception as e:
        return jsonify({"error": str(e)}), 500

        
@bp.route("/comments", methods=['DELETE'])
@use_args({"comment_id": fields.Int()}, location='json')
def delete_comment(args):
    try:
        res = CommentBLC.comment_deletion(args)

        if "error" in res:
            return jsonify(res), 404  

        return jsonify(res), 200  
    except Exception as e:
        return jsonify({"error": str(e)}), 500

        