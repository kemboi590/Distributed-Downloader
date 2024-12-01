import socket
import threading
import os

CHUNK_SIZE = 1024  

# Function to handle client requests
def handle_client(client_socket, client_address, file_path):
    print(f"[NEW CONNECTION] {client_address} connected.")
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(CHUNK_SIZE):
                client_socket.send(chunk)
        print(f"[DONE] File sent to {client_address}.")
    except FileNotFoundError:
        print(f"[ERROR] File not found!")
        client_socket.send(b"ERROR: File not found")
    finally:
        client_socket.close()

def start_server(host='127.0.0.1', port=12345, file_path="./files/ilovepython.txt"):
    if not os.path.exists(file_path):
        print(f"[ERROR] File {file_path} does not exist.")
        return

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[LISTENING] Server is listening on {host}:{port}")

    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address, file_path))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    file_name = "./files/ilovepython.txt"
    start_server(file_path=file_name)
