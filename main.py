from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

#path operation or route; 2 parts the function and the decorator
@app.get("/") #the decorator
async def root(): #the function
    return {"message": "hello"}

@app.get("/posts")
def get_posts():
    return {"Pretend there are posts here"}

@app.post("/createpost")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title {payload['title']} content {payload['content']}"}


#async is optional, only needed for asyncronous tasks, tasks that take a certain amount of time: api calls, talking to database
#root name is arbatrary; keep names descriptive

