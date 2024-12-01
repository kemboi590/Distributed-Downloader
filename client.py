import socket

CHUNK_SIZE = 1024  # Size of each chunk to receive

def start_client(host='127.0.0.1', port=12345, output_file="downloaded_file.txt"):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"[CONNECTED] Connected to the server.")

    with open(output_file, 'wb') as file:
        while True:
            chunk = client.recv(CHUNK_SIZE)
            if not chunk:
                break
            file.write(chunk)
    print(f"[DONE] File downloaded and saved as {output_file}.")
    client.close()

if __name__ == "__main__":
    output_file_name = "downloaded_file.txt"  
    start_client(output_file=output_file_name)
