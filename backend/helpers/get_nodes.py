from dotenv import load_dotenv 
import json
import os
import requests

from get_city import get_city_coords

load_dotenv()

get_city_response = get_city_coords("Toronto")["places"][0]["location"]

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
                            "latitude": get_city_response["latitude"] + i * lat_diff,
                            "longitude": get_city_response["longitude"] + j * lon_diff
                        },
                        "radius": 5000.0
                    }
                },
                "rankPreference": "DISTANCE"
            }
        )

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
                            station["location"]["longitude"],
                            station["location"]["latitude"]
                        ]
                    }
                })

min_lon = min([feature["geometry"]["coordinates"][0] for feature in data["features"]])
min_lat = min([feature["geometry"]["coordinates"][1] for feature in data["features"]])
for feature in data["features"]:
    if min_lon < 0:
        feature["geometry"]["coordinates"][0] += abs(min_lon)
    if min_lat < 0:
        feature["geometry"]["coordinates"][1] += abs(min_lat)

with open("nodes.geojson", "w") as file:
    file.write(json.dumps(data))
