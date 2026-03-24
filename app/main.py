from typing import Any

from fastapi import FastAPI, HTTPException, status
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

# This endpoint retrieves shipment information based on the provided ID. 
# If no ID is provided, it returns the latest shipment information.
@app.get("/v2/shipment")
def get_shipment_by_id_v2(id: int | None = None) -> dict[str, Any]:
    if not id:
        id = max(shipments.keys())
        return shipments[id]
    if id not in shipments:
        # If the shipment ID is not found in the shipments dictionary,
        # an HTTPException is raised with a 404 status code and a detail message.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Shipment not found")
    
    return shipments[id]

@app.post("/v1/shipment")
def submit_shipment(content: str, weight: float):
    if weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, 
            detail="Shipment weight exceeds the maximum limit of 25 kg"
        )

    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {
        "weight" : weight,
        "content" : content,
        "status" : "Placed"
    }
    return shipments[new_id]

@app.post("/v2/shipment")
def submit_shipment_v2(data: dict) -> dict[str, Any]:
    content = data["content"]
    weight = data["weight"]
    if weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, 
            detail="Shipment weight exceeds the maximum limit of 25 kg"
        )

    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {
        "weight" : weight,
        "content" : content,
        "status" : "Placed"
    }
    return shipments[new_id]

@app.get("/v2/shipment/{field}")
def get_shipment_field(field: str, id: int) -> dict[str, Any]:
    return {
        field: shipments[id][field]
    }

@app.put("/v1/shipment/{id}")
def shipment_update(
    id: int, content: str, weight: float, status: str
    ) -> dict[str, Any]:
    shipments[id] = {
        "weight" : weight,
        "content" : content,
        "status" : status
    }
    return shipments[id]

# This endpoint updates the shipment information based on the provided ID. 
@app.patch("/v1/shipment")
def patch_shipment(
    id: int, 
    content: str | None = None, 
    weight: float | None = None, 
    status: str | None = None,
):
    shipment = shipments[id]
    if content:
        shipment["content"] = content
    if weight:
        shipment["weight"] = weight
    if status:
        shipment["status"] = status
    shipments[id] = shipment
    return shipments[id]

# This endpoint updates the shipment information based on the provided ID.
@app.patch("/v2/shipment")
def patch_shipment_v2(
    id: int, 
    body: dict[str, Any],
):
    shipment = shipments[id]
    shipment.update(body)
    shipments[id] = shipment
    return shipments[id]

# This endpoint deletes a shipment based on the provided ID.
@app.delete("/v1/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    shipments.pop(id)
    return {
        "message" : f"Shipment {id} deleted successfully"
    }