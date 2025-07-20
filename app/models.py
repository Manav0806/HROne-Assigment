from pydantic import BaseModel, Field
from typing import List, Optional

class SizeModel(BaseModel):
    size: str
    quantity: int

class ProductModel(BaseModel):
    name: str
    price: float
    sizes: List[SizeModel]

class ProductOut(BaseModel):
    id: str
    name: str
    price: float

class OrderItem(BaseModel):
    productId: str
    qty: int

class CreateOrder(BaseModel):
    userId: str
    items: List[OrderItem]

class ProductDetails(BaseModel):
    name: str
    id: str

class OrderItemOut(BaseModel):
    productDetails: ProductDetails
    qty: int

class OrderOut(BaseModel):
    id: str
    items: List[OrderItemOut]
    total: float

class Pagination(BaseModel):
    next: Optional[int]
    limit: int
    previous: Optional[int]

class PaginatedProducts(BaseModel):
    data: List[ProductOut]
    page: Pagination

class PaginatedOrders(BaseModel):
    data: List[OrderOut]
    page: Pagination
