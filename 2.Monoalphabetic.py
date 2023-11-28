import random
def generate_key():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    key = random.sample(alphabet, len(alphabet))
    return dict(zip(alphabet, key))
def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            substitute_char = key[char.upper()]           
            result += substitute_char if is_upper else substitute_char.lower()
        else:
            result += char
    return result
def decrypt(text, key):
    inverted_key = {v: k for k, v in key.items()}
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            substitute_char = inverted_key[char.upper()]
            result += substitute_char if is_upper else substitute_char.lower()
        else:
            result += char
    return result
def main():
    key = generate_key()
    print("Generated Key:", key)
    plaintext = input("Enter the text to encrypt: ")
    ciphertext = encrypt(plaintext, key)
    print("Encrypted text:", ciphertext)
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)
if __name__ == "__main__":
    main()
