from fastapi import APIRouter
from models.affiliate import Affiliate
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router =APIRouter()

@router.get("/")
async def get_affiliates():
    affiliates=list_serial(collection_name.find())
    return affiliates

@router.post("/")
async def create_    

