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
        
        list_customers = []

        for customer in customers:
            list_customers.append({
            "id": customer["id"],
            "email": customer["email"],
            "first_name": customer["first_name"],
            "last_name": customer["last_name"],
            "userame":customer["username"]
            })

        return list_customers

    raise HTTPException(status_code=response.status_code,detail=response.text)