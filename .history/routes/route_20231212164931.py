from fastapi import APIRouter
from models.affiliate import Affiliate
from config.database import collection_name
from schema.schemas import list_serial
from bson 