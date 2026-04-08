from app.database.models import Shipment
from app.schemas import ShipmentCreate, ShipmentUpdate
from sqlalchemy.ext.asyncio import AsyncSession


class ShipmentService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self,id: int) -> Shipment | None:
        return await self.session.get(Shipment, id)

    async def add(self, shipmentCreate: ShipmentCreate) -> Shipment:
        shipment = Shipment(**shipmentCreate.dict())
        self.session.add(shipment)
        await self.session.commit()
        await self.session.refresh(shipment)
        return shipment

    async def update(self, id: int, shipmentUpdate: ShipmentUpdate) -> Shipment:
        shipment = await self.session.get(Shipment, id)
        if shipment is None:
            raise ValueError(f"Shipment with id {id} not found")
        for key, value in shipmentUpdate.dict().items():
            setattr(shipment, key, value)
        await self.session.commit()
        await self.session.refresh(shipment)
        return shipment

    async def delete(self, id: int) -> None:
        shipment = await self.session.get(Shipment, id)
        if shipment is None:
            raise ValueError(f"Shipment with id {id} not found")
        await self.session.delete(shipment)
        await self.session.commit()

