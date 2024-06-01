# https://ctftime.org/task/27875
import base64


def byte_xor(ba1, ba2):
    return bytes([a ^ b for a, b in zip(ba1, ba2)])


plain_txt = "A string of text can be encrypted by applying the bitwise XOR operator to every character using a given key"
ciphertext_decoded = base64.b64decode("NkMHEgkxXjV/BlN/ElUKMVZQEzFtGzpsVTgGDw==")

key = byte_xor(plain_txt.encode(), ciphertext_decoded)
print(key)