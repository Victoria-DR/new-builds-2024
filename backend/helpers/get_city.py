from dotenv import load_dotenv 
import os
import requests

def get_city_coords(city_name):
    load_dotenv()

    get_city_response = requests.post(
        "https://places.googleapis.com/v1/places:searchText",
        headers={"Content-Type": "application/json", "X-Goog-Api-Key": os.getenv("GOOGLE_API_KEY"), "X-Goog-FieldMask": "places.displayName,places.location"},
        json={
            "textQuery": city_name,
            "includedType": "locality",
            "pageSize": 1
        }
    )

    return get_city_response.json()
