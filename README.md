TOPIC:
This project was done using different scripts that were combined together at the end in the main.py script; it stimulates the process of an actual ransomware using an isolated enviroment: Virtual machine (in this case, windows vm). 
STEPS: 
1. The malware gets sent to the Victim's machine through links, ads or phishing emails.
2. After accessing the link, the malware will start by collecting specific file extensions.
3. After collecting them, the malware will proceed to encrypt them using AES. (For a higher secruity rate, RSA was used to encrypt the AES key.)
4. The malware then sends the chosen files to the attacker's email and deletes the original files from the victim's machine.
5. The process of obfuscation takes place to avoid reverse engineering.
6. Victim gets sent a ransom.
