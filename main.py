from fastapi import FastAPI

app=FastAPI()

#Define root end point
@app.get("/") #http://127.0.0.1:8000
def read_root():
    return{"message":"Hello, World!"}

#Define another endpoint with a parameter
@app.get("/hello/{name}")
def say_hello(name:str):
    return{"message":f"Hello, {name}!"}
