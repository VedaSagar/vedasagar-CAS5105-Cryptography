def generate_key(key):
    key_matrix = [['' for _ in range(5)] for _ in range(5)]
    key = key.replace('J', 'I')  # Treat 'I' and 'J' as the same letter
    key += 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    # Fill the key matrix
    k = 0
    for i in range(5):
        for j in range(5):
            key_matrix[i][j] = key[k]
            k += 1

    return key_matrix

def find_position(matrix, char):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == char:
                return i, j
    return None  # Add this line to handle the case when the character is not found

def encrypt(plain_text, key_matrix):
    cipher_text = ""
    plain_text = plain_text.replace('J', 'I')  # Treat 'I' and 'J' as the same letter
    plain_text = [plain_text[i:i + 2] for i in range(0, len(plain_text), 2)]

    for pair in plain_text:
        row1, col1 = find_position(key_matrix, pair[0])
        row2, col2 = find_position(key_matrix, pair[1])

        if row1 == row2:
            cipher_text += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            cipher_text += key_matrix[row1][col2] + key_matrix[row2][col1]

    return cipher_text

def main():
    key = input("Enter the key for the Playfair Cipher: ").upper()
    plaintext = input("Enter the plaintext: ").upper()

    key_matrix = generate_key(key)
    ciphertext = encrypt(plaintext, key_matrix)

    print("\nKey Matrix:")
    for row in key_matrix:
        print(row)

    print("\nEncrypted Text:", ciphertext)

if __name__ == "__main__":
    main()


def main():
    key = input("Enter the key for the Playfair Cipher: ").upper()
    plaintext = input("Enter the plaintext: ").upper()

    key_matrix = generate_key(key)
    ciphertext = encrypt(plaintext, key_matrix)

    print("\nKey Matrix:")
    for row in key_matrix:
        print(row)

    print("\nEncrypted Text:", ciphertext)
if __name__ == "__main__":
    main()
