import socket
port = 3000
bufferSize =  65535
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create a socket object
# AF_INET is family of ipv4 ip address
# SOCK_DGRAM means UDP & SOCK_STREAM is TCP

print(s)

hostname = "127.0.0.1"  # ip address for all local machine

s.bind((hostname, port))

print(f"server is live on {s.getsockname()}")

while True:
    data, clientAddress = s.recvfrom(bufferSize)
    msg_received = data.decode('ascii')
    print(f"{clientAddress}:  {msg_received}")
    msg_send = input("reply:  ")
    data = msg_send.encode('ascii')
    s.sendto(data, clientAddress)
