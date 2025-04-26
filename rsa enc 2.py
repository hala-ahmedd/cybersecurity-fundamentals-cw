import rsa  # For RSA encryption/decryption (asymmetric encryption)
from cryptography.fernet import Fernet  # For AES encryption/decryption (symmetric encryption)
import os  # For interacting with the operating system (file paths)
import zipfile  # For creating ZIP archives

# Step 1: Generate RSA Key Pair if not already present
def generate_rsa_keys():
    (public_key, private_key) = rsa.newkeys(2048)

    with open(r'C:/Users/Test 1/Desktop/code/public.pem', 'wb') as public_file:
        public_file.write(public_key.save_pkcs1())

    with open(r'C:/Users/Test 1/Desktop/code/private.pem', 'wb') as private_file:
        private_file.write(private_key.save_pkcs1())

    print("RSA key pair generated and saved as 'public.pem' and 'private.pem'.")

# Check if RSA keys already exist, if not generate them
if not os.path.exists(r'C:/Users/Test 1/Desktop/code/public.pem') or not os.path.exists(r'C:/Users/Test 1/Desktop/code/private.pem'):
    generate_rsa_keys()

# Step 2: Load RSA public and private keys
with open(r"C:/Users/Test 1/Desktop/code/public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open(r"C:/Users/Test 1/Desktop/code/private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Step 3: Generate AES encryption key
generated_key = Fernet.generate_key()

# Save the AES key
with open(r'C:/Users/Test 1/Desktop/code/key.bin', 'wb') as key_file:
    key_file.write(generated_key)
print("AES encryption key saved as 'key.bin'.")

# Step 4: Encrypt the AES key using RSA public key
def encrypt_aes_key(aes_key, rsa_public_key):
    encrypted_key = rsa.encrypt(aes_key, rsa_public_key)
    return encrypted_key

encrypted_aes_key = encrypt_aes_key(generated_key, public_key)

# Save the encrypted AES key
with open(r'C:/Users/Test 1/Desktop/code/encrypted_aes_key.bin', 'wb') as encrypted_key_file:
    encrypted_key_file.write(encrypted_aes_key)
print("RSA-encrypted AES key saved as 'encrypted_aes_key.bin'.")

# Step 5: Function to zip a folder
def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, os.path.dirname(folder_path))
                zipf.write(full_path, arcname)

# Step 6: Encrypt a file (the zip file) using AES key
def encrypt_file(filepath, aes_key):
    fernet = Fernet(aes_key)

    with open(filepath, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    encrypted_filepath = filepath + ".enc"
    with open(encrypted_filepath, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File '{filepath}' encrypted and saved as '{encrypted_filepath}'.")

    # Delete the original unencrypted ZIP file
    os.remove(filepath)
    print(f"Original file '{filepath}' deleted.")

# Step 7: Delete files inside the 'Confidential' folder for security
def delete_confidential_files(confidential_folder):
    if os.path.exists(confidential_folder):
        for root, dirs, files in os.walk(confidential_folder):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
        print(f"All files inside '{confidential_folder}' have been deleted.")
    else:
        print(f"Confidential folder '{confidential_folder}' does not exist.")

# Main block
if __name__ == "__main__":
    # Define your paths
    folder_to_zip = r"C:/Users/Test 1/Desktop/code/MMM"  # Folder you want to zip
    output_zip = r"C:/Users/Test 1/Desktop/code/mmm_backup.zip"  # Output zip file

    # Step 1: Create a zip of the specified folder
    zip_folder(folder_to_zip, output_zip)
    print("Folder zipped successfully!")

    # Step 2: Encrypt the zip file if it exists
    if os.path.exists(output_zip):
        print("ZIP file exists. Proceeding to encryption...")
        encrypt_file(output_zip, generated_key)
    else:
        print("ZIP file was not found. Check the path!")

    # Step 3: Delete confidential files
    confidential_folder = r"C:/Users/Test 1/Desktop/Confidential"
    delete_confidential_files(confidential_folder)