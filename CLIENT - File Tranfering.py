import socket
import pyautogui
import threading
import os
from PIL import ImageGrab,Image
import time
import io

SERVER_IP = '192.168.194.15'
PORT = 5555
BUFFER_SIZE = 1024

# Function to send a file to the server
def send_file(client_socket, file_path):
    command = f"SEND_FILE:{os.path.basename(file_path)}"
    client_socket.send(command.encode())
    
    file_size = os.path.getsize(file_path)
    client_socket.send(str(file_size).encode())
    
    with open(file_path, 'rb') as f:
        file_data = f.read()
        client_socket.sendall(file_data)

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))
    # Send a file
    send_file(client_socket, r"C:\Users\USER\OneDrive\Desktop\wow.txt")
   

start_client()
