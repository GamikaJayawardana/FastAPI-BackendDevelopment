import datetime

from sqlmodel import Enum, Field, SQLModel

class ShipmentStatus(str, Enum):
    placed = "Placed"
    in_transit = "In Transit"
    delivered = "Delivered"


class Shipment(SQLModel, table=True):
    __tablename__ = "shipment"

    id: int = Field(default=None, primary_key=True)
    content: str
    weight: float = Field(le=25)
    destination: str
    status: ShipmentStatus = Field(default=ShipmentStatus.placed)
    estimated_delivery: datetime.date

