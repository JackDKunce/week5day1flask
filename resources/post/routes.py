from flask import request
from uuid import uuid4

from app import app
from db import user, posts

# POST ROUTES

@app.post("/post")
def create_post():
    post_data = request.get_json()
    if post_data["author"] not in user:
        return {"message": "user does not exist."}, 400
    post_id = uuid4().hex
    posts[post_id] = post_data
    return {
        "message": "Post created.",
        "post-id": post_id 
        }, 201

@app.get("/post")
def get_posts():
    try:
        return list(posts.values()), 200
    except:
        return {"message": "Failed to get posts"}, 400

@app.get("/post/<post_id>")
def get_ind_post(post_id):
    if post_id in posts:
        return posts[post_id], 200
    return {"message": "invalid post"}, 400

@app.put("/post")
def update_post():
    post_data = request.get_json()
    
    if post_data["id"] in posts:
        # posts[post_data["id"]] = {k:v for k,v in post_data.items() if k != "id"}
        posts[post_data["id"]] |= post_data
        return {"message": f"post: {post_data['id']} updated"}, 201
    return {"message": "Post not found"}, 400

@app.delete('/post')
def delete_post():
    post_data = request.get_json()
    post_id = post_data['id']
    if post_id not in posts:
        return { 'message' : "Invalid Post"}, 400    
    posts.pop(post_id)
    return {'message': f'Post: {post_id} deleted'}