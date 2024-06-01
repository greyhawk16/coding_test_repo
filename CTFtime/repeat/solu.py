# https://ctftime.org/writeup/38443
 
from Crypto.Util.strxor import strxor
from binascii import unhexlify


def byte_xor(msg, key):
    return bytes([msg[i] ^ key[i%len(key)] for i in range(len(msg))])


FLAG_enc = unhexlify("982a9290d6d4bf88957586bbdcda8681de33c796c691bb9fde1a83d582c886988375838aead0e8c7dc2bc3d7cd97a4")
key = strxor(FLAG_enc[:8], b'uoftctf{')

FLAG = byte_xor(FLAG_enc, key)
print(FLAG)