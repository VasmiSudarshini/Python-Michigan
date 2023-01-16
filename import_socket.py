import socket

#creating a socket and connecting
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) 
#send the request
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

#receive the data
while True:
    data = mysock.recv(512) #512 is the number of characters to be received
    if len(data) < 1:
        break
    print(data.decode(),end='')

#closing the socket
mysock.close()