from fastapi import APIRouter, HTTPException

from app.database.session import SessionDep
from app.schemas import Shipment, ShipmentRead
from app.services import ShipmentService

router = APIRouter()


@router.get("/shipment", response_model = ShipmentRead)
def get_shipment(id: int, session = SessionDep):
    shipment = ShipmentService(session).get(id)
    # shipment = db.get(id)
    if shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment



