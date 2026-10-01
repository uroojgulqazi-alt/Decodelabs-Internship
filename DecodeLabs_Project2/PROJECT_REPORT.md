# Cyber Security Project 2 — Project Report

## Title
Basic Encryption & Decryption Using a Caesar Cipher

## Objective
The objective of this project is to implement a simple encryption and decryption technique using programmatic logic.

## Method Used
The project uses the Caesar cipher. Each alphabetic character is shifted by a fixed number of positions. Decryption applies the reverse shift to recover the original text.

## Features
- User-provided message.
- User-selected shift key.
- Encryption of uppercase and lowercase letters.
- Preservation of spaces, numbers, and punctuation.
- Decryption of encrypted text.
- Input validation.
- Menu-based interface.
- Automated unit tests.

## Algorithm
1. Read the message.
2. Read and validate the shift key.
3. Process each character.
4. If the character is alphabetic, shift it by the key.
5. Use modulo 26 to wrap around the alphabet.
6. Leave non-alphabetic characters unchanged.
7. Display the encrypted text.
8. Decrypt the encrypted text using the negative shift.
9. Display the decrypted text.

## Example
Original:
Hello World

Shift:
3

Encrypted:
Khoor Zruog

Decrypted:
Hello World

## Testing
The application was designed to test normal encryption, decryption, alphabet wrap-around, lowercase and uppercase letters, punctuation, numbers, invalid input, and round-trip correctness.

## Conclusion
The project demonstrates the basic relationship between encryption and decryption through a reversible Caesar cipher. It provides a simple practical introduction to encryption concepts and data confidentiality.

## Limitation
The Caesar cipher is not secure for real-world confidential data. It is used here as an educational example of basic cryptographic logic.
