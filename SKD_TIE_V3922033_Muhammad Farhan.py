def vigenere_encrypt(plaintext, key):
    ciphertext = ""  # Inisialisasi string untuk menyimpan teks terenkripsi
    key = key.upper()  # Mengonversi kunci ke huruf besar untuk konsistensi
    
    key_len = len(key)  # Panjang kunci

    for i in range(len(plaintext)):
        char = plaintext[i]  # Mengambil karakter dari teks masukan
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf alfabet
            shift = ord(key[i % key_len]) - ord('A')  # Menghitung pergeseran berdasarkan karakter kunci
            if char.islower():  # Jika karakter adalah huruf kecil
                ciphertext += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))  # Enkripsi huruf kecil
            else:
                ciphertext += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))  # Enkripsi huruf besar
        else:
            ciphertext += char  # Jika karakter bukan huruf, biarkan seperti itu (misalnya, spasi atau tanda baca)
    
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""  # Inisialisasi string untuk menyimpan teks terdekripsi
    key = key.upper()  # Mengonversi kunci ke huruf besar untuk konsistensi
    
    key_len = len(key)  # Panjang kunci

    for i in range(len(ciphertext)):
        char = ciphertext[i]  # Mengambil karakter dari teks terenkripsi
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf alfabet
            shift = ord(key[i % key_len]) - ord('A')  # Menghitung pergeseran berdasarkan karakter kunci
            if char.islower():  # Jika karakter adalah huruf kecil
                plaintext += chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))  # Dekripsi huruf kecil
            else:
                plaintext += chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))  # Dekripsi huruf besar
        else:
            plaintext += char  # Jika karakter bukan huruf, biarkan seperti itu (misalnya, spasi atau tanda baca)
    
    return plaintext

# Contoh penggunaan
plaintext = "Muhammad Farhan"
key = "JAMBI"

encrypted_text = vigenere_encrypt(plaintext, key)
decrypted_text = vigenere_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Enkripsi:", encrypted_text)
print("Dekripsi:", decrypted_text)
