from pydantic import BaseModel, Field
from app.database.models import ShipmentStatus

class Shipment(BaseModel):
    content: str = Field(min_length=1, max_length=100)
    weight: float = Field(lt=25, ge=1)
    status: ShipmentStatus


class BaseShipment(BaseModel):
    content: str
    weight: float = Field(lt=25, ge=1)
    

class ShipmentRead(BaseShipment):
    status: ShipmentStatus
    

class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseShipment):
    status: ShipmentStatus
