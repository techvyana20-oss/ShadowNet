# 🔒 ShadowNet

ShadowNet is a Local Encrypted Onion Network Simulator built in Termux using Python.

⚠️ This project is for **educational purposes only**.

---

## 🚀 Features

- 🔐 End-to-end encrypted chat
- 🕶 Anonymous nicknames
- 🌐 Local network communication (WiFi/Hotspot)
- 🧠 Onion-network simulation concept
- 📱 Works in Termux (No root required)

---

## 🛠 Installation

```bash
pkg update
pkg install python git
pip install cryptography

▶️ Run Server
python server.py

▶️ Run Client
python client.py

🧠 How It Works

Client encrypts messages →
Server decrypts and rebroadcasts →
Other clients receive encrypted message.

⚠️ Disclaimer

This is NOT Tor.
This is NOT Dark Web.
This is NOT illegal software.

This project is purely educational to understand encryption and local networking.

---

🚀 How To Use
On Device 1:
python server.py


Copy:

Encryption key

IP address (run ip a)

On Device 2:
python client.py


Enter:

Server IP

Encryption key

Anonymous name

Start chatting 🔥
