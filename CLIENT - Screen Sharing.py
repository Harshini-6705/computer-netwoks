import socket
from PIL import ImageGrab
import io
import struct
import time

# Define server detacils
host = '192.168.194.15'  # Replace with the server's IP address if needed
port = 1357

# Set up socket connection to server
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to server successfully.")
except Exception as e:
    print(f"Connection failed: {e}")
    exit(1)

try:
    buffer = io.BytesIO()  # Create buffer once to reuse
    
    while True:
        # Capture the screen and resize for better performance
        screenshot = ImageGrab.grab().resize((1280, 720))  # Adjust resolution as needed
        
        # Compress the screenshot to JPEG format with reduced quality for smaller data size
        buffer.seek(0)
        screenshot.save(buffer, format="JPEG", quality=50)  # Lower quality reduces data size
        data = buffer.getvalue()

        # Send the length of the data first, then the data itself
        client_socket.sendall(struct.pack("I", len(data)) + data)
        
        # Control frame rate (15 fps for smoother experience)
        time.sleep(0.066)  # ~15 frames per second
except KeyboardInterrupt:
    print("Screen sharing stopped by user.")
except Exception as e:
    print("Error during screen capture:", e)
finally:
    client_socket.close()
