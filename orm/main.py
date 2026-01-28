from fastapi import FastAPI, Depends, HTTPException,status
from orm.schemas import Postcreate, PostResponse
from orm.database import engine, SessionLocal, Base
from orm.model_post import PostCreate
from sqlalchemy.orm import Session
from sqlalchemy import select

# creating tables 
Base.metadata.create_all(bind=engine)

#creating instance
app = FastAPI()

#creating home route
@app.get("/")
def home():
    return {"message":"Fast api and sql alchemy running"}

#creating CRUD routes with db using sqlalchemy
@app.get("/posts")



