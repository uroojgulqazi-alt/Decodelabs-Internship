# Password Strength Checker

## DecodeLabs Cyber Security Internship - Project 1

### Project Overview

The Password Strength Checker is a Python-based cybersecurity project developed as part of the DecodeLabs Cyber Security Internship.

The purpose of this project is to evaluate the basic security strength of a password using string handling, conditional logic, and security-focused validation.

The program checks different password characteristics and classifies the password as:

* VERY WEAK
* WEAK
* MEDIUM
* STRONG

The project focuses on fundamental security logic rather than complex hacking techniques.

---

## Project Objectives

The main objectives of this project are to:

* Check password length
* Detect uppercase letters
* Detect lowercase letters
* Detect numbers
* Detect special symbols
* Identify commonly used passwords
* Calculate a password security score
* Classify the password according to its characteristics
* Provide suggestions for improving weak passwords

The core requirements of the DecodeLabs project are to check password length, numbers, symbols, uppercase letters, and display the password-strength result.

---

## Technologies Used

* Python 3
* Python string methods
* Conditional statements
* `any()` function
* Set data structure
* Command-Line Interface (CLI)

---

## Features

### 1. Password Length Check

The program checks the total number of characters in the password.

Passwords with 8 or more characters satisfy the minimum length requirement.

Passwords with 12 or more characters receive additional strength points.

### 2. Uppercase Letter Detection

The program checks whether the password contains at least one uppercase letter.

Example:

```text
A
B
C
```

### 3. Lowercase Letter Detection

The program checks whether the password contains lowercase letters.

Example:

```text
a
b
c
```

### 4. Number Detection

The program checks whether the password contains numeric characters.

Example:

```text
0 1 2 3 4 5 6 7 8 9
```

### 5. Symbol Detection

The program checks for special characters such as:

```text
! @ # $ % ^ & *
```

### 6. Common Password Detection

The program contains a small list of commonly used passwords.

If a password matches one of these common passwords, it is classified as VERY WEAK.

This feature was added as an improvement beyond the minimum requirements. The DecodeLabs project encourages experimentation with checks for common or leaked passwords and additional character-variety requirements.

Note: The built-in list is only a small demonstration list. It is not a complete database of leaked passwords.

### 7. Security Score

The program assigns points based on password characteristics.

The score considers:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Symbols

A common password receives a security penalty.

### 8. Improvement Suggestions

If the password is not strong enough, the program provides suggestions such as:

* Use more characters
* Add uppercase letters
* Add lowercase letters
* Add numbers
* Add symbols
* Avoid common passwords

---

## How the Program Works

The basic process is:

```text
User enters password
        |
        v
Check password length
        |
        v
Check uppercase letters
        |
        v
Check lowercase letters
        |
        v
Check numbers
        |
        v
Check symbols
        |
        v
Check common password list
        |
        v
Calculate security score
        |
        v
Determine password strength
        |
        v
Display result and suggestions
```

---

## How to Run

### Step 1 - Install Python

Make sure Python 3 is installed on your computer.

Check the installation using:

```bash
python --version
```

### Step 2 - Open the Project Folder

Open the project folder in VS Code.

The folder should contain:

```text
DecodeLabs_Project1/
|
├── password_checker.py
└── README.md
```

### Step 3 - Run the Program

Open the VS Code terminal and run:

```bash
python password_checker.py
```

### Step 4 - Enter a Test Password

When prompted:

```text
Enter your password:
```

Enter a test password.

Do not use an actual personal password for testing or screenshots.

---

## Test Cases

### Test Case 1 - Weak Password

Input:

```text
abc
```

Expected result:

```text
PASSWORD STRENGTH: WEAK
```

Reason:

* Too short
* No uppercase letter
* No number
* No symbol

---

### Test Case 2 - Medium Password

Input:

```text
Jiya1234
```

Expected result:

```text
PASSWORD STRENGTH: MEDIUM
```

The password contains:

* Uppercase letter
* Lowercase letters
* Numbers

However, it does not contain a symbol and is shorter than the recommended 12 characters.

---

### Test Case 3 - Strong Password

Input:

```text
Jiya@Cyber2026!
```

Expected result:

```text
PASSWORD STRENGTH: STRONG
```

The password contains:

* 12 or more characters
* Uppercase letters
* Lowercase letters
* Numbers
* Symbols

---

### Test Case 4 - Common Password

Input:

```text
password123
```

Expected result:

```text
PASSWORD STRENGTH: VERY WEAK
```

The program identifies it as a commonly used password.

---

## Security Considerations

This project is a basic rule-based password strength checker.

It does not:

* Guarantee that a password cannot be cracked
* Perform real password-cracking attempts
* Check every leaked password ever published
* Measure real-world password entropy precisely
* Replace professional password-security systems

The purpose is to demonstrate fundamental cybersecurity concepts including data validation, string handling, conditional logic, and password-security awareness.

---

## Skills Demonstrated

This project demonstrates practical understanding of:

* Python programming
* String manipulation
* Conditional statements
* Boolean logic
* Iteration
* Character classification
* Basic security validation
* Input validation
* Command-line programming
* Security-oriented problem solving

These skills correspond to the project's stated focus on string handling, condition checks, and security basics.

---

## Future Improvements

Possible future improvements include:

* A larger vetted common-password dataset
* Password entropy estimation
* Detection of repeated characters
* Detection of sequential patterns such as `123456`
* Detection of keyboard patterns such as `qwerty`
* A graphical user interface
* Password-generation functionality
* More detailed security feedback
* Unit testing

---

## Project Information

Program: Cyber Security

Internship: DecodeLabs Industrial Training

Project: Project 1 - Password Strength Checker

Language: Python 3

---

## Conclusion

The Password Strength Checker demonstrates how basic Python programming can be applied to a cybersecurity problem.

By combining string handling, conditional checks, character validation, scoring, and common-password detection, the program provides a simple assessment of password strength.

This project serves as a foundation for understanding defensive cybersecurity and security-focused programming.
