import requests
from dotenv import load_dotenv
import os
import json # Import the json library to pretty-print the output

load_dotenv()
api_key = os.getenv("KEY")

PRODUCTS_API_VERSION = "1.1"

store_id = "687e4d5bc645c046d7714789"

def api_get_request(url):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "User-Agent": "MyTestApp/1.0"
    }
    response = requests.get(url, headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": True,
            "status_code": response.status_code,
            "message": response.text
        }
    
def api_post_request(url, json):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "User-Agent": "MyTestApp/1.0",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers, json)
    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": True,
            "status_code": response.status_code,
            "message": response.text
        }

def get_all_store_pages():
    url = "https://api.squarespace.com/1.0/commerce/store_pages"
    return api_get_request(url)

def create_product():
    url = f"https://api.squarespace.com/1.1/commerce/products/"
    product_data = {
        "type": "PHYSICAL",
        "storePageId": store_id,
        "name": "Artisanal Steak Dry Rub",
        "description": "<p>This can be a few words or even a few <i>paragraphs</i>.</p>",
        "urlSlug": "artisanal-steak-dry-rub",
        "tags": ["artisanal", "steak"],
        "isVisible": True,
        "variantAttributes": ["Flavor"],
        "variants": [
            {
                "sku": "SQ0557856",
                "pricing": {
                    "basePrice": {
                        "currency": "USD",
                        "value": "12.95"
                    },
                    "onSale": False,
                    "salePrice": {
                        "currency": "USD",
                        "value": "0.00"
                    }
                },
                "stock": {
                    "quantity": 10,
                    "unlimited": False
                },
                "attributes": {
                    "Flavor": "Habanero"
                },
                "shippingMeasurements": {
                    "weight": {
                        "unit": "POUND",
                        "value": 2.0
                    },
                    "dimensions": {
                        "unit": "INCH",
                        "length": 7.0,
                        "width": 5.0,
                        "height": 5.0
                    }
                }
            }
        ]
    }
    return api_post_request(url, product_data)

def get_all_products():
    url = "https://api.squarespace.com/1.1/commerce/products?cursor=abc"
    return api_get_request(url)


# print(json.dumps(get_all_store_pages(), indent=2))
# print(create_product())
print(json.dumps(get_all_products(), indent=2))