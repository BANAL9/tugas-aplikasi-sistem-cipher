class CaesarCipher:
    """Caesar Cipher: substitusi alfabet dengan pergeseran tertentu."""

    @staticmethod
    def encrypt(text: str, shift: int) -> str:
        if not isinstance(text, str):
            raise TypeError("Teks harus berupa string.")
        if not isinstance(shift, int):
            raise TypeError("Shift harus berupa integer.")

        result = []
        for char in text:
            if "A" <= char <= "Z":
                result.append(chr((ord(char) - ord("A") + shift) % 26 + ord("A")))
            elif "a" <= char <= "z":
                result.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
            else:
                result.append(char)
        return "".join(result)

    @staticmethod
    def decrypt(text: str, shift: int) -> str:
        return CaesarCipher.encrypt(text, -shift)
