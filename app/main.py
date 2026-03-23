from typing import Any

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

# Create a FastAPI application instance. 
# This instance will be used to define the API endpoints and handle incoming requests.
app = FastAPI()

# This is a simple FastAPI application that defines 
# endpoint for retrieving shipment information 
# The shipment endpoints return hardcoded data about a 
# shipment, while the scalar endpoint generates documentation based on 
# the OpenAPI specification of the FastAPI application.
@app.get("/shipment")
def get_shipment():
    return {
        "content" : "Woden Table",
        "status" : "In Transit"
    }

# This endpoint retrieves shipment information based on the provided ID. 
# It returns a JSON object containing the shipment ID, content, and status. 
# The data is hardcoded for demonstration purposes.
@app.get("/shipment/{id}")
def get_shipment_by_id(id: int) -> dict[str, str | int | float]:
    return {
        "id" : id,
        "weight" : 10.5,
        "content" : "Woden Table",
        "status" : "In Transit"
    }


# This endpoint generates documentation for the Scalar API 
# based on the OpenAPI specification of the FastAPI application.
@app.get("/scalar", include_in_schema=False)
def get_scalar_doc():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )




shipments ={
    12701: {
        "weight" : 10.5,
        "content" : "Woden Table",
        "status" : "Placed"
    },
    12702: {
        "weight" : 5.0,
        "content" : "Metal Chair",
        "status" : "In Transit"
    },
    12703: {
        "weight" : 2.0,
        "content" : "Plastic Lamp",
        "status" : "Delivered"
    },
    12704: {
        "weight" : 15.0,
        "content" : "Glass Vase",
        "status" : "Placed"
    },
    12705: {
        "weight" : 8.0,
        "content" : "Leather Sofa",
        "status" : "In Transit"
    },
    12706: {
        "weight" : 3.5,
        "content" : "Ceramic Plate",
        "status" : "Delivered"
    },
}

@app.get("/v1/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]

@app.get("/v1/shipment/{id}")
def get_shipment_by_id_v1(id: int) -> dict[str, Any]:
    if id not in shipments:
        return {
            "error" : "Shipment not found"
        }
    return shipments[id]