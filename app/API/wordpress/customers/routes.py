from fastapi import APIRouter, HTTPException
from app.Core.woocommerce_client import wcapi

router = APIRouter()

@router.get("/")
def get_woocommerce_customers():

    response = wcapi.get("customers")

    if response.status_code == 200:

        customers = response.json()

        if not customers:
            return {"message": "No hay clientes registrados"}
        
        return customers

    raise HTTPException(status_code=response.status_code,detail=response.text)