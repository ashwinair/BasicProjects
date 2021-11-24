import socket
port = 3000
bufferSize =  65535
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create a socket object
# AF_INET is family of ipv4 ip address
# SOCK_DGRAM means UDP & SOCK_STREAM is TCP

hostname = "127.0.0.1"  # ip address for all local machine
# ephemeral ports
# Os will bind the port automatically for us

while True:
    s.connect((hostname, port))
    msg = input("Type: ")
    data = msg.encode('ascii')
    s.send(data)
    data = s.recv(bufferSize)
    text = data.decode('ascii')
    print(f"server is saying: {text}")
