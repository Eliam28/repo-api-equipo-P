from fastapi import APIRouter, HTTPException
from app.Core.woocommerce_client import wcapi

router = APIRouter()


@router.get("/{coupon_id}")
def get_coupon_by_id(coupon_id: int):
    """
    Obtiene un cupón por su ID desde WordPress/WooCommerce
    
    GET /wp-json/wc/v3/coupons/{id}
    """
    try:
        response = wcapi.get(f"coupons/{coupon_id}")

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Cupón no encontrado o error en WooCommerce: {response.text}"
            )

        coupon = response.json()

        return {
            "id": coupon.get("id"),
            "code": coupon.get("code"),
            "discount_type": coupon.get("discount_type"),
            "amount": coupon.get("amount"),
            "status": coupon.get("status"),
            "date_created": coupon.get("date_created"),
            "date_modified": coupon.get("date_modified"),
            "description": coupon.get("description"),
            "discount_expires": coupon.get("discount_expires"),
            "usage_count": coupon.get("usage_count"),
            "used_by": coupon.get("used_by"),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
