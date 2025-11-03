import socket
import threading

# ------------------------
# Server Code
# ------------------------
def handle_client(client_socket, client_address):
    print(f"[+] New connection from {client_address}")
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            print(f"[Client {client_address}] {msg}")
            # Echo the message back
            client_socket.sendall(f"Server received: {msg}".encode())
        except ConnectionResetError:
            break
    print(f"[-] Connection closed {client_address}")
    client_socket.close()

def start_server(host="127.0.0.1", port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[SERVER] Listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, client_address)
        )
        client_thread.start()


# ------------------------
# Client Code
# ------------------------
def start_client(server_host="127.0.0.1", server_port=5000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(f"[CLIENT] Connected to server {server_host}:{server_port}")

    try:
        while True:
            msg = input("Enter message (or 'quit' to exit): ")
            if msg.lower() == "quit":
                break
            client_socket.sendall(msg.encode())
            response = client_socket.recv(1024).decode()
            print(f"[SERVER RESPONSE] {response}")
    finally:
        client_socket.close()
        print("[CLIENT] Disconnected")


# ------------------------
# Run as server or client
# ------------------------
if _name_ == "_main_":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "server":
        start_server()
    else:
        start_client()