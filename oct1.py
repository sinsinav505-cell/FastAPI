from fastapi import FastAPI,Request

app = FastAPI()

items = []

@app.post("/additems")

async def add_items(request:Request):
    #read the request body as json
    data = await request.json()  
    
    #extract the item from the json body
    item = data.get("item") 

    #store it in the temporary list
    items.append(item)

    #return a success message
    return {"message":f"successfully added item{item}"}

@app.get("/getitems")
def get_items():
    return{"items":items}

