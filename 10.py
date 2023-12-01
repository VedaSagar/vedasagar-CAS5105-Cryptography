import string

def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            decrypted_char = chr((ord(char) - shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def letter_frequency(text):
    frequency = {}
    total_letters = 0

    for char in text:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
            total_letters += 1

    for char in frequency:
        frequency[char] = frequency[char] / total_letters

    return frequency

def possible_plaintexts(ciphertext, top_n=10):
    letter_frequencies_english = {
        'E': 0.127, 'T': 0.090, 'A': 0.081, 'O': 0.075, 'I': 0.070,
        'N': 0.067, 'S': 0.063, 'H': 0.061, 'R': 0.060, 'D': 0.043,
        'L': 0.040, 'U': 0.028, 'C': 0.027, 'M': 0.024, 'F': 0.022,
        'Y': 0.020, 'W': 0.018, 'G': 0.016, 'P': 0.015, 'B': 0.012,
        'V': 0.011, 'K': 0.006, 'X': 0.002, 'Q': 0.001, 'J': 0.001, 'Z': 0.001
    }

    possible_texts = []

    for shift in range(26):
        decrypted_text = decrypt_caesar(ciphertext, shift)
        decrypted_frequency = letter_frequency(decrypted_text)

        # Calculate the sum of squared differences between observed and expected frequencies
        sum_squared_diff = sum((decrypted_frequency.get(char, 0) - letter_frequencies_english[char]) ** 2
                               for char in string.ascii_uppercase)

        possible_texts.append({
            'text': decrypted_text,
            'shift': shift,
            'sum_squared_diff': sum_squared_diff
        })

    # Sort by the sum of squared differences in ascending order
    possible_texts.sort(key=lambda x: x['sum_squared_diff'])

    return possible_texts[:top_n]

if __name__ == "__main__":
    # Example usage
    ciphertext = "Wklv lv d whvw phvvdjh lv dwhvw wkh lvvw oryh dw wlph udqjh lv"
    top_n = 5

    possible_texts = possible_plaintexts(ciphertext, top_n)

    print(f"Top {top_n} possible plaintexts:")
    for i, result in enumerate(possible_texts, 1):
        print(f"\nOption {i}:")
        print(f"Shift: {result['shift']}")
        print(f"Plaintext: {result['text']}")
