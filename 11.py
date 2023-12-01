def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_allowed_a():
    allowed_a = []
    for a in range(26):
        if gcd(a, 26) == 1:
            allowed_a.append(a)
    return allowed_a

def find_allowed_b():
    return list(range(26))

if __name__ == "__main__":
    # Find allowed values for a
    allowed_a = find_allowed_a()

    # Find limitations on b
    allowed_b = find_allowed_b()

    print("Allowed values for 'a':", allowed_a)
    print("Allowed values for 'b':", allowed_b)
