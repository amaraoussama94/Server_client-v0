# connect to th server via socket
import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.43.73'  # same ip of the server in server.py
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        # print(self.pos)

    def get_pos(self):
        return self.pos

    def connect(self):

        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()  # recev token and decode it
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(str(e))

# n= Network()#for testing
# print(n.send("hello"))
# print(n.send("workin"))

