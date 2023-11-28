def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()            
            char_code = ord(char)
            shifted_code = (char_code - ord('A' if is_upper else 'a') + shift) % 26
            encrypted_char = chr(shifted_code + ord('A' if is_upper else 'a'))
            result += encrypted_char
        else:
            result += char
    return result
def decrypt(text, shift):
    return encrypt(text, -shift)
def main():
    plaintext = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    ciphertext = encrypt(plaintext, shift)
    print("Encrypted text:", ciphertext)
    decrypted_text = decrypt(ciphertext, shift)
    print("Decrypted text:", decrypted_text)
if __name__ == "__main__":
    main()
