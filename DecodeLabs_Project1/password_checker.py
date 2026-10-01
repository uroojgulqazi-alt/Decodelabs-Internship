# ============================================================
# DecodeLabs - Cyber Security Internship
# Project 1: Password Strength Checker
# ============================================================

# Common passwords that should be avoided
COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "iloveyou",
    "abc123"
}


# ------------------------------------------------------------
# Get password from user
# ------------------------------------------------------------

password = input("Enter your password: ")

if not password:
    print("\nError: Password cannot be empty.")
    exit()


# ------------------------------------------------------------
# Password checks
# ------------------------------------------------------------

length = len(password)

has_uppercase = any(char.isupper() for char in password)

has_lowercase = any(char.islower() for char in password)

has_number = any(char.isdigit() for char in password)

symbols = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"

has_symbol = any(char in symbols for char in password)


# Check whether the password is a commonly used password
is_common = password.lower() in COMMON_PASSWORDS


# ------------------------------------------------------------
# Calculate password strength
# ------------------------------------------------------------

score = 0

# Length
if length >= 12:
    score += 2
elif length >= 8:
    score += 1


# Uppercase
if has_uppercase:
    score += 1


# Lowercase
if has_lowercase:
    score += 1


# Number
if has_number:
    score += 1


# Symbol
if has_symbol:
    score += 1


# Common password penalty
if is_common:
    score = 0


# ------------------------------------------------------------
# Determine strength
# ------------------------------------------------------------

if is_common:
    strength = "VERY WEAK"

elif score <= 2:
    strength = "WEAK"

elif score <= 4:
    strength = "MEDIUM"

else:
    strength = "STRONG"


# ------------------------------------------------------------
# Display results
# ------------------------------------------------------------

print("\n" + "=" * 45)
print("       PASSWORD SECURITY ANALYSIS")
print("=" * 45)

print("\nPassword Requirements:")

if length >= 8:
    print("[PASS] Minimum 8 characters")
else:
    print("[FAIL] Minimum 8 characters")

if length >= 12:
    print("[PASS] 12 or more characters")
else:
    print("[INFO] 12 or more characters recommended")

if has_uppercase:
    print("[PASS] Contains uppercase letter")
else:
    print("[FAIL] Contains uppercase letter")

if has_lowercase:
    print("[PASS] Contains lowercase letter")
else:
    print("[FAIL] Contains lowercase letter")

if has_number:
    print("[PASS] Contains number")
else:
    print("[FAIL] Contains number")

if has_symbol:
    print("[PASS] Contains symbol")
else:
    print("[FAIL] Contains symbol")

if is_common:
    print("[FAIL] Common password detected")
else:
    print("[PASS] Not detected as a common password")


# ------------------------------------------------------------
# Final result
# ------------------------------------------------------------

print("\n" + "-" * 45)
print("PASSWORD STRENGTH:", strength)
print("Security Score:", score, "/ 6")
print("-" * 45)


# ------------------------------------------------------------
# Suggestions
# ------------------------------------------------------------

if strength != "STRONG":

    print("\nSuggestions to improve your password:")

    if length < 8:
        print("- Use at least 8 characters.")

    if length < 12:
        print("- Consider using 12 or more characters.")

    if not has_uppercase:
        print("- Add at least one uppercase letter.")

    if not has_lowercase:
        print("- Add at least one lowercase letter.")

    if not has_number:
        print("- Add at least one number.")

    if not has_symbol:
        print("- Add at least one special symbol.")

    if is_common:
        print("- Avoid common or easily guessed passwords.")

else:
    print("\nYour password meets all the basic security checks.")

print("\nNote: This checker provides a basic security assessment.")
print("It does not guarantee that a password is impossible to crack.") 