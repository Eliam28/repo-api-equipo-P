from fastapi import APIRouter, HTTPException
from app.Core.woocommerce_client import wcapi
from app.API.wordpress.customers.schema_json import CustomerCreate

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

@router.post("/")
async def create_woocommerce_customer(customer: CustomerCreate):
    customer_data = customer.model_dump() 
    

    response = wcapi.post("customers", customer_data)

    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(
            status_code=response.status_code, 
            detail=response.json()
        )