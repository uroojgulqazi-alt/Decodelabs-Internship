"""
Cyber Security Project 2
Basic Encryption & Decryption using a Caesar Cipher

Author: DecodeLabs Intern
Purpose: Demonstrate basic reversible encryption and decryption.
"""

def encrypt(text, shift):
    """Encrypt text using a Caesar cipher."""
    result = ""

    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def decrypt(text, shift):
    """Decrypt Caesar-ciphered text using the same shift key."""
    return encrypt(text, -shift)


def get_shift():
    """Get and validate a numeric shift key from the user."""
    while True:
        try:
            shift = int(input("Enter the shift key (0-25): "))

            if 0 <= shift <= 25:
                return shift

            print("Please enter a shift between 0 and 25.")

        except ValueError:
            print("Please enter a valid whole number.")


def run_encryption():
    """Read input, encrypt it, decrypt it, and display the results."""
    message = input("\nEnter your message: ")

    if not message.strip():
        print("Message cannot be empty.")
        return

    shift = get_shift()

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\n----------- RESULTS -----------")
    print("Original Text  :", message)
    print("Shift Key      :", shift)
    print("Encrypted Text :", encrypted)
    print("Decrypted Text :", decrypted)
    print("-------------------------------")


def main():
    """Run the main application menu."""
    print("=" * 40)
    print("       BASIC ENCRYPTION TOOL")
    print("=" * 40)

    while True:
        print("\n1. Encrypt and Decrypt")
        print("2. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            run_encryption()

        elif choice == "2":
            print("\nThank you for using the Basic Encryption Tool!")
            break

        else:
            print("\nInvalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
