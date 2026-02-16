# ==========================================
# ShadowNet Server
# Local Encrypted Onion Network Simulator
# ==========================================

import socket
import threading
from cryptography.fernet import Fernet
import random
import string

HOST = "0.0.0.0"
PORT = 5000

clients = []

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Generate hidden address simulation
hidden_address = ''.join(random.choices(string.ascii_lowercase, k=12)) + ".local"

print("\n🔒 ShadowNet Server Started")
print(f"🌐 Hidden Address: {hidden_address}")
print(f"🔑 Encryption Key: {key.decode()}")
print(f"📡 Listening on port {PORT}\n")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()


def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)


def handle_client(conn, addr):
    print(f"⚡ New connection from {addr}")
    clients.append(conn)

    while True:
        try:
            encrypted_message = conn.recv(1024)
            if not encrypted_message:
                break

            decrypted_message = cipher.decrypt(encrypted_message).decode()
            print(f"💬 {decrypted_message}")

            broadcast(encrypted_message, conn)

        except:
            break

    print(f"❌ Connection closed: {addr}")
    clients.remove(conn)
    conn.close()


while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
