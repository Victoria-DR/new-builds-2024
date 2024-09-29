import json

def calculate_centroid(coordinates):
    """Calculate the centroid of a polygon."""
    x_sum = sum(coord[0] for coord in coordinates[0][0])
    y_sum = sum(coord[1] for coord in coordinates[0][0])
    count = len(coordinates[0][0])
    return [x_sum / count, y_sum / count]

# Read the input MultiPolygon GeoJSON file
with open('neighborhoods.geojson', 'r') as f:
    input_data = json.load(f)

# Prepare the output GeoJSON structure
output_data = {
    "type": "FeatureCollection",
    "features": []
}

# Process each feature in the input data
centroids = []
for feature in input_data['features']:
    name = feature['properties']['name']
    coordinates = feature['geometry']['coordinates']
    centroid = calculate_centroid(coordinates)
    centroids.append(centroid)

# Calculate the range of centroids
min_lon = min(c[0] for c in centroids)
max_lon = max(c[0] for c in centroids)
min_lat = min(c[1] for c in centroids)
max_lat = max(c[1] for c in centroids)

# Define a scaling factor (adjust this to bring coordinates closer or further apart)
scaling_factor = 0.1  # Smaller value brings coordinates closer together

# Process centroids and create features
for i, (centroid, feature) in enumerate(zip(centroids, input_data['features'])):
    name = feature['properties']['name']
    
    # Scale and shift the coordinates
    scaled_lon = (centroid[0] - min_lon) / (max_lon - min_lon)
    scaled_lat = (centroid[1] - min_lat) / (max_lat - min_lat)
    
    new_lon = scaled_lon * scaling_factor
    new_lat = scaled_lat * scaling_factor
    
    # Create a new feature with Point geometry
    new_feature = {
        "type": "Feature",
        "properties": {
            "marker-size": "small",
            "marker-symbol": "circle",
            "marker-color": "#797979",
            "name": name
        },
        "geometry": {
            "type": "Point",
            "coordinates": [new_lon, new_lat]
        }
    }
    output_data['features'].append(new_feature)

# Write the output to a new GeoJSON file
with open('toronto_neighborhood_nodes_close.geojson', 'w') as f:
    json.dump(output_data, f, indent=2)

print("Toronto neighborhood nodes GeoJSON file with closer coordinates has been created successfully.")