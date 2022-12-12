import socket

sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender.connect(("127.0.0.1",55555))

file = open ("oi.txt", "r")
read_buffer = file.read(1024)

while (read_buffer == True):
    sender.send(read_buffer)
    ler_buffer = file.read(1024)
file.close()