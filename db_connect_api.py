from fastapi import FastAPI,HTTPException,status
from db import get_connection
from pydantic import BaseModel
import time

app = FastAPI()

#checking the connection of api and db

try:
    conn = get_connection()
    print("Connected successfully")
    
except Exception as e:
    print(f"Connection failed due to {e}")
    time.sleep(2)

#connection cursor with connection
cursor = conn.cursor()

class PostCreate(BaseModel):
    title : str
    content : str
    published : bool = True


@app.get("/")
def home():
    return "API running successfully"

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return posts

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post : PostCreate):
    cursor.execute("""INSERT INTO posts(title,content,published) VALUES (%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
    new_post = cursor.fetchone()
    conn.commit()
    if new_post == None:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,detail="Server under maintenance")
    return new_post

@app.get("/posts/{id}")
def get_one_post(id : int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""",(id,))
    post = cursor.fetchone()
    return post
       

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int ):
    cursor.execute("DELETE FROM posts WHERE id = %s RETURNING * ",(id,))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no post found with id {id}")

    return deleted_post


@app.put("/posts/{id}")
def update_post(id : int , post : PostCreate):
    cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * ",(post.title,post.content,post.published,id))
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post with id:{id} does not exist")

    return updated_post
