from pydantic import BaseModel

class Affiliate(BaseModel) :
    id:int
    name:str
    email:str