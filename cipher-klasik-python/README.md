# Classic Cipher Engine in Python

Aplikasi **Command Line Interface (CLI)** untuk mempelajari dan menjalankan kriptografi klasik menggunakan Python.

## Fitur

1. **Caesar Cipher**
   - Enkripsi dan dekripsi.
   - Mendukung huruf besar dan kecil.
   - Angka, spasi, dan simbol tidak diubah.
   - Mendukung shift positif maupun negatif.

2. **Columnar Transposition Cipher**
   - Menggunakan kata kunci.
   - Mendukung kunci dengan huruf berulang.
   - Tidak memakai padding `X`, sehingga hasil dekripsi kembali persis seperti plaintext.
   - Spasi, angka, dan simbol dipertahankan.

3. **Super Encryption**
   - Tahap 1: Caesar Cipher.
   - Tahap 2: Columnar Transposition.
   - Dekripsi dilakukan dengan urutan terbalik.

4. **Unit Test**
   - Pengujian Caesar.
   - Pengujian transposisi berbagai panjang teks.
   - Pengujian kunci dengan huruf berulang.
   - Pengujian Super Encryption.

## Struktur Proyek

```text
cipher-klasik-python/
├── .gitignore
├── README.md
├── main.py
├── ciphers/
│   ├── __init__.py
│   ├── caesar.py
│   ├── transposition.py
│   └── super_encryption.py
└── tests/
    ├── __init__.py
    └── test_ciphers.py
```

## Prasyarat

- Python 3.8 atau lebih baru.
- Tidak membutuhkan library eksternal.

Cek versi Python:

```bash
python --version
```

## Menjalankan Program

Masuk ke folder proyek:

```bash
cd cipher-klasik-python
```

Jalankan:

```bash
python main.py
```

## Menjalankan Pengujian

```bash
python -m unittest discover -s tests -v
```

Jika semua berhasil, setiap test akan berstatus `ok`.

## Contoh Caesar Cipher

Plaintext:

```text
Hello World!
```

Shift:

```text
3
```

Hasil:

```text
Khoor Zruog!
```

Dekripsi dengan shift 3 menghasilkan kembali:

```text
Hello World!
```

## Contoh Super Encryption

Input:

```text
Teks      : MENGANTUK
Shift     : 3
Kunci     : TOMBAK
```

Proses:

```text
MENGANTUK
    ↓
Caesar +3
    ↓
PHQJDQWXN
    ↓
Columnar Transposition
    ↓
Ciphertext
```

Ciphertext dapat berbeda jika kunci atau teks diubah. Gunakan menu **Dekripsi** dengan shift dan kunci yang sama untuk mengembalikan plaintext.

## Catatan Penting

Ini adalah implementasi **kriptografi klasik untuk pembelajaran**. Caesar Cipher dan transposisi kolom tidak cocok digunakan sebagai perlindungan data modern yang membutuhkan keamanan nyata.

## GitHub

```bash
git init
git add .
git commit -m "feat: lengkapkan aplikasi cipher klasik"
git branch -M main
git remote add origin https://github.com/USERNAME/cipher-klasik-python.git
git push -u origin main
```

Ganti `USERNAME` dengan username GitHub Anda.
