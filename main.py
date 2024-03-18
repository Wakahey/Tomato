from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/lol")
async def lol():
    return "lol"


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)