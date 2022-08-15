import requests

inventory_base_url = "https://api.locationinventory.info/inventory"
shop_id = "test20170501.myshopify.com"
product_handle = "x-pod-sling-pack"
variant_id = 19284412006513
country_code = "US"

inventory_url = f"{inventory_base_url}?shop={shop_id}&handle={product_handle}"

# Do some checking to make sure the request worked
inventory_req = requests.get(inventory_url)

response = inventory_req.json()

variants = response["variantLocations"]

# Do some checking to make sure we have a variant with that number
for variant in variants:
    if variant["variant"] == variant_id:
        inventory_locations = variant["inventoryLocations"]
        for location in inventory_locations:
            if location["location"]["country"] == country_code:
                quantity_available = location["quantity"]
                if quantity_available > 0:
                    print(f"{quantity_available} available units in {country_code}!")
                else:
                    print(f"Item not available in {country_code}")
