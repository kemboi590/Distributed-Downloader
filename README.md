# Simple Distributed System (Class Assignmetnt 2024)

This project demonstrates a simple distributed system with a server and a client. The server sends a file to the client upon request.

## Files

- `server.py`: Contains the server code.
- `client.py`: Contains the client code.

## Requirements

- Python 3.x

## Usage

### Server

1. Navigate to the directory containing `server.py`.
2. Run the server:
    ```sh
    python server.py
    ```
3. The server will start and listen for incoming connections on `127.0.0.1:12345`.

### Client

1. Navigate to the directory containing `client.py`.
2. Run the client:
    ```sh
    python client.py
    ```
3. The client will connect to the server and download the file, saving it as `downloaded_file.txt`.

## Configuration

- The server sends the file located at `./files/ilovepython.txt` by default. You can change the file path by modifying the `file_path` parameter in `start_server`.
- The client saves the downloaded file as `downloaded_file.txt` by default. You can change the output file name by modifying the `output_file` parameter in `start_client`.

## How It Works

- The server listens for incoming connections.
- When a client connects, the server sends the specified file in chunks.
- The client receives the file in chunks and writes it to the specified output file.

## License

This project is licensed under the MIT License.
