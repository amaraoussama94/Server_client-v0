# Server
# windows test
import socket
from _thread import *
import sys

# via cmd -> ipconfig ->IPV4
server = '192.168.43.73'  # "IP" you wil gett an error: use 'IP'
port = 5555  # open port

pos = [(0, 0), (255, 255)]  # stored n stack


def read_pos(str):  # conv str pos to int pos for client
    str = str.split(",")
    return int(str[0]), int(str[1])  # tup


def make_pos(tup):  # conv int pos to str pos for sever
    return str(tup[0]) + "," + str(tup[1])  # tup


def threaded_client(conn, player):
    # conn.send(str.encode("connected"))#validation token
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())  # size of  data to recive 2MB in b
            # reply=data.decode("utf-8")
            pos[player] = data  # update player position in the server

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]  # player 0 position
                else:
                    reply = pos[1]  # player 1 position
                print("Received  ", data)
                print("Sending  ", reply)
            conn.sendall(str.encode(make_pos(reply)))  # encode data and send it
        except:
            break
    print("Lost connection")
    conn.close


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # type of  connection

try:

    serversocket.bind((server, port))

except  socket.error as e:
    print(str(e))

# max_conn =2
serversocket.listen(2)  # open the port 2 pp  only can connect to the port
print("waiting for connection , Server Sttarted")
current_player = 0
while True:
    (conn, addr) = serversocket.accept()  # accept any connection and sotre the connection and IP adress
    print("connected to :  ", addr)
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
    print("current_player :  ",current_player)




