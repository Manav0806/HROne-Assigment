from fastapi import APIRouter, HTTPException, Query
from app.database import db
from app.models import ProductModel, ProductOut, PaginatedProducts
from app.utils import serialize_product

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product(product: ProductModel):
    result = await db.products.insert_one(product.dict())
    return {"id": str(result.inserted_id)}

@router.get("/products", response_model=PaginatedProducts)
async def list_products(
    name: str = Query(None),
    size: str = Query(None),
    limit: int = Query(10),
    offset: int = Query(0)
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes"] = {"$elemMatch": {"size": size}}

    cursor = db.products.find(query).sort("_id").skip(offset).limit(limit)
    results = await cursor.to_list(length=limit)
    return {
        "data": [serialize_product(p) for p in results],
        "page": {
            "next": offset + limit,
            "limit": len(results),
            "previous": max(0, offset - limit)
        }
    }
