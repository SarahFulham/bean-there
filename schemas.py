from pydantic import BaseModel
import typing

class CafeBase(BaseModel):

    name: str
    address: str
    features: typing.Dict[str,str]

class CafeCreate(CafeBase):
    pass

class Cafe(CafeBase):
    id: int

    class Config:
        orm_mode = True

class CafeUpdate(Cafe):
    pass
