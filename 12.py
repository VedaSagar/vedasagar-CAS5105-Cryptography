import binascii

def permute(original, table):
    return ''.join(original[i - 1] for i in table)

def generate_keys(key):
    # Perform the initial permutation on the key
    key = permute(key, PC1)

    # Split the key into two halves
    left, right = key[:28], key[28:]

    # Generate 16 subkeys using the key schedule
    subkeys = []
    for i in range(16):
        left = left_shift(left, SHIFT_SCHEDULE[i])
        right = left_shift(right, SHIFT_SCHEDULE[i])
        subkey = permute(left + right, PC2)
        subkeys.append(subkey)

    return subkeys[::-1]  # Reverse the subkeys for decryption

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def encrypt_block(block, subkeys):
    # Initial permutation
    block = permute(block, IP)

    # Split the block into two halves
    left, right = block[:32], block[32:]

    # 16 rounds of Feistel network
    for i in range(15, -1, -1):
        new_right = permute(right, E_BIT_SELECTION)
        new_right = xor(new_right, subkeys[i])
        new_right = substitute(new_right)
        new_right = permute(new_right, P)

        new_right = xor(left, new_right)

        left, right = right, new_right

    # Final permutation
    ciphertext = permute(right + left, IP_INVERSE)
    return ciphertext

def xor(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

def substitute(bits):
    result = ''
    for i in range(8):
        block = bits[i * 6: (i + 1) * 6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        result += format(S_BOXES[i][row][col], '04b')
    return result

def des_decrypt(ciphertext, key):
    subkeys = generate_keys(key)
    plaintext = ''

    for block in divide_into_blocks(ciphertext, 64):
        block = encrypt_block(block, subkeys)
        plaintext += block

    return hex_to_ascii(binary_to_hex(plaintext))

def divide_into_blocks(text, block_size):
    return [text[i:i+block_size] for i in range(0, len(text), block_size)]

def hex_to_binary(hex_text):
    return bin(int(hex_text, 16))[2:]

def binary_to_hex(binary_text):
    return hex(int(binary_text, 2))[2:]

def hex_to_ascii(hex_text):
    return binascii.unhexlify(hex_text).decode('utf-8')

# Permutation tables and S-boxes
IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

IP_INVERSE = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

E_BIT_SELECTION = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11,
                   12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21,
                   22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2,
       59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39,
       31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37,
       29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 
