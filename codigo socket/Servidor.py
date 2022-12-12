import socket
receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver.bind(("127.0.0.1",55555))
receiver.listen(10)

connection = True

while connection:
    sc, address = receiver.accept()    
    file = open("mensagem_recebida.txt",'w')
    end = 0
    while (end == 0):
        read_bffer = sc.recv(1024)
        while (read_bffer):                
                file.write(read_bffer)
                read_bffer = sc.recv(1024)                
                end = 1                 
    file.close()
    sc.close()
receiver.close()