import unittest
from main import encrypt, decrypt


class TestCaesarCipher(unittest.TestCase):

    def test_uppercase(self):
        self.assertEqual(encrypt("HELLO", 3), "KHOOR")

    def test_lowercase(self):
        self.assertEqual(encrypt("hello", 3), "khoor")

    def test_wraparound(self):
        self.assertEqual(encrypt("XYZ", 3), "ABC")

    def test_spaces_and_punctuation(self):
        self.assertEqual(encrypt("Hello, World!", 3), "Khoor, Zruog!")

    def test_numbers_remain_unchanged(self):
        self.assertEqual(encrypt("Test 123", 3), "Whvw 123")

    def test_decryption(self):
        self.assertEqual(decrypt("KHOOR", 3), "HELLO")

    def test_encrypt_decrypt_round_trip(self):
        message = "Cyber Security Project 2!"
        encrypted = encrypt(message, 7)
        decrypted = decrypt(encrypted, 7)
        self.assertEqual(decrypted, message)

    def test_large_shift_equivalence(self):
        self.assertEqual(encrypt("ABC", 29), encrypt("ABC", 3))


if __name__ == "__main__":
    unittest.main()
