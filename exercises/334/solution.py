import json


with open('velib_clean.json', 'r') as json_data:
    data = json.load(json_data)


def locate(tup):
    closest = 1000000000
    city = 'none'
    for i in range(len(data)):
        new = (((data[i]['latitude'] - tup[1]) ** 2 +
                (data[i]['longitude'] - tup[2]) ** 2) ** 0.5)
        if new < closest:
            closest = new
            city = data[i]['city']
    return {'distance': closest, 'city': city}
