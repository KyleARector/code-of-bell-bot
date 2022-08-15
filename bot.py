import time
import requests

# Constants
inventory_base_url = "https://api.locationinventory.info/inventory"
shop_id = "test20170501.myshopify.com"
product_handle = "x-pod-sling-pack"
variant_id = 19284412006513
country_code = "US"
discord_webhook_url = "discord_webhook"
product_page_url = "https://www.codeofbell.com/products/x-pod-sling-pack"
inventory_url = f"{inventory_base_url}?shop={shop_id}&handle={product_handle}"
delay_time_minutes = 2;
notification_debounce = 4;

notification_count = notification_debounce;
while True:
    try:
        # Request inventory from Shopify
        inventory_req = requests.get(inventory_url)
        response = inventory_req.json()
        variants = response["variantLocations"]

        # Check if the thing we want is in stock
        for variant in variants:
            if variant["variant"] == variant_id:
                inventory_locations = variant["inventoryLocations"]
                for location in inventory_locations:
                    if location["location"]["country"] == country_code:
                        quantity_available = location["quantity"]
                        if quantity_available > 0:
                            # If in stock, send message to Discord
                            if notification_count >= notification_debounce:
                                message = f"{quantity_available} units available in {country_code}!"
                                #requests.post(discord_webhook_url, json={"content": f"{message}: {product_page_url}"})
                                print(message)
                                notification_count = 0
                            else:
                                print("Delaying notification since we just sent one")
                                notification_count += 1
                        else:
                            # Not sure what to do here yet, maybe log?
                            message = f"Item not available in {country_code}"
                            print(message)
    except:
        print("There was an issue processing the request")
        pass
    time.sleep(delay_time_minutes * 60)