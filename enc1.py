from cryptography.fernet import Fernet
import os
from collecting_files import file_collection,print_files
# Step 1: Generate the AES encryption key (Fernet) and save it in key.bin
generated_key = Fernet.generate_key()  # Generate the AES key
with open("key.bin", "wb") as key_file:
    key_file.write(generated_key)  # Store the key in a secure file
print("AES encryption key saved as 'key.bin'.")

# Step 2: Encrypt the file
def encrypt_file(filename, generated_key):
    # Create the encryption object
    fernet = Fernet(generated_key)

    # Read the file as binary
    with open(filename, "rb") as file:
        file_data = file.read()

    # Encrypt the data
    encrypted_data = fernet.encrypt(file_data)

    # Write the encrypted file
    encrypted_filename = filename + ".enc"
    with open(encrypted_filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    print(f"File '{filename}' encrypted and saved as '{encrypted_filename}'.")
    
    # Delete the original file
    os.remove(filename)
    print(f"Original file '{filename}' deleted.")

# User Input for File to Encrypt
if __name__ == "__main__":
    filename = r"c:/Users/Test 1/Desktop/code/files.log"  # Ask user for file path
    encrypt_file(filename, generated_key)  # Encrypt the file and delete the original