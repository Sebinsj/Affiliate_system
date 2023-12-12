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
async def create_affiliates(affiliate:Affiliate):
    collection_name.insert_one(dict(affiliate))    

@router.get("/calculate_commission")
async def calculate_commission(affiliate_id: str, sales_amount: float):
    if affiliate_id not in collection_name.find():
        return {"message": "Affiliate not found"}

    commission = sales_amount * 0.1
    return {"affiliate_id": affiliate_id, "commission_amount": commission}
