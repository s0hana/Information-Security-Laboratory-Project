while True:
    print("===== Caesar Cipher =====")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter plaintext: ")
        result = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    result += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
                else:
                    result += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            else:
                result += char
        print("Encrypted text:", result)
    elif choice == "2":
        text = input("Enter ciphertext: ")
        result = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    result += chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
                else:
                    result += chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
            else:
                result += char
        print("Decrypted text:", result)
    elif choice == "3":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please try again.")