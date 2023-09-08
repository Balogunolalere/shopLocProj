
from pydantic import BaseModel
from typing import Optional

class Shop(BaseModel):
    id: str = None 
    name: str
    description: str = None
    latitude: float 
    longitude: float

    class Config:
        json_schema_extra = {
            "example": {
                "id": "1",
                "name": "Shop Example",
                "description": "An example shop", 
                "latitude": 45.5236,
                "longitude": -122.6750,
            }
        }

class ShopCreate(BaseModel):
    id: str = None
    name: str
    description: str = None
    latitude: float 
    longitude: float

    class Config:
        json_schema_extra = {
            "example": {
                "id": "1",
                "name": "Shop Example",
                "description": "An example shop", 
                "latitude": 45.5236,
                "longitude": -122.6750,
            }
        }

class ShopUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Shop Example",
                "description": "An example shop", 
                "latitude": 45.5236,
                "longitude": -122.6750,
            }
        }

class ShopDelete(BaseModel):
    id: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": "1",
            }
        }

class ShopList(BaseModel):
    shops: list[Shop]

    class Config:
        json_schema_extra = {
            "example": {
                "shops": [
                    {
                        "id": "1",
                        "name": "Shop Example",
                        "description": "An example shop", 
                        "latitude": 45.5236,
                        "longitude": -122.6750,
                    },
                    {
                        "id": "2",
                        "name": "Shop Example 2",
                        "description": "An example shop 2", 
                        "latitude": 45.5236,
                        "longitude": -122.6750,
                    },
                ]
            }
        }

