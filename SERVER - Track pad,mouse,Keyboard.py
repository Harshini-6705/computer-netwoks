import socket 
import tkinter as tk 
from tkinter.messagebox import showinfo 
from random import randint 

def type_box():
    tp_fr = tk.Tk()
    tp_fr.title('Python Remote Keyboard')
    bx_txt = tk.Entry(tp_fr, width=100)
    bx_txt.pack()
    send_but =tk.Button(tp_fr, text="Type Text", command=lambda:conn.send(('cde:'+bx_txt.get()).encode()))
    del_but =tk.Button(tp_fr, text="Delete", command=lambda:conn.send(('del'.encode())))
    nl_but =tk.Button(tp_fr, text="Enter", command=lambda:conn.send(('nl'.encode())))
    del_but.pack()
    send_but.pack()
    nl_but.pack()
    tp_fr.mainloop()


k = tk.Tk()
root = tk.Tk()
root.title('Python Remote Trackpad')
root.geometry('960x540')
global x, y, data
host = socket.gethostbyname(socket.gethostname())
port = randint(1000, 10000)
print('Server host and port no:')
print(host)
print(port)
server_socket = socket.socket()
print("Ater socket creation")
server_socket.bind(('', port))
print("After bind")
server_socket.listen(60)
print("After listen")
conn,address = server_socket.accept()
print("After accept")
print("Connection from: " + str(address))
x = 10
y = 10

def motion(event):
    x, y = event.x, event.y
    data = conn.recv(1024).decode()
    data = str(x*4)+' '+str(y*4)
    conn.send(data.encode())

root.bind('<Motion>', motion)
cde = ''

def a(o):
    conn.send('click'.encode())
    print("After Left Click")

def r(o):
    conn.send('rclick'.encode())
    print("After Right Click")

def d(o):
    conn.send('dclick'.encode())
    print("After Double Click")

root.bind('<Control-l>', a)
print("After bind control-l")                                                                           
root.bind('<Control-r>', r)
print("After bind control-r")
root.bind('<Control-d>', d)
print("After bind control-d")
menubar = tk.Menu(root)
menubar.add_command(label="Type", command=type_box)
root.config(menu = menubar)
root.mainloop()
