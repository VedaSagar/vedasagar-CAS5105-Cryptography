from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization

def cbc_mac(key, message):
    cipher = Cipher(algorithms.AES(key), modes.CBC(bytes(16)), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()
    return ciphertext[-16:] 

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def forge_cbc_mac(original_key, original_message):
    original_mac = cbc_mac(original_key, original_message)
    new_message = original_message + xor_bytes(original_message, original_mac)
    forged_mac = cbc_mac(original_key, new_message)

    return new_message, forged_mac

if __name__ == "__main__":
    key = b'SecretKey1234567'  
    message = b'Hello, CBC-MAC!'
    original_mac = cbc_mac(key, message)

    print(f"Original Message: {message}")
    print(f"Original MAC: {original_mac.hex()}")
    forged_message, forged_mac = forge_cbc_mac(key, message)

    print(f"\nForged Message: {forged_message}")
    print(f"Forged MAC: {forged_mac.hex()}")
