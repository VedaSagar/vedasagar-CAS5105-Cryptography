import string

def vigenere_encrypt(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        if plaintext[i] in string.ascii_uppercase:
            shift = key[i % len(key)]
            encrypted_char = chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(plaintext[i])
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    plaintext = []
    for i in range(len(ciphertext)):
        if ciphertext[i] in string.ascii_uppercase:
            shift = key[i % len(key)]
            decrypted_char = chr((ord(ciphertext[i]) - ord('A') - shift) % 26 + ord('A'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(ciphertext[i])
    return ''.join(plaintext)

def main():
    plaintext = "SENDMOREMONEY"
    key_stream = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

    # Encrypt the plaintext
    ciphertext = vigenere_encrypt(plaintext, key_stream)
    print("Encrypted Ciphertext:", ciphertext)

    # Decrypt the ciphertext to find the key for "CASHNOTNEEDED"
    target_plaintext = "CASHNOTNEEDED"
    possible_key = []
    for i in range(len(ciphertext)):
        shift = (ord(ciphertext[i]) - ord('A') - (ord(target_plaintext[i]) - ord('A'))) % 26
        possible_key.append(shift)

    print("Found Key:", possible_key)

    # Decrypt the ciphertext using the found key to verify
    decrypted_text = vigenere_decrypt(ciphertext, possible_key)
    print("Decrypted Plaintext:", decrypted_text)

if __name__ == "__main__":
    main()
