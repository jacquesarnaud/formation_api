from pydantic import BaseModel,Field,PositiveInt
from typing import Optional

class Herovalid():
    id: int
    name: str
    title: str
    power: str
    role: str
    image: str
    rarity: int
    active: bool

    def __init__(self,id,name,title,power,role,image,rarity,active):
        self.id = id
        self.name = name
        self.title = title
        self.power = power
        self.role = role
        self.image = image
        self.rarity =rarity
        self.active =active


class Herovalidation(BaseModel):
    id:Optional[int] = Field(default=None,)
    name: str = Field(min_length=3)
    title: str =Field(min_length=3)
    power: str = Field(min_length=3)
    role: str = Field(min_length=3)
    image: str =Field(min_length=3)
    rarity: PositiveInt = Field(gt=0, lt=10)
    active: bool 

    model_config = {
        "json_schema_extra":{
            "example": {
                "name": "Jupiterre",
                "title": "La planete",
                "power": "Énergie planetère",
                "role": "DPS",
                "image": "/images/heroes/aether.jpg",
                "rarity": 6,
                "active": True
                }
        }
    }