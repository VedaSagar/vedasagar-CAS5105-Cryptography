import numpy as np

MATRIX_SIZE = 2

def encrypt_hill_cipher(message, key):
    message = message.upper().replace(" ", "")

    # Check if the message length is even, if not, pad with 'X'
    if len(message) % MATRIX_SIZE != 0:
        pad_len = MATRIX_SIZE - (len(message) % MATRIX_SIZE)
        message += 'X' * pad_len

    # Convert characters to numbers (A=0, B=1, ..., Z=25)
    matrix = np.array([[ord(char) - ord('A') for char in message[i:i+MATRIX_SIZE]] for i in range(0, len(message), MATRIX_SIZE)])

    # Multiply the matrix with the key
    result = np.dot(key, matrix.T) % 26

    # Convert numbers back to characters and print the encrypted message
    encrypted_message = ''.join([chr(char + ord('A')) for row in result.T for char in row])
    print("Encrypted Message:", encrypted_message)

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1

def decrypt_hill_cipher(ciphertext, key):
    # Convert characters to numbers (A=0, B=1, ..., Z=25)
    matrix = np.array([[ord(char) - ord('A') for char in ciphertext[i:i+MATRIX_SIZE]] for i in range(0, len(ciphertext), MATRIX_SIZE)])

    # Find the determinant of the key matrix
    det = np.linalg.det(key)
    det = int(np.round(det)) % 26

    # Calculate the modular inverse of the determinant
    det_inverse = mod_inverse(det, 26)

    # Calculate the adjugate of the key matrix
    adjugate = (det_inverse * np.round(det * np.linalg.inv(key)).astype(int)) % 26

    # Calculate the inverse of the key matrix
    key_inverse = (det_inverse * adjugate) % 26

    # Multiply the inverse of the key matrix with the ciphertext
    result = np.dot(key_inverse, matrix.T) % 26

    # Convert numbers back to characters and print the decrypted message
    decrypted_message = ''.join([chr(char + ord('A')) for row in result.T for char in row])
    print("Decrypted Message:", decrypted_message)

def main():
    message = "MEET ME AT THE USUAL PLACE AT TEN RATHER THAN EIGHT OCLOCK"
    key = np.array([[9, 4], [5, 7]])

    # Encrypt the message
    encrypt_hill_cipher(message, key)

    # Corresponding decryption of the ciphertext
    ciphertext = "HCXFAMRKPKHJZTDPMMUDHJ"
    decrypt_hill_cipher(ciphertext, key)

if _name_ == "_main_":
    main()
