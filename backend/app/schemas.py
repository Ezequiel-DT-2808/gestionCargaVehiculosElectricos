from pydantic import BaseModel

class StationBase(BaseModel):
    name: str
    location: str
    max_kw: float
    is_active: bool = True

class StationCreate(StationBase):
    pass

class StationUpdate(BaseModel):
    is_active: bool

class StationOut(StationBase):
    id: int
    class Config:
        orm_mode = True
