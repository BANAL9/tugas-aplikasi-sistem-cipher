import unittest

from ciphers import CaesarCipher, TranspositionCipher, SuperEncryption


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(CaesarCipher.encrypt("Hello World!", 3), "Khoor Zruog!")

    def test_decrypt(self):
        self.assertEqual(CaesarCipher.decrypt("Khoor Zruog!", 3), "Hello World!")

    def test_large_and_negative_shift(self):
        self.assertEqual(CaesarCipher.encrypt("ABC", 26), "ABC")
        self.assertEqual(CaesarCipher.encrypt("ABC", -1), "ZAB")


class TestTranspositionCipher(unittest.TestCase):
    def test_round_trip_various_lengths(self):
        for text in ["", "A", "HELLO", "MENGANTUK", "HELLOWORLD", "123 ABC!"]:
            encrypted = TranspositionCipher.encrypt(text, "TOMBAK")
            self.assertEqual(TranspositionCipher.decrypt(encrypted, "TOMBAK"), text)

    def test_repeated_key_characters(self):
        text = "CONTOH TEKS"
        key = "BALLOON"
        encrypted = TranspositionCipher.encrypt(text, key)
        self.assertEqual(TranspositionCipher.decrypt(encrypted, key), text)

    def test_invalid_key(self):
        with self.assertRaises(ValueError):
            TranspositionCipher.encrypt("ABC", "123")


class TestSuperEncryption(unittest.TestCase):
    def test_round_trip(self):
        text = "MENGANTUK 123!"
        encrypted = SuperEncryption.encrypt(text, 3, "TOMBAK")
        self.assertEqual(SuperEncryption.decrypt(encrypted, 3, "TOMBAK"), text)


if __name__ == "__main__":
    unittest.main()
