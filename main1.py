# Root Endpoint ("/")
#    - Return a welcome message like:
#      {"message": "Welcome to the Math API!"}


from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def fun():
    return{"message":"Welcome to the Math API"}



#
#  Multiplication Endpoint ("/multiply/{number}")
#    - Accept a number from the URL path.
#    - Return the result of that number multiplied by 5.
#    - Example:
#        Request: GET /multiply/6
#        Response: {"number": 6, "result": 30}

@app.get("/multiply/{number}")
def fun1(number:int):
    result=number*5
    return{"number":{number},"result":{result}}



#  Square Endpoint ("/square/{number}")
#    - Accept a number from the URL path.
#    - Return the square of that number.
#    - Example:
#        Request: GET /square/4
#        Response: {"number": 4, "result": 16}

@app.get("/square/{number}")
def fun2(number:int):
    result=number**2
    return{"number":{number}, "result":{result}}

