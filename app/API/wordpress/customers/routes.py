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

@router.get("/{customer_id}")
def get_woocommerce_customer_by_id(customer_id: int):
    response = wcapi.get(f"customers/{customer_id}")

    if response.status_code == 200:
        customer = response.json()
        return {
            "id": customer["id"],
            "email": customer["email"],
            "first_name": customer["first_name"],
            "last_name": customer["last_name"],
            "username": customer["username"]
        }
    elif response.status_code == 404:
        return {"message": f"No existe un cliente con el ID {customer_id}"}

    raise HTTPException(status_code=response.status_code, detail=response.text)