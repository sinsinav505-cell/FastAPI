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


#update
@app.put("/updateitems/{index}")

async def update_items(index:int,request:Request):

    if index < 0 or index >=len(items):
        return{"error":"Invalid index"}
    
    #read the new item value from the request body
    data = await request.json()
    new_item = data.get("items")
    items[index] = new_item
    return {"message":f"succesfully added {new_item}"}

@app.delete("/delete/{index}")
async def delete_items(index:int):

    #validate the index
    if index <0 or index >=len(items):
        return {"error":"Invalid index"}
    
    deleted_item = items.pop(index)

    return {"message":f"Succesfully deleted item '{deleted_item}'"}

