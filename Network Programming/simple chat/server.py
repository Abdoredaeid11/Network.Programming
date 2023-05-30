import socket
from socket import *
#from socket import AF_INET, socket, SOCK_STREAM,SO_REUSEADDR
try:
    s = socket(AF_INET,SOCK_STREAM) 
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    host = "127.0.0.1"
    port = 5000

    s.bind((host,port))
    s.listen(5)
    # while True : 
    #     c, add = s.accept()
    #     print("Connection from :",add[0])
    #     x = c.recv(500)
    #     print(x)
    c, add = s.accept()
    print("Connection from :",add[0])
    while True : 
        x = c.recv(2048)
        print( 'Client: ',x.decode('utf-8'))
        c.send(input('Server:').encode('utf-8'))
    s.close()
except error as e:
    print(e)
except KeyboardInterrupt:
    print("chat is finished")    