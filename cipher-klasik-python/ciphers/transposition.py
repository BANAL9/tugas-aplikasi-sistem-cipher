class TranspositionCipher:
    """
    Columnar Transposition Cipher.

    Padding tidak ditambahkan. Dengan demikian hasil dekripsi dapat
    dikembalikan persis ke plaintext asli, termasuk panjang teks.
    """

    @staticmethod
    def _clean_key(key: str) -> str:
        if not isinstance(key, str):
            raise TypeError("Kunci transposisi harus berupa string.")

        clean = "".join(c.upper() for c in key if c.isalpha())
        if not clean:
            raise ValueError(
                "Kunci transposisi harus mengandung setidaknya satu huruf."
            )
        return clean

    @classmethod
    def _column_order(cls, key: str) -> list[int]:
        # sort stabil berdasarkan huruf lalu posisi asli,
        # sehingga kunci dengan huruf berulang tetap deterministik.
        return sorted(range(len(key)), key=lambda i: (key[i], i))

    @classmethod
    def encrypt(cls, text: str, key: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Teks harus berupa string.")

        key = cls._clean_key(key)
        cols = len(key)

        # Setiap kolom mendapat jumlah karakter sesuai posisi kolomnya.
        rows = (len(text) + cols - 1) // cols
        if not text:
            return ""

        column_lengths = [
            rows if col < (len(text) % cols or cols) else rows - 1
            for col in range(cols)
        ]

        result = []
        for col in cls._column_order(key):
            for row in range(column_lengths[col]):
                idx = row * cols + col
                if idx < len(text):
                    result.append(text[idx])

        return "".join(result)

    @classmethod
    def decrypt(cls, ciphertext: str, key: str) -> str:
        if not isinstance(ciphertext, str):
            raise TypeError("Ciphertext harus berupa string.")

        key = cls._clean_key(key)
        cols = len(key)

        if not ciphertext:
            return ""

        rows = (len(ciphertext) + cols - 1) // cols
        remainder = len(ciphertext) % cols

        # Pada plaintext yang ditulis per baris tanpa padding,
        # kolom 0..remainder-1 memiliki satu karakter lebih banyak.
        column_lengths = [
            rows if (remainder == 0 or col < remainder) else rows - 1
            for col in range(cols)
        ]

        columns = [""] * cols
        pos = 0

        for col in cls._column_order(key):
            length = column_lengths[col]
            columns[col] = ciphertext[pos:pos + length]
            pos += length

        result = []
        for row in range(rows):
            for col in range(cols):
                if row < len(columns[col]):
                    result.append(columns[col][row])

        return "".join(result)
