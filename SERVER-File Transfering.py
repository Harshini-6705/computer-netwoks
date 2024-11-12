import socket
import os

# Server IP and port
SERVER_IP = '0.0.0.0'
PORT = 5555
BUFFER_SIZE = 1024

# Function to handle file reception from the client
def handle_client(client_socket):
    try:
        # Receive the command (e.g., SEND_FILE)
        command = client_socket.recv(BUFFER_SIZE).decode()
        if command.startswith("SEND_FILE:"):
            # Extract the file name
            file_name = command.split(":")[1]
            print(f"Preparing to receive file: {file_name}")

            # Receive the file size
            file_size = int(client_socket.recv(BUFFER_SIZE).decode())
            print(f"Expected file size: {file_size} bytes")

            # Receive the file data
            received_size = 0
            with open(file_name, "wb") as f:
                while received_size < file_size:
                    data = client_socket.recv(BUFFER_SIZE)
                    f.write(data)
                    received_size += len(data)
                    print(f"Received {received_size}/{file_size} bytes")

            print(f"File {file_name} received successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

# Start the server to listen for incoming connections
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, PORT))
    server_socket.listen(5)
    print("Server listening for incoming connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        # Handle file reception in a separate thread
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.daemon = True
        client_thread.start()

start_server()
