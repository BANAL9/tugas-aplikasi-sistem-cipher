from .caesar import CaesarCipher
from .transposition import TranspositionCipher


class SuperEncryption:
    """
    Super Encryption / Product Cipher:
    Caesar Cipher + Columnar Transposition Cipher.
    """

    @staticmethod
    def encrypt(text: str, caesar_shift: int, transposition_key: str) -> str:
        stage1 = CaesarCipher.encrypt(text, caesar_shift)
        return TranspositionCipher.encrypt(stage1, transposition_key)

    @staticmethod
    def decrypt(
        ciphertext: str, caesar_shift: int, transposition_key: str
    ) -> str:
        stage1 = TranspositionCipher.decrypt(ciphertext, transposition_key)
        return CaesarCipher.decrypt(stage1, caesar_shift)
