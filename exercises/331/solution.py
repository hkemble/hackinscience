import json


with open('velib.json', 'r') as json_data:
    data = json.load(json_data)
zips = []
city = []
for i in range(len(data)):
    data[i]['zip_code'] = data[i]['address'].split()[-2]
    data[i]['city'] = data[i]['address'].split()[-1]
    data[i]['name'] = str.join(' ', data[i]['name'].split()[2:])
    data[i]['address'] = str.join(' ', data[i]['address'].split()[:-3])
with open('solution.json', 'w') as json_data_out:
    json.dump(data, json_data_out)
