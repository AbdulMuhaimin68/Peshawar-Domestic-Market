from flask import Blueprint, jsonify
from project.app.schemas.BlogSchema import BlogSchema, GetAllBlogs, UpdateCarDetailsById, DeleteBlogById
from webargs.flaskparser import use_args
from project.app.bl.BlogBLC import BlogBLC
from marshmallow import fields
from http import HTTPStatus
from flask_jwt_extended import jwt_required
# from project.app.decorator import admin_required

bp = Blueprint('blogs', __name__)

@bp.route("/blogs", methods = ['POST'])
@use_args(BlogSchema(), location='json')
@jwt_required()
# @admin_required()
def blog(args):
    try:
        res = BlogBLC.add_blog(args)
        return jsonify({"message" : "blog added Successfully!", "result" : res}),201
    except Exception as e:
        return jsonify({"error!" : str(e)})
    
    
@bp.route("/blogs", methods=['GET'])
@use_args({"blog_id": fields.Int()}, location="query")
def get_all_blogs(args):
    id = args.get("blog_id")
    if id:
        try:
            res = BlogBLC.get_blogs_with_id(args)
            if "error" in res:
                return jsonify(res), 404  
            return jsonify({"result": res}), 200  
        except Exception as e:
            return jsonify({"error": str(e)}), 500 
    else:
        res = BlogBLC.get_all_blogs()
        if res:
            schema = GetAllBlogs(many=True)
            result = schema.dump(res)
            return jsonify({"message": "All the blogs info", "result": result}), 200
        else:
            return jsonify({"error": "No blogs found!"}), 404 

@bp.route("/blogs", methods=['PUT'])
@use_args(UpdateCarDetailsById(), location='json')
def update_blog_details(args):
    try:
        return BlogBLC.update_blog_by_id(args)  
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route("/blogs", methods = ['DELETE'])
@use_args({"blog_id" : fields.Int()}, location="json")
def delete_blog(args):
    try:
        return BlogBLC.delete_blog_by_id(args)
    except Exception as e:
        return jsonify({"error!" : str(e)}), 404