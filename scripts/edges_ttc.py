import json

# Load the GeoJSON data
with open('stations.geojson', 'r') as f:
    data = json.load(f)

# Extract stations
stations = data['features']

# Define lines (these are approximate based on typical Toronto subway layout)
lines = [
    ["Bloor-Yonge", "Sherbourne", "Bay", "St George", "Bathurst", "Dufferin", "Keele"],
    ["Bloor-Yonge", "Eglinton", "St Clair", "Eglinton West", "Yorkdale"],
    ["Bloor-Yonge", "College Station", "Dundas Station", "Queen", "King", "St Andrew", "Osgoode", "St George", "Queen's Park"],
    ["Bloor-Yonge", "Sherbourne", "Pape", "Main Street"]
]

# Function to find a station by name
def find_station(name):
    return next((s for s in stations if s['properties']['name'] == name), None)

# Create the subway line feature
subway_lines = []
for i, line in enumerate(lines):
    coordinates = []
    for station_name in line:
        station = find_station(station_name)
        if station:
            coordinates.append(station['geometry']['coordinates'])
    
    subway_line = {
        "type": "Feature",
        "properties": {
            "name": f"Toronto Subway Line {i+1}",
            "stroke": "#f1bc1a",
            "ref": f"Line{i+1}"
        },
        "geometry": {
            "type": "LineString",
            "coordinates": coordinates
        }
    }
    subway_lines.append(subway_line)

# Create the final GeoJSON structure
subway_geojson = {
    "type": "FeatureCollection",
    "features": subway_lines
}

# Save to file
with open('toronto_subway_lines.geojson', 'w') as f:
    json.dump(subway_geojson, f, indent=2)

print("Toronto subway lines file created successfully!")