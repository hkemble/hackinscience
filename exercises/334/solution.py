import bencode_tools as bt


def encode(obj):
    t = str(type(obj))
    obj = bt.bencode_dic['%s' %t](obj)
    return encode(obj)
    
    
    bt.bencode_dic["<class 'bytes'>"](obj)
#def decode(byte):
    