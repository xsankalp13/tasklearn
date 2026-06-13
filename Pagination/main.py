import json
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

with open("products.json", "r") as f:
    products = json.load(f)

@app.get("/api/orders")
def get_orders(
    page: int = Query(default=1, ge=1, description="Page Number"),
    limit: int = Query(default=10, ge=1, le=20, description="Number of items per page")
):
    start = (page  - 1) * limit
    if start >= len(products):
        return {
            "page": page,
            "limit": limit,
            "message": "No products found",
            "data": []
        }
    
    end = start + limit
    paginated_products = products[start:end]
    return {
        "data" : paginated_products,
        "totalItems": len(products),
        "totalPages": (len(products) + limit - 1  ) // limit,
        "currentPage": page,
        "itemsPerPage": limit
    }