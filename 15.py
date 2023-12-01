from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def generate_random_key():
    return os.urandom(16)  # For AES-128

def pad_data(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

def cbc_mac(key, message):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Assume that message is a single block
    ciphertext = encryptor.update(message) + encryptor.finalize()
    return ciphertext

def create_forgery(key, message):
    # Calculate the MAC for the one-block message
    mac = cbc_mac(key, message)

    # Create the two-block message X || (X ⊕ T)
    x_xor_t = bytes(x ^ t for x, t in zip(message, mac))
    two_block_message = message + x_xor_t

    return two_block_message

if __name__ == "__main__":
    # Example usage
    key = generate_random_key()
    message = b"Hello, CBC-MAC!"

    # Calculate the MAC for the one-block message
    mac_one_block = cbc_mac(key, message)

    # Create a forgery for the two-block message X || (X ⊕ T)
    forgery = create_forgery(key, message)

    # Display results
    print("Original Message:", message)
    print("MAC for One-Block Message:", mac_one_block)
    print("Forgery for Two-Block Message:", forgery)
