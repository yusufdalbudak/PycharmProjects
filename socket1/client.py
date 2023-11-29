import socket

host = "127.0.0.1"
port = 50002

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
    message = input(">> ")

    if message.lower().strip() == "quit":
        break

    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print("Response from server: " + str(data))

# Döngüden çıktıktan sonra soketi kapat
client_socket.close()

