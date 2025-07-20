from bson import ObjectId

def to_object_id(id_str):
    try:
        return ObjectId(id_str)
    except:
        return None

def serialize_product(product):
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"]
    }

def serialize_order(order, product_map):
    items = []
    total = 0.0
    for item in order["items"]:
        product = product_map.get(str(item["productId"]))
        if product:
            items.append({
                "productDetails": {
                    "name": product["name"],
                    "id": str(product["_id"])
                },
                "qty": item["qty"]
            })
            total += product["price"] * item["qty"]
    return {
        "id": str(order["_id"]),
        "items": items,
        "total": total
    }
