#write fastapi route here

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse




app = FastAPI()








@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/jokes")
async def jokes():
    return {"message": "Jokes will be here"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",reload=False,port=8080,)





