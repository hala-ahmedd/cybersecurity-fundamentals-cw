# Import the required modules
from cryptography.fernet import Fernet  # For AES encryption/decryption using Fernet (symmetric encryption)
import os  # For interacting with the operating system (file paths, walking directories)
import zipfile  # For creating ZIP archives
from collecting_files import file_collection, print_files  

# Step 1: Function to zip a folder
def zip_folder(folder_path, output_path):
    # Create a ZIP file in write mode using deflated compression
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through all directories and files in the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)  # Absolute file path
                arcname = os.path.relpath(full_path, os.path.dirname(folder_path))  # Relative path to preserve structure
                zipf.write(full_path, arcname)  # Add the file to the ZIP archive

# Step 2: Generate AES encryption key using Fernet and save it to a file
generated_key = Fernet.generate_key()
with open("key.bin", "wb") as key_file:
    key_file.write(generated_key)  # Save the generated key to a binary file
print("AES encryption key saved as 'key.bin'.")

# Step 3: Define paths for folder to be zipped and the output ZIP file
folder_to_zip = r"C:\Users\Test 1\Desktop\code\MMM"
output_zip = r"C:\Users\Test 1\Desktop\code\mmm_backup.zip"

# Step 4: Define a function to encrypt the ZIP file using the generated key
def encrypt_file(filepath, generated_key):
    fernet = Fernet(generated_key)  # Create a Fernet object with the key

    # Read original ZIP file as binary
    with open(filepath, "rb") as file:
        file_data = file.read()

    # Encrypt the file data
    encrypted_data = fernet.encrypt(file_data)

    # Save the encrypted data to a new file with .enc extension
    encrypted_filepath = filepath + ".enc"
    with open(encrypted_filepath, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File '{filepath}' encrypted and saved as '{encrypted_filepath}'.")

    # Delete the original unencrypted ZIP file
    os.remove(filepath)
    print(f"Original file '{filepath}' deleted.")

# Main block to execute zipping, encryption, and cleanup
if __name__ == "__main__":
    # Create a ZIP of the specified folder
    zip_folder(folder_to_zip, output_zip)
    print("mmm folder zipped successfully!")

    # Check if ZIP file exists before proceeding
    zip_path = r"c:/Users/Test 1/Desktop/code/mmm_backup.zip"
    if os.path.exists(zip_path):
        print("ZIP file exists. Proceeding to encryption...")
        encrypt_file(zip_path, generated_key)  # Encrypt the ZIP file
    else:
        print("ZIP file was not found. Check the path!")

    # Step 5: Delete all files inside the 'Confidential' folder for security
    confidential_folder = r"C:/Users/Test 1/Desktop/Confidential"

    # Walk through the folder and remove each file
    for root, dirs, files in os.walk(confidential_folder):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

    print(f"All files inside '{confidential_folder}' have been deleted.")
