from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from app import oauth2
from .. import models, schemas, oauth2
from .. database import get_db


router = APIRouter(
    prefix="/posts",
    tags=['Posts'] # doc da alohida guruhlash uchun nom
)

# @router.get("/", response_model=List[schemas.Post])
# def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     # cursor.execute("""SELECT * FROM posts """)
#     # posts = cursor.fetchall()
#     print(current_user.id)
#     posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()

#     print(posts)
#     return posts
  
# @router.get("/{id}", response_model=schemas.Post)
# def get_post(id: int, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
#     # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),)) # (id),) shu vergul qanaqadir hatoni oldini olarkan , aniq sababi yo'q
#     # post =cursor.fetchone()
#     post = db.query(models.Post).filter(models.Post.id == id).first()

#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")
    
#     if post.owner_id != current_user.id: # owner_id bilan token id to'g'ri kemasa hato beradi
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#                              detail="Not authorized to perform requested action")   

#     return post

@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user),
    limit: int = 100, skip: int = 0, search: Optional[str] = ""):
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    print(limit)
    posts = db.query(models.Post).filter(models.Post.title.contains(search)). limit(limit).offset(skip).all()

    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)): #(user_id: int = Depends(oauth2.get_current_user) bu autorizatsi qimaganiga qo'ymaydi)
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s)RETURNING * """,
    #                (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    # new_post = models.Post(title=post.title, content=post.content, published=post.published)
    print(current_user.id, "ok")
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()     
    db.refresh(new_post)

    return  new_post


@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),)) # (id),) shu vergul qanaqadir hatoni oldini olarkan , aniq sababi yo'q
    # post =cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
    # delete_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:  #so'ralgan id yo'q bo'lsa hato bermaslik uschun
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    if post.owner_id != current_user.id: # owner_id bilan token id to'g'ri kemasa hato beradi
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail="Not authorized to perform requested action")
    
    post_query.delete(synchronize_session=False)
    db.commit()    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
 

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    # cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
    #                 (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None: #so'ralgan id yo'q bo'lsa hato bermaslik uschun
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail="Not authorized to perform requested action")

    # post_query.update({'title': 'hey this my update title',
    #                   'content': 'this is my update content'}, synchronize_session=False)
    post_query.update(updated_post.dict(), synchronize_session=False)
    
    db.commit()
    return  post_query.first()    

