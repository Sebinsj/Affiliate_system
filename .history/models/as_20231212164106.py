from pydantic import BaseModel

class Affiliat(BaseModel) :
    id:int
    name:str
    email:str