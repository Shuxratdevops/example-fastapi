from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
 

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(new_post: Post):
    #print(new_post.title)
    #print(new_post.content)
    print(new_post)
    return {"data": "new post"}