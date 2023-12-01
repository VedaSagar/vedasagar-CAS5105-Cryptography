def generate_subkeys(block_cipher, block_size):
    if block_size == 64:
        constant = 0x1B
    elif block_size == 128:
        constant = 0x87
    else:
        raise ValueError("Unsupported block size")
    zero_block = bytes([0] * (block_size // 8))
    subkey_1 = block_cipher.encrypt(zero_block)
    subkey_1 = shift_left(subkey_1, block_size)
    if (subkey_1[0] & 0x80) == 0x80:
        subkey_1 = bytes([((byte << 1) ^ constant) & 0xFF for byte in subkey_1])
    else:
        subkey_1 = bytes([byte << 1 for byte in subkey_1])
    subkey_2 = shift_left(subkey_1, block_size)
    if (subkey_2[0] & 0x80) == 0x80:
        subkey_2 = bytes([((byte << 1) ^ constant) & 0xFF for byte in subkey_2])
    else:
        subkey_2 = bytes([byte << 1 for byte in subkey_2])

    return subkey_1, subkey_2

def shift_left(data, block_size):
    result = bytearray(data)
    carry = 0
    for i in range(len(result) - 1, -1, -1):
        new_carry = (result[i] & (1 << (8 - block_size % 8))) >> (8 - block_size % 8)
        result[i] = ((result[i] << 1) & 0xFF) | carry
        carry = new_carry
    return bytes(result)

if __name__ == "__main__":
    block_size = 128
    key = b'your_key'

    cipher = AES.new(key, AES.MODE_ECB)

    subkey_1, subkey_2 = generate_subkeys(cipher, block_size)

    print(f"Subkey 1: {subkey_1.hex()}")
    print(f"Subkey 2: {subkey_2.hex()}")
