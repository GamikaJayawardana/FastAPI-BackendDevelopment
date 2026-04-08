from contextlib import asynccontextmanager
from rich import print, panel
from fastapi import FastAPI, HTTPException
from scalar_fastapi import get_scalar_api_reference
from app.api.router import router
from app.databases import ShipmentsDatabase
from app.database.session import create_db_tables
from app.schemas import ShipmentCreate, ShipmentRead, ShipmentUpdate



@asynccontextmanager
async def lifefan_handler(app: FastAPI):
    create_db_tables()
    print(panel.Panel("server Started....", border_style="green"))
    yield
    print(panel.Panel("server Stopped....", border_style="red"))


app = FastAPI(lifespan=lifefan_handler)

db = ShipmentsDatabase()

app.include_router(router)


@app.post("/shipment", response_model = ShipmentCreate)
def create_shipment(shipment: ShipmentCreate):
    return db.create(shipment)

@app.patch("/shipment", response_model = ShipmentRead)
def update_shipment(id: int, shipment: ShipmentUpdate):
    updated_shipment = db.update(id, shipment)
    if updated_shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return updated_shipment

@app.delete("/shipment")
def delete_shipment(id: int):
    db.delete(id)
    return {"detail": "Shipment deleted successfully"}

@app.get("/scalar")
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API Reference"
    )
