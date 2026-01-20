# starting the day 1 for Fast api working and learning from free code camp

from fastapi import FastAPI , HTTPException, status
from pydantic import BaseModel #importing for the basic constraint schema of post request

#creating instance for fastapi
app = FastAPI()

class PostCreate(BaseModel):
    title : str #this is a way of predefing the required type of content from the user 
    content : str
    funtionality:bool = True #this is optional as it contains default value

#creating a function to find id for updation and deletion 
def find_index(id: int):
    for index, post in enumerate(my_posts):
        if post["id"] == id:
            return index
    return None


#creating a false storage since not connected to database
my_posts = [{"title":"title hi khede","content":"first post ","id":1},
            {"title":"title 2 hi khede","content":"second post ","id":2}]

#creating the first route 
@app.get("/")
def home():
    return {"message":"server started"}

#reading or fetching the posts
@app.get("/posts")
def read_posts():
    return {"posts":my_posts}

#uploading the posts
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post: PostCreate):
    new_id = my_posts[-1]["id"] + 1 if my_posts else 1
    post_dict = post.model_dump()
    post_dict["id"] = new_id
    my_posts.append(post_dict)
    return post_dict

#updating the posts
@app.put("/posts/{id}")
def updating_post(id : int ,post: PostCreate):
    index = find_index(id)
    
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    

    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return my_posts[index]

#deleting the posts
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index(id)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")

    my_posts.pop(index)
    return None

