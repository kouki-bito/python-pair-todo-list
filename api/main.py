from fastapi import FastAPI

app=FastAPI()
@app.get("/hello")
async def hello():
    return {"message":"hello word!"}

DB_URL="mysql+pymysql://root@localhost:3306/demo?charset=utf8"