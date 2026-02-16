# ==========================================
# ShadowNet Client
# Connect to Local Encrypted Server
# ==========================================

import socket
import threading
from cryptography.fernet import Fernet

HOST = input("🌐 Enter Server IP: ")
PORT = 5000
key_input = input("🔑 Enter Encryption Key: ").encode()

cipher = Fernet(key_input)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
except:
    print("❌ Unable to connect to server.")
    exit()

nickname = input("🕶 Enter Anonymous Name: ")

print("\n✅ Connected to ShadowNet\n")


def receive():
    while True:
        try:
            encrypted_message = client.recv(1024)
            if not encrypted_message:
                break

            message = cipher.decrypt(encrypted_message).decode()
            print(message)

        except:
            print("❌ Connection lost.")
            break


def send():
    while True:
        message = input("")
        full_message = f"{nickname}: {message}"
        encrypted = cipher.encrypt(full_message.encode())
        client.send(encrypted)


receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
