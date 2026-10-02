def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def main():
    print("===== RSA Cryptosystem Implementation =====")
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    n = p * q
    phi = (p - 1) * (q - 1)
    print("Computed n =", n)
    print("Computed phi (n) =", phi)

    e = int(input("\nEnter public exponent e (gcd(e, phi) = 1): "))

    if gcd(e, phi) != 1:
        print("Invalid e! gcd(e, phi) must be 1.")
        return
    d = mod_inverse(e, phi)
    if d == -1:
        print("Modular inverse not found!")
        return
    print("Public Key (e, n):", (e, n))
    print("Private Key (d, n):", (d, n))

    while True:
        print("========== MENU ==========")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = int(input("Choose option: "))
        if choice == 1:
            m = int(input(f"Enter plaintext (0 <= m < {n}): "))
            if m < 0 or m >= n:
                print("Invalid message range!")
                continue
            C = mod_exp(m, e, n)
            print("Encrypted Ciphertext:", C)
        elif choice == 2:
            C = int(input("Enter ciphertext: "))
            m = mod_exp(C, d, n)
            print("Decrypted Plaintext:", m)
        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")
if __name__ == "__main__":
    main()