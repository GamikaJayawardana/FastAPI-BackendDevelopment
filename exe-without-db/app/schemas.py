from enum import Enum
from pydantic import BaseModel, Field

class ShipmentStatus(str, Enum):
    placed = "Placed"
    in_transit = "In Transit"
    delivered = "Delivered"

class Shipment(BaseModel):
    content: str = Field(min_length=1, max_length=100)
    weight: float = Field(lt=25, ge=1)
    status: str = Field(min_length=1, max_length=100)
    destination: int | None = Field(default=None)

class BaseShipment(BaseModel):
    content: str
    weight: float = Field(lt=25, ge=1)
    destination: int 

class ShipmentRead(BaseShipment):
    status: ShipmentStatus
    

class ShipmentCreate(BaseModel):
    pass

class ShipmentUpdate(BaseModel):
    status: ShipmentStatus
