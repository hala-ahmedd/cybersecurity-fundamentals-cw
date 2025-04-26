import os
import base64
import sys
import winreg as reg
a = []
def b(d):
    for r, d2, fs in os.walk(d):
        for f in fs:
            if f.endswith(('.txt', '.jpg', '.docx')):
                fullnew = os.path.join(r, f)
                a.append(fullnew)
    return a
def c(e):
    log_path = base64.b64decode(b'QzpcVXNlcnNcVGVzdCAxXERlc3ktd29ya2luZyBjaGFsbGVuZ2U=').decode()
    with open(os.path.join(log_path, "files.log"), 'w') as f:
        for i in e:
            f.write(i + "\n")
    os.system(f'start "" "{log_path}"')
    return log_path
def add_persistence():
    key = reg.HKEY_CURRENT_USER
    subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
    value_name = "ScriptPersistence"
    script_path = sys.argv[0]
    reg.CreateKey(key, subkey)
    registry_key = reg.OpenKey(key, subkey, 0, reg.KEY_WRITE)
    reg.SetValueEx(registry_key, value_name, 0, reg.REG_SZ, script_path)
    reg.CloseKey(registry_key)
    print("Persistence mechanism added to Windows registry.")
if __name__ == "__main__":
    user_prompt = base64.b64decode(b'UGxlYXNlIGVudGVyIHlvdXIgZGlyZWN0b3J5J3MgUGF0aDog').decode()
    path = input(user_prompt)
    e = b(path)
    print(e)
    c(e)
    add_persistence()

