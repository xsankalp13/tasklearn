import json
import random

categories = [
    "Laptops",
    "Smartphones",
    "Audio",
    "Accessories",
    "Monitors",
    "Storage",
    "Networking",
    "Gaming",
    "Wearables",
    "Tablets",
]

products = []

for i in range(1, 101):
    category = random.choice(categories)

    products.append({
        "id": i,
        "title": f"{category} Product {i}",
        "description": f"High-quality {category.lower()} device with modern features.",
        "category": category,
        "brand": f"Brand{i % 10 + 1}",
        "price": round(random.uniform(29.99, 2499.99), 2),
        "quantity": random.randint(0, 500),
        "rating": round(random.uniform(3.5, 5.0), 1),
        "inStock": random.choice([True, True, True, False])
    })

with open("products.json", "w") as f:
    json.dump(products, f, indent=2)

print("Created products.json with 100 products")