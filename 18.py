import hashlib

def sha3_initialization():
    block_size = 1024
    rate = 1600
    capacity = rate - block_size
    state_size = rate // 64 
    internal_state = [[0] * state_size for _ in range(state_size)]
    iterations = 0

    while any(all(value == 0 for value in row) for row in internal_state):
        input_data = bytes(f"MessageBlock{iterations}", 'utf-8')
        hash_obj = hashlib.sha3_512(input_data)
        hash_digest = hash_obj.digest()
        for i in range(state_size):
            for j in range(state_size):
                internal_state[i][j] ^= int.from_bytes(hash_digest[i * 8 + j * state_size * 8 : (i + 1) * 8 + j * state_size * 8], byteorder='big')

        iterations += 1

    return internal_state, iterations

if __name__ == "__main__":
    final_state, num_iterations = sha3_initialization()

    print("Final Internal State Matrix:")
    for row in final_state:
        print(row)

    print(f"\nNumber of Iterations: {num_iterations}")
