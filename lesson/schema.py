from pydantic import BaseModel

class Product_post(BaseModel):
    title: str
    content: str
    published: bool = True

class Post_detail(BaseModel):
    id:int
    title: str
    content: str
    published: bool = True