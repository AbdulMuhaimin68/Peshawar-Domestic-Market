from flask import Blueprint, jsonify
from project.app.schemas.BlogSchema import BlogSchema, GetAllBlogs
from webargs.flaskparser import use_args
from project.app.bl.BlogBLC import BlogBLC
from marshmallow import fields


bp = Blueprint('blogs', __name__)

@bp.route("/blogs", methods = ['POST'])
@use_args(BlogSchema(), location='json')
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
