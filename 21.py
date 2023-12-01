from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

def generate_dsa_key_pair():
    private_key = dsa.generate_private_key(
        key_size=1024,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(
        message,
        hashes.SHA256()
    )

    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message,
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

if __name__ == "__main__":
    private_key, public_key = generate_dsa_key_pair()
    message = b"Hello, DSA!"
    signature = sign_message(private_key, message)

    print(f"Message: {message.decode('utf-8')}")
    print(f"Signature: {signature.hex()}")
    is_verified = verify_signature(public_key, message, signature)

    if is_verified:
        print("Signature is verified.")
    else:
        print("Signature verification failed.")
