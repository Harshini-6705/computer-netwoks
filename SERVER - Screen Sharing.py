import socket
import cv2
import numpy as np
import struct
import threading

# Define server details
host = socket.gethostbyname(socket.gethostname())
port = 65432

# Function to receive and display frames
def receive_frames(conn):
    while True:
        try:
            # Receive the size of the image data
            data_size = struct.unpack("I", conn.recv(4))[0]

            # Receive the image data based on the given size
            data = b""
            while len(data) < data_size:
                packet = conn.recv(4096)
                if not packet:
                    break
                data += packet

            # Convert the data to an image format
            img_array = np.frombuffer(data, dtype=np.uint8)
            frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            # Display the image
            if frame is not None:
                cv2.imshow("Client Screen", frame)
                if cv2.waitKey(1) == ord('q'):  # Press 'q' to exit
                    break
        except Exception as e:
            print("Error during frame reception:", e)
            break

    conn.close()
    cv2.destroyAllWindows()

# Set up socket to listen for client connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Server is listening on {host}:{port}")

# Accept the client connection
conn, address = server_socket.accept()
print("Connection from:", address)

# Start a thread to receive and display frames
receive_thread = threading.Thread(target=receive_frames, args=(conn,))
receive_thread.start()
