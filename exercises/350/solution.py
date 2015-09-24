import bencode_tools as bt


def encode2(obj):
    if type(obj) == bytes or int:
        return bt.bencode_dic[str(type(obj))](obj)
    elif type(obj) == dict:
        for i in obj:
            obj[i] = bt.bencode_dic[str(type(obj[i]))](obj)[i]
        return obj
    elif type(obj) == list:
        for i in range(len(list)):
            obj[i] = bt.bencode_dic[str(type(obj[i]))](obj)[i]
        return obj
    else:
        return obj


def encode(stuff):
    return bytes(encode2(stuff), encoding='ascii')
