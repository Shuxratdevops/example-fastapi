from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from ..app.database import get_db
from .schema import Product_post, Post_detail
from ..app.models import Post

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/main",
    tags=['salom']
)

@router.get('/salom')
def main():
    return {'detail':'Hello world'}

@router.post('/salom_post', response_model=Post_detail)
def post_salom(request:Product_post, db:db_dependency):
    post = Post(
        title = request.title,
        content=request.content,
        published=request.published
    )
    db.add(post)
    db.commit()
    return post
