import sys
from ciphers import CaesarCipher, TranspositionCipher, SuperEncryption


def print_header():
    print("=" * 64)
    print("          PROGRAM CIPHER KLASIK - PYTHON CLI")
    print("=" * 64)


def pause():
    input("\nTekan ENTER untuk kembali ke menu...")


def get_action_choice():
    print("\nPilih Aksi:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    return input("Masukkan pilihan (1/2): ").strip()


def get_shift():
    while True:
        value = input("Masukkan nilai Shift (integer): ").strip()
        try:
            return int(value)
        except ValueError:
            print("❌ Shift harus berupa angka integer.")


def handle_caesar():
    action = get_action_choice()
    if action not in {"1", "2"}:
        print("❌ Pilihan aksi tidak valid.")
        return

    text = input("Masukkan teks: ")
    shift = get_shift()

    result = (
        CaesarCipher.encrypt(text, shift)
        if action == "1"
        else CaesarCipher.decrypt(text, shift)
    )
    print(f"\n{'Enkripsi' if action == '1' else 'Dekripsi'}: {result}")


def handle_transposition():
    action = get_action_choice()
    if action not in {"1", "2"}:
        print("❌ Pilihan aksi tidak valid.")
        return

    text = input("Masukkan teks: ")
    key = input("Masukkan kata kunci: ")

    try:
        result = (
            TranspositionCipher.encrypt(text, key)
            if action == "1"
            else TranspositionCipher.decrypt(text, key)
        )
        print(f"\n{'Enkripsi' if action == '1' else 'Dekripsi'}: {result}")
    except (ValueError, TypeError) as exc:
        print(f"❌ Error: {exc}")


def handle_super_encryption():
    action = get_action_choice()
    if action not in {"1", "2"}:
        print("❌ Pilihan aksi tidak valid.")
        return

    text = input("Masukkan teks: ")
    shift = get_shift()
    key = input("Masukkan kata kunci transposisi: ")

    try:
        result = (
            SuperEncryption.encrypt(text, shift, key)
            if action == "1"
            else SuperEncryption.decrypt(text, shift, key)
        )
        print(
            f"\n{'Super Enkripsi' if action == '1' else 'Super Dekripsi'}: {result}"
        )
    except (ValueError, TypeError) as exc:
        print(f"❌ Error: {exc}")


def main():
    print_header()

    handlers = {
        "1": handle_caesar,
        "2": handle_transposition,
        "3": handle_super_encryption,
    }

    while True:
        print("\nPilih Algoritma Kriptografi:")
        print("1. Caesar Cipher")
        print("2. Columnar Transposition Cipher")
        print("3. Super Encryption (Caesar + Transposition)")
        print("0. Keluar")
        print("-" * 64)

        choice = input("Masukkan pilihan menu (0-3): ").strip()

        if choice == "0":
            print("\nTerima kasih telah menggunakan program.")
            sys.exit(0)

        handler = handlers.get(choice)
        if handler:
            handler()
            pause()
        else:
            print("❌ Pilihan menu tidak valid.")


if __name__ == "__main__":
    main()
