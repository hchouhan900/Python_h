product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}
# keys_to_remove = ["stock", "warehouse"]

for key in list(product):
    if key == "stock" or key == "warehouse" or key == "price":
        product.pop(key)

product["gender"] = "male"
# for keys in keys_to_remove:
# product.pop(key,None)

print(product)
