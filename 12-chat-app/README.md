# 💬 Chat Application (Socket-Based)

## 🧩 Project Overview
The **Chat Application** is a Python-based real-time messaging program that enables users to **communicate with each other over a local network**.  
It’s built using **socket programming** and **multithreading**, allowing multiple clients to connect to a server and exchange messages simultaneously.

This project demonstrates the fundamental concepts behind real-time chat platforms like WhatsApp, Discord, or Slack — on a smaller, local scale.

---

## 🚀 Features
- 🌐 **Real-Time Messaging:** Instant communication between connected clients.  
- 🧠 **Multithreaded Architecture:** Server handles multiple users at once.  
- 👥 **Nicknames:** Each client joins with a chosen username.  
- 📢 **Broadcast System:** All messages are shared with every connected client.  
- ⚠️ **Connection Management:** Automatically removes disconnected clients.  
- 🧹 **Lightweight Design:** Pure Python, no external dependencies required.

---

## 🛠️ Technologies Used
- **Python 3** — Core language  
- **socket** — For establishing network connections  
- **threading** — For managing simultaneous message sending and receiving  

---

🧠 How It Works

Server (server.py):

Listens for incoming connections on a specific port (default 55555).

Maintains lists of active clients and their nicknames.

Uses threads to handle multiple clients simultaneously.

Broadcasts any received message to all connected clients.

Client (client.py):

Connects to the server using sockets.

Sends nickname upon joining.

Runs two threads:

One for receiving messages (receive())

One for sending messages (write())

Communication Flow:

The client sends a message → The server receives it → The server broadcasts it to all connected clients.