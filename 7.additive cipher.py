import string

def caesar_decrypt(ciphertext, key):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr((ord(char) - key - ord('A')) % 26 + ord('A')) if char.isupper() else chr((ord(char) - key - ord('a')) % 26 + ord('a'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def letter_frequency(text):
    letter_count = {letter: 0 for letter in string.ascii_uppercase}
    total_letters = 0

    for char in text:
        if char.isalpha():
            letter_count[char.upper()] += 1
            total_letters += 1

    frequencies = {letter: count / total_letters for letter, count in letter_count.items()}
    return frequencies

def possible_plaintexts(ciphertext, num_plaintexts=10):
    results = []

    for key in range(26):
        decrypted_text = caesar_decrypt(ciphertext, key)
        frequency = letter_frequency(decrypted_text)
        score = sum(frequency[letter] * expected_frequency[letter] for letter in string.ascii_uppercase)

        results.append({'key': key, 'plaintext': decrypted_text, 'score': score})

    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:num_plaintexts]

expected_frequency = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253,
    'E': 0.12702, 'F': 0.02228, 'G': 0.02015, 'H': 0.06094,
    'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025,
    'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 'P': 0.01929,
    'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
    'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150,
    'Y': 0.01974, 'Z': 0.00074
}

def main():
    ciphertext = "LXFOPVEFRNHR"

    print("Ciphertext:", ciphertext)

    possible_texts = possible_plaintexts(ciphertext)
    print("\nTop 10 Possible Plaintexts:")
    for i, result in enumerate(possible_texts, start=1):
        print(f"{i}. Key: {result['key']}, Score: {result['score']:.4f}, Plaintext: {result['plaintext']}")

if __name__ == "__main__":
    main()
