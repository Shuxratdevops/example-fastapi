from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    #return {"message": "succesfull created posts"}
    return {"new_post": f"title {payload['title']} content: {payload['content']}"}
