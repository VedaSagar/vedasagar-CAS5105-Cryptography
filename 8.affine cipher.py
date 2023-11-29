def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_decrypt(ciphertext, a, b):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((mod_inverse(a, 26) * (ord(char) - ord('A') - b)) % 26 + ord('A'))
            else:
                decrypted_char = chr((mod_inverse(a, 26) * (ord(char) - ord('a') - b)) % 26 + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def break_affine_cipher(ciphertext, first_most_frequent, second_most_frequent):
    for a in range(1, 26):
        if mod_inverse(a, 26) is not None:
            for b in range(26):
                decrypted_text = affine_decrypt(ciphertext, a, b)
                first_freq = decrypted_text.count(first_most_frequent)
                second_freq = decrypted_text.count(second_most_frequent)

                if first_freq > 0 and second_freq > 0:
                    return decrypted_text

    return "Failed to break the affine cipher."

def main():
    ciphertext = "BUBUBUBUBUBUBUBUBUBUBUBUBUBUBU"
    first_most_frequent = "B"
    second_most_frequent = "U"

    print("Ciphertext:", ciphertext)

    decrypted_text = break_affine_cipher(ciphertext, first_most_frequent, second_most_frequent)
    print("Decrypted Plaintext:", decrypted_text)

if __name__ == "__main__":
    main()


