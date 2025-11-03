CHAT CLIENT SERVER USING UDP
chat_server.py
import socket

def chat_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Chat Server running on {host}:{port}")

    clients = set()
    while True:
        msg, addr = server_socket.recvfrom(1024)
        clients.add(addr)
        print(f"Received '{msg.decode()}' from {addr}")

        # Send message to all clients except sender
        for client in clients:
            if client != addr:
                server_socket.sendto(msg, client)

if __name__ == "__main__":
    chat_server()

chat_client.py
import socket
import threading

def chat_client(server_host='127.0.0.1', server_port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(2)

    def receive():
        while True:
            try:
                msg, _ = client_socket.recvfrom(1024)
                print("\n[CHAT] " + msg.decode())
            except:
                break

    threading.Thread(target=receive, daemon=True).start()

    print("You can now chat! Type messages and press Enter.")
    while True:
        msg = input()
        if not msg:
            break
        client_socket.sendto(msg.encode(), (server_host, server_port))

if __name__ == "__main__":
    chat_client()
