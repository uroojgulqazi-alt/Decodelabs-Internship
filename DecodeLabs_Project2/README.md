# Cyber Security Project 2 — Basic Encryption & Decryption

## 1. Project Overview

This project implements a basic encryption and decryption technique using a Caesar cipher.

The program:
- accepts text from the user;
- accepts a user-selected shift key;
- encrypts the text;
- displays the encrypted text;
- decrypts the encrypted text;
- displays the decrypted result;
- validates menu choices, messages, and shift keys.

The project demonstrates basic encryption concepts, programming logic, and data confidentiality.

## 2. How the Caesar Cipher Works

A Caesar cipher shifts alphabetic characters by a fixed number of positions.

For example, with a shift of 3:

A -> D
B -> E
C -> F

At the end of the alphabet, the cipher wraps around:

X -> A
Y -> B
Z -> C

Decryption reverses the shift.

## 3. Requirements

- Python 3.x
- No external Python packages are required.

## 4. Run the Application

Open a terminal in this folder and run:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## 5. Example

Input:

```text
Enter your choice: 1
Enter your message: Hello World
Enter the shift key (0-25): 3
```

Output:

```text
Original Text  : Hello World
Shift Key      : 3
Encrypted Text : Khoor Zruog
Decrypted Text : Hello World
```

## 6. Validation

The application:
- rejects an empty message;
- rejects non-numeric shift keys;
- rejects shift values outside 0–25;
- rejects invalid menu choices.

## 7. Testing

Run the automated tests with:

```bash
python -m unittest test_main.py -v
```

The test suite covers uppercase/lowercase text, wrap-around, spaces, punctuation, numbers, decryption, round-trip correctness, and equivalent large shifts.

## 8. Security Note

A Caesar cipher is a learning example and is not suitable for protecting sensitive real-world information. It has a very small key space and can be broken easily. This project is intended to demonstrate fundamental encryption and decryption logic.
