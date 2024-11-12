import pyautogui as pg
import socket



client = socket.gethostbyname(socket.gethostname())
host = input('Server Host: ')  
port = int(input('Server Port: '))
client_socket = socket.socket()  
client_socket.connect((host, port))  

message = 'done'
while True:
    try:
        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())  
            data = client_socket.recv(1024).decode()
            if data == 'click':
                pg.click(x, y)
                print("After click")
            elif data == 'del':
                pg.typewrite(['backspace'])
                print("After backspace")
            elif data.startswith('cde:'):
                pg.write(data.replace('cde:', ''))
                print("After type text")
            elif data=='rclick':
                pg.click(button='right')
                print("After right click")
            elif data=='dclick':
                pg.click(clicks=2)
                print("After double click")
            elif data=='nl':
                pg.typewrite(['enter'])
                print("After enter")
            else:
                x = int(data.split(' ')[0])
                y = int(data.split(' ')[1])
                pg.moveTo(x, y)  
            message = 'done' 
        client_socket.close()  
    except:
        pass
