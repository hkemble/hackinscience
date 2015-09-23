import folium
import json


with open('velib_clean.json', 'r') as json_data:
    data = json.load(json_data)
map_osm = folium.Map(location=[2.3498, 48.8530])
for i in range(len(data)):
    map_osm.simple_marker([data[i]['latitude'], data[i]['longitude']],
                          popup='available: '+str(data[i]['number']))

map_osm.create_map(path='velib.html')
