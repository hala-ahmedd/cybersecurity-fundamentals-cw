from cryptography.fernet import Fernet
import os

def decrypt_file(encrypted_filepath, aes_key_path):
    if not os.path.exists(encrypted_filepath):
        print(f"Error: Encrypted file '{encrypted_filepath}' not found.")
        return
    if not os.path.exists(aes_key_path):
        print(f"Error: AES key file '{aes_key_path}' not found.")
        return

    with open(aes_key_path, 'rb') as key_file:
        aes_key = key_file.read()

    fernet = Fernet(aes_key)

    with open(encrypted_filepath, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception as e:
        print("Error during decryption:", e)
        return

    decrypted_filepath = encrypted_filepath.replace('.enc', '_decrypted.zip')
    with open(decrypted_filepath, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"Decryption successful! Decrypted file saved as '{decrypted_filepath}'.")

if __name__ == "__main__":
    encrypted_file = r"C:/Users/Test 1/Desktop/code/mmm_backup.zip.enc"
    aes_key_file = r"C:/Users/Test 1/Desktop/code/key.bin"

    decrypt_file(encrypted_file, aes_key_file)
