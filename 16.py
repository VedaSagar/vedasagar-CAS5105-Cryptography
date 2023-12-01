def generate_subkeys(block_size):
    if block_size == 64:
        constant = 0x1B  
    elif block_size == 128:
        constant = 0x87  
    else:
        raise ValueError("Unsupported block size")

   
    if block_size == 64:
        shift_value = 0x80
        mask_value = 0x7F
    elif block_size == 128:
        shift_value = 0x80000000000000000000000000000000
        mask_value = 0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF80000000000000000000000000000000

   
    first_subkey = constant if (shift_value & 0x80) else 0
    first_subkey <<= 1
    first_subkey &= mask_value


    second_subkey = constant if (first_subkey & 0x8000000000000000) else 0
    second_subkey <<= 1
    second_subkey &= mask_value

    return first_subkey, second_subkey

if __name__ == "__main__":
   
    block_size_64_constants = generate_subkeys(64)
    block_size_128_constants = generate_subkeys(128)

    
    print("Constants for 64-bit block size:", block_size_64_constants)
    print("Constants for 128-bit block size:", block_size_128_constants)
