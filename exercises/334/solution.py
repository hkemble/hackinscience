import json


with open('velib_clean.json', 'r') as json_data:
    data = json.load(json_data)


def locate(lat, lon):
    closest = 1000000000
    city = 'none'
    for i in range(len(data)):
        new = (((data[i]['latitude'] - lat) ** 2 +
                (data[i]['longitude'] - long) ** 2) ** 0.5)
        if new < closest:
            closest = new
            city = data[i]['city']
    return {'distance': closest, 'city': city}
