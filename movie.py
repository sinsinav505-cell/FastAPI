# 🧑‍🎓 Question 3: Movie Collection API
# -------------------------------------------------
# Task:
# Create a FastAPI app to manage a "movie collection".
#
# Endpoints to create:
# ⿡ POST /addmovie
#     - Accepts JSON body:
#       {
#         "name": "Inception",
#         "rating": 9
#       }
#     - Adds a new movie to the list.
#
# ⿢ GET /getmovies
#     - Returns all movies.
#
# ⿣ PUT /updatemovie/{index}
#     - Updates a movie's name or rating by index.
#
# ⿤ DELETE /deletemovie/{index}
#     - Deletes a movie by index.
#
# Requirements:
# - Each movie should have:
#     - "name" (string)
#     - "rating" (integer between 1 and 10)
# - If the rating is outside this range, return an error message.


from fastapi import FastAPI,Request

app = FastAPI()

movie=[]


#post
@app.post("/addmovie")
async def add_movie(request:Request):
    
    data = await request.json()

    name = data.get("name")
    rating = data.get("rating")

    collection = {"name":name, "rating" : rating}
    movie.append(collection)

    return{f"added:{movie}"}



#get
@app.get("/getmovie")
def get_movie():

    return{"movie collections":movie}


#put
@app.put("/updatemovie/{index}")
async def update_movie(index:int,request:Request):

        data = await request.json()

        new_movie=data.get("mo")
        movie[index] = new_movie

        return {f"updated{new_movie}"}


#delete
@app.delete("/deletemovie/{index}")
async def delete_movie(index:int):
     
     deleted=movie.pop(index)
     return{f"deleted{deleted}"}







    
