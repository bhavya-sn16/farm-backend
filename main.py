from fastapi import FastAPI
from contextlib import asynccontextmanager
from pymongo import MongoClient
from routes import router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
   
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




async def connectToDatabase():
    db = MongoClient("mongodb+srv://Bhavya:password4mongo@cluster0.4x3it.mongodb.net/npk.farm")
    return db

@asynccontextmanager
async def lifespan(app: FastAPI):
    dbHost = await connectToDatabase()
    app.db = dbHost
    app.sensordata = dbHost.npk.farm
    print("startup has begun!!")
    yield
    print("shutdown has begun!!")

app = FastAPI(lifespan=lifespan)
app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

