def encrypt_vigenere(plain_text, key):
    key = key.upper()
    key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]

    cipher_text = ""
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            is_upper = plain_text[i].isupper()
            plain_char = plain_text[i].upper()
            key_char = key_repeated[i]
            
            # Use Caesar cipher logic for each character
            char_code = ord(plain_char) - ord('A')
            key_code = ord(key_char) - ord('A')
            encrypted_char = chr((char_code + key_code) % 26 + ord('A'))

            cipher_text += encrypted_char if is_upper else encrypted_char.lower()
        else:
            cipher_text += plain_text[i]

    return cipher_text

def decrypt_vigenere(cipher_text, key):
    key = key.upper()
    key_repeated = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]

    plain_text = ""
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            is_upper = cipher_text[i].isupper()
            cipher_char = cipher_text[i].upper()
            key_char = key_repeated[i]
            
            # Use Caesar cipher logic for each character
            char_code = ord(cipher_char) - ord('A')
            key_code = ord(key_char) - ord('A')
            decrypted_char = chr((char_code - key_code) % 26 + ord('A'))

            plain_text += decrypted_char if is_upper else decrypted_char.lower()
        else:
            plain_text += cipher_text[i]

    return plain_text

def main():
    key = input("Enter the key for the Vigenère Cipher: ")
    plaintext = input("Enter the plaintext: ")

    ciphertext = encrypt_vigenere(plaintext, key)
    decrypted_text = decrypt_vigenere(ciphertext, key)

    print("\nEncrypted Text:", ciphertext)
    print("Decrypted Text:", decrypted_text)
if __name__ == "__main__":
    main()

