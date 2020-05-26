import socket
import _thread
#from _thread import *

def handle_connection(conn, addr):
    print("New connection added")
    conn.send("You are now connected to The Great Sarandeep's Server")
    msg = conn.recv(1024)
    print("Client", addr, "says", msg)
#TODO: handle connection here


#TODO: think of address
HOSTADD = "0.0.0.0"
PORT = 9090
MAXCLIENTS=5

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created succesfully")
except:
    print("Unable to create a socket")
    exit(0)
try:
    s.bind((HOSTADD, PORT))
    s.listen(MAXCLIENTS)     #kitne clients connect kar sakte h. abhi ke liye 5 hai.
    print("Binded Succesfully")
except:
    print("Unable to bind")
    exit(0)

#create thread here when accepted.
for i in range(MAXCLIENTS):
    conn, addr = s.accept()
    _thread.start_new_thread(handle_connection, (conn, addr, ))

s.close()