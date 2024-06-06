def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters are not changed
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        print("\nCaesar Cipher Program")
        choice = input("Do you want to encrypt or decrypt a message? (e/d) or (q to quit): ").lower()
        
        if choice == 'q':
            print("Exiting program.")
            break
        elif choice not in ['e', 'd']:
            print("Invalid choice. Please select 'e' for encryption, 'd' for decryption, or 'q' to quit.")
            continue
        
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == 'e':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
            verify_choice = input("Do you want to decrypt this message to verify? (y/n): ").lower()
            if verify_choice == 'y':
                decrypted_message = decrypt(encrypted_message, shift)
                print(f"Decrypted message: {decrypted_message}")
        else:
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
            verify_choice = input("Do you want to encrypt this message to verify? (y/n): ").lower()
            if verify_choice == 'y':
                encrypted_message = encrypt(decrypted_message, shift)
                print(f"Encrypted message: {encrypted_message}")

if __name__ == "__main__":
    main()
