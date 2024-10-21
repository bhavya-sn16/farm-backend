from wsgiref.util import application_uri
from fastapi import APIRouter, Depends, Request, Body, Query
from models.farmModel import SensorData
from bson import ObjectId
from fastapi.templating import Jinja2Templates
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from fastapi.responses import JSONResponse
from datetime import datetime





router = APIRouter(prefix="", tags=['SensorData'])
templates = Jinja2Templates(directory="templates")

# @router.get("/getdata")
# async def getData(request: Request)->list[SensorData]:
#     db = request.app.sensordata
    
#     response = list(db.find({}).limit(100))

#     for item in response:
#         item["_id"] = str(item["_id"])
#     return JSONResponse(content={"data": response})

@router.get("/getdata")
async def getData(request: Request, date: str = Query(None))->list[SensorData]:
    db = request.app.sensordata
    
    if not date:
        date = datetime.now().strftime("%Y/%m/%d")

    response = list(db.find({"time": {"$regex": f"^{date}"}}))
    print(date)
    for item in response:
        item["_id"] = str(item["_id"])

    
    return JSONResponse(content={"data": response})


@router.post("/device/save_log")
#async def addData(request: Request, sensordata: SensorData = Body(...)):
async def addData(request: Request):
    data = await request.json()
    print(str(data))
    #db = request.app.sensordata
    print("draw")
    response = db.insert_one(data)
    db = MongoClient("mongodb+srv://Bhavya:password4mongo@cluster0.4x3it.mongodb.net/npk.farm")
    #response = db.insert_one(SensorData.model_dump())
    #data = await request.json()
    #return {"id": str(response.inserted_id)}

# @router.delete("/{id}")
# async def deletePlayer(request: Request, id):
#     _id = ObjectId(id)
#     db = request.app.players
#     response = db.delete_one({"_id": _id})
#     return {"deleted_count": response.deleted_count}

# @router.put("/{id}")
# async def updatePlayer(request: Request, id, player: Player = Body(...)):
#     _id = ObjectId(id)
#     db = request.app.players
#     response = db.update_one({"_id": _id}, {"$set": player.model_dump()})
#     return {"updated_count": response.modified_count}
