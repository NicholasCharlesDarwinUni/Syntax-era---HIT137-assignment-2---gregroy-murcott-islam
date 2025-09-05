import os

# ---- helpers ---------------------------------------------------------------
def classify(ch):
    if 'a' <= ch <= 'z':
        return 'la' if ch <= 'm' else 'lz'
    if 'A' <= ch <= 'Z':
        return 'ua' if ch <= 'M' else 'uz'
    return None

def enc_char(ch, s1, s2):
    cls = classify(ch)
    if cls == 'la':
        k = (s1 * s2) % 26
        return chr((ord(ch) - 97 + k) % 26 + 97)
    if cls == 'lz':
        k = (s1 + s2) % 26
        return chr((ord(ch) - 97 - k) % 26 + 97)
    if cls == 'ua':
        k = s1 % 26
        return chr((ord(ch) - 65 - k) % 26 + 65)
    if cls == 'uz':
        k = (s2 * s2) % 26
        return chr((ord(ch) - 65 + k) % 26 + 65)
    return ch

def dec_char(ch, cls, s1, s2):
    if cls == 'la':
        k = (s1 * s2) % 26
        return chr((ord(ch) - 97 - k) % 26 + 97)
    if cls == 'lz':
        k = (s1 + s2) % 26
        return chr((ord(ch) - 97 + k) % 26 + 97)
    if cls == 'ua':
        k = s1 % 26
        return chr((ord(ch) - 65 + k) % 26 + 65)
    if cls == 'uz':
        k = (s2 * s2) % 26
        return chr((ord(ch) - 65 - k) % 26 + 65)
    return ch

# ---- file I/O --------------------------------------------------------------
def encrypt_file(raw_file, enc_file, flag_file, s1, s2):
    with open(raw_file, "r", encoding="utf-8") as fin, \
         open(enc_file, "w", encoding="utf-8") as fout, \
         open(flag_file, "w", encoding="utf-8") as fflag:
        src = fin.read()
        out_chars = []
        flags = []
        for ch in src:
            cls = classify(ch)
            out_chars.append(enc_char(ch, s1, s2))
            flags.append(cls if cls else '.')  # '.' for non-letters
        fout.write("".join(out_chars))
        fflag.write("|".join(flags))

def decrypt_file(enc_file, flag_file, dec_file, s1, s2):
    with open(enc_file, "r", encoding="utf-8") as fin, \
         open(flag_file, "r", encoding="utf-8") as fflag, \
         open(dec_file, "w", encoding="utf-8") as fout:
        enc = fin.read()
        flags = fflag.read().split("|")
        if len(flags) != len(enc):
            raise ValueError("Flag file length does not match encrypted text length.")
        out = []
        for ch, cls in zip(enc, flags):
            cls = None if cls == '.' else cls
            out.append(dec_char(ch, cls, s1, s2))
        decrypted_text = "".join(out)
        fout.write(decrypted_text)
        return decrypted_text

def verify_files(original_file, decrypted_text):
    with open(original_file, "r", encoding="utf-8") as f:
        original_text = f.read()
    if original_text == decrypted_text:
        print("Decryption successful! Files match.")
    else:
        print("Decryption failed! Wrong shift values or corrupted files.")
        # Optional: show first mismatch
        for i, (x, y) in enumerate(zip(original_text, decrypted_text)):
            if x != y:
                print(f"First mismatch at position {i}: original='{x}' decrypted='{y}'")
                break
        if len(original_text) != len(decrypted_text):
            print(f"Length mismatch: original={len(original_text)} decrypted={len(decrypted_text)}")

# ---- main ------------------------------------------------------------------
if __name__ == "__main__":
    base = "/Users/hi/Desktop"  # change as needed
    raw_path = os.path.join(base, "raw_text.txt")
    enc_path = os.path.join(base, "encrypted_text.txt")
    dec_path = os.path.join(base, "decrypted_text.txt")
    flag_path = os.path.join(base, "encrypted_flags.txt")

    # robust numeric input
    while True:
        try:
            shift1 = int(input("Enter shift1 (number): "))
            shift2 = int(input("Enter shift2 (number): "))
            break
        except ValueError:
            print("Please enter whole numbers (e.g., 2 and 7). Try again.")

    # encrypt, decrypt, and verify
    encrypt_file(raw_path, enc_path, flag_path, shift1, shift2)
    decrypted_text = decrypt_file(enc_path, flag_path, dec_path, shift1, shift2)
    verify_files(raw_path, decrypted_text)
