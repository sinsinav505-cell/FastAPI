#  Question 1: Book Management API
# -------------------------------------------------
# Task:
# Create a FastAPI app to manage a simple "book collection".
# Implement full CRUD operations as described below:
#
# Endpoints to create:
# ⿡ POST /addbook
#     - Accepts JSON body:
#       {
#         "title": "Book Name",
#         "author": "Author Name"
#       }
#     - Adds the book to a temporary list.
#
# ⿢ GET /getbooks
#     - Returns all stored books.
#
# ⿣ PUT /updatebook/{index}
#     - Updates a book's details (title or author) by index.
#
# ⿤ DELETE /deletebook/{index}
#     - Deletes a book from the list by index.
#
# Requirements:
# - Each book should have:
#     - "title" (string)
#     - "author" (string)
# - Store all books in a Python list.

from fastapi import FastAPI,Request

app = FastAPI()

books=[]

#post
@app.post("/addbook")
async def add_book(request:Request):
    data = await request.json()

    title = data.get("title")
    author = data.get("author")

    collection={"title":title , "author":author}
    books.append(collection)

    return {f"successfully added {title} by {author}"}

#get
@app.get("/getbook")
def get_book():
    return{"books collection":books}

#put
@app.put("/updatebook/{index}")
async def update_book(index:int,request:Request):
    if index < 0 or index >=len(books):
        return{"error":"Invalid index"}
    
    data = await request.json()
    new_book = data.get("books")
    books[index]=new_book
    return{f"updated :{new_book}"}


#delete
@app.delete("/delete/{index}")
async def delete_book(index:int):
    if index < 0 or index >=len(books):
        return {"error":"Invalid index"}

    deleted_book = books.pop(index)
    return{f"Deleted{deleted_book}"}

    





