import socket
import threading
import numpy as np


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
listW = []
listB = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            if(msg == DISCONNECT_MSG):
                connected = False
            else:
            parse_msg(msg)
            if(msg == "end"):
                conn.send(calculte_avg_W_B().encode(FORMAT))
            conn.send("Msg Recieved".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr) )
        thread.start()
        print("hi")
        print(f"[ACTIVE CONNECTIONS] { threading.active_count()-1}")
        print("hi")

def parse_msg(msg):
    if(("start" in msg)):
        listW.clear
        listB.clear
        msg = msg.replace("strart:", "")
    b_idx = msg.find("B")
    w_idx = msg.find("W")
    weigths = msg[w_idx+1: b_idx]
    bias = msg[b_idx+1:]
    listW.append(np.fromstring(weigths, sep = ",") )
    listB.append(float(bias))
    print(listW)
    print(listB)

def calculte_avg_W_B():
    sumW = np.zeros(listW[0].shape)
    count = 0
    for w in listW:
        sumW = sumW+w
        count = count +1
    avgW = sumW/count
    print(avgW)

    sumB = 0
    count = 0
    for b in listB:
      sumB = sumB+b
      count = count +1
    avgB = sumB/count
    print(avgB)

    return avgW.tostring() + " " + str(avgB)


print("[STARTING] server is starting... ")
start()
# parse_msg("start:W10,1030,490.9,690.9,10,30,B10007")
# parse_msg("W110,1030,900.9,5.3,10,49,B10007.9")
# calculte_avg_W_B()
