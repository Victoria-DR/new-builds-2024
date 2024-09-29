import json

# Define the scaling factor (adjust as needed)
scaling_factor = 0.1  # Smaller value brings coordinates closer together

# Read the existing GeoJSON file
with open('nodes.geojson', 'r') as f:
    data = json.load(f)

# Calculate the range of coordinates
min_lon = min(feature["geometry"]["coordinates"][0] for feature in data["features"])
max_lon = max(feature["geometry"]["coordinates"][0] for feature in data["features"])
min_lat = min(feature["geometry"]["coordinates"][1] for feature in data["features"])
max_lat = max(feature["geometry"]["coordinates"][1] for feature in data["features"])

# Scale and shift the coordinates
for feature in data["features"]:
    lon, lat = feature["geometry"]["coordinates"]
    
    # Scale the coordinates
    scaled_lon = (lon - min_lon) / (max_lon - min_lon)
    scaled_lat = (lat - min_lat) / (max_lat - min_lat)
    
    new_lon = scaled_lon * scaling_factor
    new_lat = scaled_lat * scaling_factor
    
    feature["geometry"]["coordinates"] = [new_lon, new_lat]

# Write the scaled data to a new GeoJSON file
with open("scaled_nodes.geojson", "w") as f:
    json.dump(data, f, indent=2)

print("Scaled nodes GeoJSON file has been created successfully.")