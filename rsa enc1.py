import rsa  # For RSA encryption/decryption (asymmetric encryption)
from cryptography.fernet import Fernet  # For AES encryption/decryption using Fernet (symmetric encryption)
import os  # For interacting with the operating system (file paths)

# Step 1: Generate RSA Key Pair if not already present
def generate_rsa_keys():
    # Generate a new RSA key pair (public and private)
    (public_key, private_key) = rsa.newkeys(2048)

    # Save the RSA keys to files using absolute paths
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

# Step 3: Generate AES encryption key using Fernet
generated_key = Fernet.generate_key()

# Save the AES key using an absolute path
with open(r'C:/Users/Test 1/Desktop/code/key.bin', 'wb') as key_file:
    key_file.write(generated_key)
print("AES encryption key saved as 'key.bin'.")

# Step 4: Encrypt the AES key using the RSA public key
def encrypt_aes_key(aes_key, rsa_public_key):
    encrypted_key = rsa.encrypt(aes_key, rsa_public_key)  # RSA encryption of the AES key
    return encrypted_key

encrypted_aes_key = encrypt_aes_key(generated_key, public_key)

# Save the encrypted AES key using an absolute path
with open(r'C:/Users/Test 1/Desktop/code/encrypted_aes_key.bin', 'wb') as encrypted_key_file:
    encrypted_key_file.write(encrypted_aes_key)
print("RSA-encrypted AES key saved as 'encrypted_aes_key.bin'.")

# Step 5: Encrypt the file using AES (Fernet)
def encrypt_file(filepath, aes_key):
    fernet = Fernet(aes_key)  # Create a Fernet object with the AES key

    with open(filepath, "rb") as file:
        file_data = file.read()

    # Encrypt the file data using the AES key
    encrypted_data = fernet.encrypt(file_data)

    # Save the encrypted file with a .enc extension
    encrypted_filepath = filepath + ".enc"
    with open(encrypted_filepath, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File '{filepath}' encrypted and saved as '{encrypted_filepath}'.")

    # Delete the original unencrypted file
    os.remove(filepath)
    print(f"Original file '{filepath}' deleted.")

# Main block
if __name__ == "__main__":
    # Specify the path of the file you want to encrypt
    filepath = r"C:/Users/Test 1/Desktop/code/files.log"
    
    # Encrypt the file using the generated AES key
    encrypt_file(filepath, generated_key)  # Calls the function to encrypt the file