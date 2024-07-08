from pydantic import BaseModel
class DoneRespose(BaseModel):
    id:int 
    class Config:
        orm_mode=True