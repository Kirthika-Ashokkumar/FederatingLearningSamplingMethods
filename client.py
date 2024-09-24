import socket

class client:
    def __init__(self):
        self.HEADER = 64
        self.PORT = 5050
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MSG = "!DISCONNECT"
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(self.ADDR)
        
    def send(self, msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER-len(send_length))
        # print("sending: |", send_length.decode(self.FORMAT), "|")
        # print("sending: |", message.decode(self.FORMAT), "|")
        client.send(send_length)
        client.send(message)
        print(client.recv(2048).decode(self.FORMAT))
    
    def discconnect(self):
        self.send(self.DISCONNECT_MSG)
