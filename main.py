from fastapi import FastAPI

app = FastAPI()

#path operation or route; 2 parts the function and the decorator
@app.get("/") #the decorator
async def root(): #the function
    return {"message": "hello"}

#async is optional, only needed for asyncronous tasks, tasks that take a certain amount of time: api calls, talking to database
#root name is arbatrary; keep names descriptive

