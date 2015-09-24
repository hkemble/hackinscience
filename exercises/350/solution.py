import bencode_tools as bt


def encode(stuff):
    return bytes(bt.encode2(stuff), encoding='ascii')
