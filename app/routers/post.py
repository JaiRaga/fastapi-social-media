from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import engine, get_db

router = APIRouter(
  prefix = "/posts",
  tags = ["Posts"]
)

# Get Posts
@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
  # cursor.execute("""SELECT * FROM posts """)
  # posts = cursor.fetchall()
  posts = db.query(models.Post).all()
  return posts

# Get Single Post
@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
  # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
  # post = cursor.fetchone()

  post = db.query(models.Post).filter(models.Post.id == id).first()

  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {id} not found")
  return post


# Create Post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def new_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
  # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
  # new_post = cursor.fetchone()
  # conn.commit()

  print(1, post)
  print(2, post.dict())

  new_post = models.Post(**post.dict())
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  
  return new_post

# Update Post
@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
  # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))

  # updated_post = cursor.fetchone()
  # conn.commit()

  post_query = db.query(models.Post).filter(models.Post.id == id)

  found_post = post_query.first()

  if found_post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} does not exists.')

  post_query.update(post.dict(), synchronize_session=False)

  db.commit()
  
  return post_query.first()


# Delete Post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
  # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
  # deleted_post = cursor.fetchone()
  # conn.commit()

  post = db.query(models.Post).filter(models.Post.id == id)

  if post.first() == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} does not exists.')
  
  post.delete(synchronize_session=False)
  db.commit()

  return Response(status_code=status.HTTP_204_NO_CONTENT)