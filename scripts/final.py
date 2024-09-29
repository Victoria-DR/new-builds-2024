import json

# Population data
population_data = """
Agincourt North	29,113
Agincourt South-Malvern West	23,757
Alderwood	12,054
Annex	30,526
Banbury-Don Mills	27,695
Bathurst Manor	15,873
Bay Street Corridor	25,797
Bayview Village	21,396
Bayview Woods-Steeles	13,154
Bedford Park-Nortown	23,236
Beechborough-Greenbrook	6,577
Bendale	29,960
Birchcliffe-Cliffside	22,291
Black Creek	21,737
Blake-Jones	7,727
Briar Hill-Belgravia	14,257
Bridle Path-Sunnybrook-York Mills	9,266
Broadview North	11,499
Brookhaven-Amesbury	17,757
Cabbagetown-South St. James Town	11,669
Caledonia-Fairbank	9,955
Casa Loma	10,968
Centennial Scarborough	13,362
Church-Yonge Corridor	31,340
Clairlea-Birchmount	26,984
Clanton Park	16,472
Cliffcrest	15,935
Corso Italia-Davenport	14,133
Danforth	9,666
Danforth East York	17,180
Don Valley Village	27,051
Dorset Park	25,003
Dovercourt-Wallace Emerson-Junction	36,625
Downsview-Roding-CFB	35,052
Dufferin Grove	11,785
East End-Danforth	21,381
Edenbridge-Humber Valley	15,535
Eglinton East	22,776
Elms-Old Rexdale	9,456
Englemount-Lawrence	22,372
Eringate-Centennial-West Deane	18,588
Etobicoke West Mall	11,848
Flemingdon Park	21,933
Forest Hill North	12,806
Forest Hill South	10,732
Glenfield-Jane Heights	30,491
Greenwood-Coxwell	14,417
Guildwood	9,917
Henry Farm	15,723
High Park North	22,162
High Park-Swansea	23,925
Highland Creek	12,494
Hillcrest Village	16,934
Humber Heights-Westmount	10,948
Humber Summit	12,416
Humbermede	15,545
Humewood-Cedarvale	14,365
Ionview	13,641
Islington-City Centre West	43,965
Junction Area	14,366
Keelesdale-Eglinton West	11,058
Kennedy Park	17,123
Kensington-Chinatown	17,945
Kingsview Village-The Westway	22,000
Kingsway South	9,271
L'Amoreaux	43,993
Lambton Baby Point	7,985
Lansing-Westgate	16,164
Lawrence Park North	14,607
Lawrence Park South	15,179
Leaside-Bennington	16,828
Little Portugal	15,559
Long Branch	10,084
Malvern	43,794
Maple Leaf	10,111
Markland Wood	10,554
Milliken	26,572
Mimico (includes Humber Bay Shores)	33,964
Morningside	17,455
Moss Park	20,506
Mount Dennis	13,593
Mount Olive-Silverstone-Jamestown	32,954
Mount Pleasant East	16,775
Mount Pleasant West	29,658
New Toronto	11,463
Newtonbrook East	16,097
Newtonbrook West	23,831
Niagara	31,180
North Riverdale	11,916
North St. James Town	18,615
O'Connor-Parkview	18,675
Oakridge	13,845
Oakwood Village	21,210
Old East York	9,233
Palmerston-Little Italy	13,826
Parkwoods-Donalda	34,805
Pelmo Park-Humberlea	10,722
Playter Estates-Danforth	7,804
Pleasant View	15,818
Princess-Rosethorn	11,051
Regent Park	10,803
Rexdale-Kipling	10,529
Rockcliffe-Smythe	22,246
Roncesvalles	14,974
Rosedale-Moore Park	20,923
Rouge	46,496
Runnymede-Bloor West Village	10,070
Rustic	9,941
Scarborough Village	16,724
South Parkdale	21,849
South Riverdale	27,876
St.Andrew-Windfields	17,812
Steeles	24,623
Stonegate-Queensway	25,051
Tam O'Shanter-Sullivan	27,446
Taylor-Massey	15,683
The Beaches	21,567
Thistletown-Beaumond Heights	10,360
Thorncliffe Park	21,108
Trinity-Bellwoods	16,556
University	7,607
Victoria Village	17,510
Waterfront Communities-The Island	65,913
West Hill	27,392
West Humber-Clairville	33,312
Westminster-Branson	26,274
Weston	17,992
Weston-Pelham Park	11,098
Wexford/Maryvale	27,917
Willowdale East	50,434
Willowdale West	16,936
Willowridge-Martingrove-Richview	22,156
Woburn	53,485
Woodbine Corridor	12,541
Woodbine-Lumsden	7,865
Wychwood	14,349
Yonge-Eglinton	11,817
Yonge-St.Clair	12,528
York University Heights	27,593
Yorkdale-Glen Park	14,804
"""

# Process population data
population_dict = {}
for line in population_data.strip().split('\n'):
    name, pop = line.rsplit('\t', 1)
    population_dict[name] = int(pop.replace(',', ''))

# Read the GeoJSON file
with open('toronto_neighborhood_nodes_close.geojson', 'r') as f:
    geojson_data = json.load(f)

# Filter features based on population
filtered_features = []
for feature in geojson_data['features']:
    name = feature['properties']['name']
    if name in population_dict and population_dict[name] >= 20000:
        filtered_features.append(feature)

# Create new GeoJSON with filtered features
filtered_geojson = {
    "type": "FeatureCollection",
    "features": filtered_features
}

# Write the filtered GeoJSON to a new file
with open('toronto_filtered_neighborhoods.geojson', 'w') as f:
    json.dump(filtered_geojson, f, indent=2)

print(f"Original number of neighborhoods: {len(geojson_data['features'])}")
print(f"Number of neighborhoods after filtering: {len(filtered_features)}")
print("Filtered GeoJSON saved as 'toronto_filtered_neighborhoods.geojson'")