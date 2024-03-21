from flask import request
from flask.views import MethodView
from uuid import uuid4

from . import bp
from db import user, posts

# POST ROUTES

@bp.route("/post")
class PostList(MethodView):
    def post(self):
        post_data = request.get_json()
        if post_data["author"] not in user:
            return {"message": "user does not exist."}, 400
        post_id = uuid4().hex
        posts[post_id] = post_data
        return {
            "message": "Post created.",
            "post-id": post_id 
            }, 201
    def get(self):
        try:
            return list(posts.values()), 200
        except:
            return {"message": "Failed to get posts"}, 400

@bp.route("/post/<post_id>")
class Post(MethodView):
    def get(self, post_id):
        if post_id in posts:
            return posts[post_id], 200
        return {"message": "invalid post"}, 400
  
    def put(self, post_id):
        post_data = request.get_json()
    
        if post_id in posts:
             # posts[post_data["id"]] = {k:v for k,v in post_data.items() if k != "id"}
            posts[post_id] |= post_data
            return {"message": f"post: {post_id} updated"}, 201
        return {"message": "Post not found"}, 400

    def delete(self, post_id):
        post_data = request.get_json()
        post_id = post_data['id']
        if post_id not in posts:
            return { 'message' : "Invalid Post"}, 400    
        posts.pop(post_id)
        return {'message': f'Post: {post_id} deleted'}