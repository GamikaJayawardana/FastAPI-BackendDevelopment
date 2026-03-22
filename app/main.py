from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

@app.get("/shipment")
def get_shipment():
    return {
        "content" : "Woden Table",
        "status" : "In Transit"
    }

@app.get("/scalar")
def get_scalar_doc():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )