from random import randrange
from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

#post schema or outline
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

#hard coded posts for examples, usually would be stored in a database
my_posts = [
    {'title': 'title of post', 'content': 'content of post', 'id': 1},
    {'title': 'coding is hard', 'content': 'this is a really hard skill to learn, why did I do it?', 'id': 2}
]

#function to find posts in the my_posts list
def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post
 
#function to find the index of the posts in my_posts
def find_index_post(id):
    for index, post in enumerate(my_posts):
        if post['id'] == id:
            return index

        
#Be careful of ordering requests, fastapi looks at requests top down; path parameters could match other paths by accident

#async is optional, only needed for asyncronous tasks, tasks that take a certain amount of time: api calls, talking to database
#root name is arbatrary; keep names descriptive
#path operation or route; 2 parts the function and the decorator
@app.get("/") #the decorator
async def root(): #the function
    return {"message": "hello"}

#get request to get posts from the practice database (my_posts)
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

#post request to create posts using the Post boilerplate and new_post as the variable
#turns the new_post into a dictionary, assigns the post a new id using randrange, and appends the new post my_posts list
#with a status code for a successfully created post
@app.post("/post", status_code = status.HTTP_201_CREATED)
def create_posts(new_post: Post):
    new_post_dict = new_post.model_dump()
    new_post_dict['id'] = randrange(0, 10000)
    my_posts.append(new_post_dict)
    return {"data": new_post_dict}

#get singular post
#path parameters *{id}* are returned as strings
#id: int validates that the paremeter entered is an int
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'post with id {id} was not found')
    print(post)
    return {f'{id}': post}

#delete request to remove a post from our my_posts list
@app.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="post not found")
    my_posts.pop(index)
    return Response(status_code = status.HTTP_204_NO_CONTENT)

#put request or an update
#finds the index of the post with the same id in my_posts, if not there raise an exception
#turn the updated post into a dictionary, give the updated post the same id, place the updated post in the same index 
@app.put("/posts/{id}", status_code= status.HTTP_201_CREATED)
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="post not found")
    
    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict

    print(my_posts)
    return {'Post updated': post_dict}

