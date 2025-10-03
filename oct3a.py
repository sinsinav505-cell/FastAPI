#  Question 2: Task Manager API
# -------------------------------------------------
# Task:
# Build a FastAPI CRUD API to manage a "to-do task list".
#
# Endpoints to create:
# ⿡ POST /addtask
#     - Accepts JSON body:
#       {
#         "title": "Do homework",
#         "status": "pending"
#       }
#     - Adds a new task to the list.
#
# ⿢ GET /gettasks
#     - Returns all tasks.
#
# ⿣ PUT /updatetask/{index}
#     - Updates a task's title or status by index.
#
# ⿤ DELETE /deletetask/{index}
#     - Deletes a task from the list.
#
# Requirements:
# - Each task should have:
#     - "title" (string)
#     - "status" (string) — must be either "pending" or "completed".
# - Validate that the status value is valid before adding or updating.


from fastapi import FastAPI,Request

app=FastAPI()

todo=[]


#post
@app.post("/addlist")
async def add_list(request:Request):
    data = await request.json()

    title = data.get("title")
    status = data.get("status")

    new_todo = {"title":title , "status":status}
    todo.append(new_todo)

    return{f"added {title} with {status}"}


#get
@app.get("/getlist")
def get_list():
    return{"to do list":todo}


#put
@app.put("/update/{index}")
async def update_list(index:int,request:Request):

    if index < 0 or index >=len(todo):
        return{"error":"Invalid index"}
    
    data = await request.json()

    todo_list=data.get("todo")
    todo[index] = todo_list

    return{f"updated:{todo_list}"}


#delete
@app.delete("/delete/{index}")
async def delete_list(index:int,request:Request):

    if index < 0 or index >=len(todo):
        return{"error":"Invalid index"}
    
    deleted = todo.pop(index)
    return{f"Deleted:{deleted}"}
