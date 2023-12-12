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
    try:
        affiliate = collection_name.find_one({"id": affiliate_id})
        if not affiliate:
            return {"message": "Affiliate not found"}

        # Assuming you have a function to calculate commission based on affiliate and sales amount
        commission = calculate_commission_logic(affiliate_id, sales_amount)
        return {"affiliate_id": affiliate_id, "commission": commission}
    except Exception as e:
        return {"error": f"Failed to calculate commission: {str(e)}"}
