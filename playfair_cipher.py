def create_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    letters = ""
    for char in keyword:
        if char in alphabet and char not in letters:
            letters += char
    for char in alphabet:
        if char not in letters:
            letters += char
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(letters[i:i+5])
    return matrix

def find_position(matrix, char):
    if char == "J":
        char = "I"
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(char for char in text if char.isalpha())
    pairs = []
    i = 0
    while i < len(text):
        first = text[i]
        if i + 1 < len(text):
            second = text[i + 1]
            if first == second:
                pairs.append(first + "X")
                i += 1
            else:
                pairs.append(first + second)
                i += 2
        else:
            pairs.append(first + "X")
            i += 1
    return pairs

def encrypt_pair(pair, matrix):
    a, b = pair
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    if row1 == row2:
        new_a = matrix[row1][(col1 + 1) % 5]
        new_b = matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        new_a = matrix[(row1 + 1) % 5][col1]
        new_b = matrix[(row2 + 1) % 5][col2]
    else:
        new_a = matrix[row1][col2]
        new_b = matrix[row2][col1]
    return new_a + new_b

def decrypt_pair(pair, matrix):
    a, b = pair
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    if row1 == row2:
        new_a = matrix[row1][(col1 - 1) % 5]
        new_b = matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        new_a = matrix[(row1 - 1) % 5][col1]
        new_b = matrix[(row2 - 1) % 5][col2]
    else:
        new_a = matrix[row1][col2]
        new_b = matrix[row2][col1]
    return new_a + new_b

def print_matrix(matrix):
    print("Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))

while True:
    print("===== Playfair Cipher =====")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        keyword = input("Enter keyword: ")
        plaintext = input("Enter plaintext: ")
        matrix = create_matrix(keyword)
        print_matrix(matrix)
        pairs = prepare_text(plaintext)
        ciphertext = ""
        for pair in pairs:
            ciphertext += encrypt_pair(pair, matrix)
        print("Pairs:", " ".join(pairs))
        print("Ciphertext:", ciphertext)
    elif choice == "2":
        keyword = input("Enter keyword: ")
        ciphertext = input("Enter ciphertext: ")
        matrix = create_matrix(keyword)
        print_matrix(matrix)
        ciphertext = ciphertext.upper().replace("J", "I")
        ciphertext = "".join(char for char in ciphertext if char.isalpha())
        plaintext = ""
        for i in range(0, len(ciphertext), 2):
            pair = ciphertext[i:i+2]
            if len(pair) == 2:
                plaintext += decrypt_pair(pair, matrix)
        print("Plaintext:", plaintext)
    elif choice == "3":
        print("Program ended.")
        break
    else:
        print("Invalid choice!")