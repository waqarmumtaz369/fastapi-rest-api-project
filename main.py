from fastapi import FastAPI

app = FastAPI()

# Get method for a root path
@app.get("/")
async def root():
    return {"Hello": "World"}