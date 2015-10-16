import socket

s = socket.socket()         # Create a socket object
host = '192.168.1.112'  # Get local machine name
port = 12345     
s.bind((host, port))

s.listen(5)               # Now wait for client connection.
while True:
 c, addr = s.accept() 
 print ('Got connection from',addr)
 c.send('Thank you for connecting')
 c.close()


