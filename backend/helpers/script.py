import json
import re

def convert_to_json(data):
    neighborhoods = {}
    for line in data.strip().split('\n'):
        # Use regular expression to split on multiple spaces
        parts = re.split(r'\s{2,}', line.strip())
        if len(parts) == 2:
            name, population = parts
            # Remove commas from population and convert to int
            neighborhoods[name.strip()] = int(population.replace(',', ''))
    return neighborhoods

# The data string (replace this with reading from a file in a real scenario)
data = """Agincourt North    29113
Agincourt South-Malvern West    23757
Alderwood    12054
Annex    30526
Banbury-Don Mills    27695
Bathurst Manor    15873
Bay Street Corridor    25797
Bayview Village    21396
Bayview Woods-Steeles    13154
Bedford Park-Nortown    23236
Beechborough-Greenbrook    6577
Bendale    29960
Birchcliffe-Cliffside    22291
Black Creek    21737
Blake-Jones    7727
Briar Hill-Belgravia    14257
Bridle Path-Sunnybrook-York Mills    9266
Broadview North    11499
Brookhaven-Amesbury    17757
Cabbagetown-South St. James Town    11669
Caledonia-Fairbank    9955
Casa Loma    10968
Centennial Scarborough    13362
Church-Yonge Corridor    31340
Clairlea-Birchmount    26984
Clanton Park    16472
Cliffcrest    15935
Corso Italia-Davenport    14133
Danforth    9666
Danforth East York    17180
Don Valley Village    27051
Dorset Park    25003
Dovercourt-Wallace Emerson-Junction    36625
Downsview-Roding-CFB    35052
Dufferin Grove    11785
East End-Danforth    21381
Edenbridge-Humber Valley    15535
Eglinton East    22776
Elms-Old Rexdale    9456
Englemount-Lawrence    22372
Eringate-Centennial-West Deane    18588
Etobicoke West Mall    11848
Flemingdon Park    21933
Forest Hill North    12806
Forest Hill South    10732
Glenfield-Jane Heights    30491
Greenwood-Coxwell    14417
Guildwood    9917
Henry Farm    15723
High Park North    22162
High Park-Swansea    23925
Highland Creek    12494
Hillcrest Village    16934
Humber Heights-Westmount    10948
Humber Summit    12416
Humbermede    15545
Humewood-Cedarvale    14365
Ionview    13641
Islington-City Centre West    43965
Junction Area    14366
Keelesdale-Eglinton West    11058
Kennedy Park    17123
Kensington-Chinatown    17945
Kingsview Village-The Westway    22000
Kingsway South    9271
L'Amoreaux    43993
Lambton Baby Point    7985
Lansing-Westgate    16164
Lawrence Park North    14607
Lawrence Park South    15179
Leaside-Bennington    16828
Little Portugal    15559
Long Branch    10084
Malvern    43794
Maple Leaf    10111
Markland Wood    10554
Milliken    26572
Mimico (includes Humber Bay Shores)    33964
Morningside    17455
Moss Park    20506
Mount Dennis    13593
Mount Olive-Silverstone-Jamestown    32954
Mount Pleasant East    16775
Mount Pleasant West    29658
New Toronto    11463
Newtonbrook East    16097
Newtonbrook West    23831
Niagara    31180
North Riverdale    11916
North St. James Town    18615
O'Connor-Parkview    18675
Oakridge    13845
Oakwood Village    21210
Old East York    9233
Palmerston-Little Italy    13826
Parkwoods-Donalda    34805
Pelmo Park-Humberlea    10722
Playter Estates-Danforth    7804
Pleasant View    15818
Princess-Rosethorn    11051
Regent Park    10803
Rexdale-Kipling    10529
Rockcliffe-Smythe    22246
Roncesvalles    14974
Rosedale-Moore Park    20923
Rouge    46496
Runnymede-Bloor West Village    10070
Rustic    9941
Scarborough Village    16724
South Parkdale    21849
South Riverdale    27876
St.Andrew-Windfields    17812
Steeles    24623
Stonegate-Queensway    25051
Tam O'Shanter-Sullivan    27446
Taylor-Massey    15683
The Beaches    21567
Thistletown-Beaumond Heights    10360
Thorncliffe Park    21108
Trinity-Bellwoods    16556
University    7607
Victoria Village    17510
Waterfront Communities-The Island    65913
West Hill    27392
West Humber-Clairville    33312
Westminster-Branson    26274
Weston    17992
Weston-Pelham Park    11098
Wexford/Maryvale    27917
Willowdale East    50434
Willowdale West    16936
Willowridge-Martingrove-Richview    22156
Woburn    53485
Woodbine Corridor    12541
Woodbine-Lumsden    7865
Wychwood    14349
Yonge-Eglinton    11817
Yonge-St.Clair    12528
York University Heights    27593
Yorkdale-Glen Park    14804"""

# Convert the data to a dictionary
neighborhoods = convert_to_json(data)

# Write the data to a JSON file
with open('toronto_neighborhoods.json', 'w') as f:
    json.dump(neighborhoods, f, indent=2)

print("Data has been converted and saved to 'toronto_neighborhoods.json'")