from dotenv import load_dotenv 
import json
import os
import requests

load_dotenv()

get_city_response = {
    "places": [
        {
            "location": {
                "latitude": 43.653226,
                "longitude": -79.3831843
            },
            "displayName": {
                "text": "Toronto",
                "languageCode": "en"
            }
        }
    ]
}

data = {
    "type": "FeatureCollection",
    "features": []
}

lat_diff = 0.009
lon_diff = 0.011

for i in range(-2, 3):
    for j in range(-2, 3):
        get_subway_stations_response = requests.post(
            "https://places.googleapis.com/v1/places:searchNearby",
            headers={"Content-Type": "application/json", "X-Goog-Api-Key": os.getenv("GOOGLE_API_KEY"), "X-Goog-FieldMask": "places.displayName,places.location"},
            json={
                "includedTypes": [
                    "subway_station"
                ],
                "maxResultCount": 20,
                "locationRestriction": {
                    "circle": {
                        "center": {
                            "latitude": 43.653226 + i * lat_diff,
                            "longitude": -79.3831843 + j * lon_diff
                        },
                        "radius": 5000.0
                    }
                },
                "rankPreference": "DISTANCE"
            }
        )

        print(get_subway_stations_response.json())

        for station in get_subway_stations_response.json()["places"]:
            if station["displayName"]["text"] not in [feature["properties"]["name"] for feature in data["features"]]:
                data["features"].append({
                    "type": "Feature",
                    "properties": {
                        "marker-size": "small",
                        "marker-symbol": "circle",
                        "marker-color": "#797979",
                        "name": station["displayName"]["text"]
                    },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            abs(station["location"]["longitude"]),
                            abs(station["location"]["latitude"])
                        ]
                    }
                })

with open("toronto_nodes.geojson", "w") as file:
    file.write(json.dumps(data))
