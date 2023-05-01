import socket, threading

#Define the constants we will use in the project
DEST_IP = "130.229.136.91"
DEST_PORT = 12345
ENCODER = "utf-8"
BYTE_SIZE = 1024
IPV4 = socket.AF_INET
TCP = socket.SOCK_STREAM

#Create socket
client_socket = socket.socket(IPV4, TCP)
client_socket.connect((DEST_IP, DEST_PORT))

def send_message():
    while True:
        message = input("")
        client_socket.send(message.encode(ENCODER))

def receive_message():
    while True:
        try:
            message = client_socket.recv(BYTE_SIZE).decode(ENCODER)
            if message == "NAME":
                name = input("What is your username?  ")
                client_socket.send(name.encode(ENCODER))
                send_thread = threading.Thread(target=send_message)
                send_thread.start()
            else:
                print(message)
        except:
            print("An error occured...")
            client_socket.close()
            break

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()