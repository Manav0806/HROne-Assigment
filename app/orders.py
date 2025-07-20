from fastapi import APIRouter, HTTPException, Path, Query
from app.database import db
from app.models import CreateOrder, PaginatedOrders
from app.utils import to_object_id, serialize_order

router = APIRouter()

@router.post("/orders", status_code=201)
async def create_order(order: CreateOrder):
    result = await db.orders.insert_one(order.dict())
    return {"id": str(result.inserted_id)}

@router.get("/orders/{user_id}", response_model=PaginatedOrders)
async def get_orders(
    user_id: str = Path(...),
    limit: int = Query(10),
    offset: int = Query(0)
):
    orders_cursor = db.orders.find({"userId": user_id}).sort("_id").skip(offset).limit(limit)
    orders = await orders_cursor.to_list(length=limit)

    product_ids = {item["productId"] for order in orders for item in order["items"]}
    object_ids = [to_object_id(pid) for pid in product_ids if to_object_id(pid)]
    products = await db.products.find({"_id": {"$in": object_ids}}).to_list(None)
    product_map = {str(p["_id"]): p for p in products}

    return {
        "data": [serialize_order(order, product_map) for order in orders],
        "page": {
            "next": offset + limit,
            "limit": len(orders),
            "previous": max(0, offset - limit)
        }
    }
