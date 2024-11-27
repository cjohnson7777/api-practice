from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel #helps develop schemas

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


#path operation or route; 2 parts the function and the decorator
@app.get("/") #the decorator
async def root(): #the function
    return {"message": "hello"}

@app.get("/posts")
def get_posts():
    return {"Pretend there are posts here"}

@app.post("/post")
def create_posts(new_post: Post):
    print(new_post.dict())    
    return {"data": new_post}


#async is optional, only needed for asyncronous tasks, tasks that take a certain amount of time: api calls, talking to database
#root name is arbatrary; keep names descriptive

