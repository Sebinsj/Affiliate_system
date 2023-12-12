from pydantic import BaseModel

class Affiliation_system(BaseModel) :
    id:int
    name:str
    email