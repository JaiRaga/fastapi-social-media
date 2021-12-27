from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
import time

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# while True:
#   try:
#     conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="HK2556BM941", cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print('Database Connection was Successful')
#     break
#   except Exception as error:
#     print('Database Connectio Failed')
#     print('Error: ', error)
#     time.sleep(2)

class Post(BaseModel):
  title: str
  content: str
  published: bool = True

# Test db connection
@app.get("/sqlalchemy")
def test_db(db: Session = Depends(get_db)):
  posts = db.query(models.Post).all()
  return {"data": posts}

# Get Posts
@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
  # cursor.execute("""SELECT * FROM posts """)
  # posts = cursor.fetchall()
  posts = db.query(models.Post).all()
  return {"data": posts}

# get Latest Post
# @app.get("/posts/latest")
# def get_latest_posts():
#   posts = findLatest()
#   return {"posts": posts}


# Get Single Post
@app.get("/posts/{id}")
def get_post(id: int):
  # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
  # post = cursor.fetchone()
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {id} not found")
  return {"post": post}


# Create Post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def new_post(post: Post, db: Session = Depends(get_db)):
  # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
  # new_post = cursor.fetchone()
  # conn.commit()

  print(post)
  new_post = models.Post(**post.dict())
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  
  print(new_post)
  return {"data": new_post}

# Update Post
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
  # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))

  # updated_post = cursor.fetchone()
  # conn.commit()

  if updated_post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} does not exists.')
  return {"posts": updated_post}


# Delete Post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
  # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
  # deleted_post = cursor.fetchone()
  # conn.commit()

  if deleted_post == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post with id {id} does not exists.')
  
  return Response(status_code=status.HTTP_204_NO_CONTENT)
