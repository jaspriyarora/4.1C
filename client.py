import socket

# Define the host and port number
HOST = 'localhost'
PORT = 12345

# Create a socket object and connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Send a 'Hello' message to the server
    s.sendall('Hello'.encode())
    # Receive a response from the server
    data = s.recv(1024)
    # Print the received message
    print('Received message:', data.decode())
    # Prompt the user to enter their name
    name = input('Enter your name: ')
    # Send the user's name to the server
    s.sendall(name.encode())
    # Receive a welcome message from the server
    data = s.recv(1024)
    # Print the received message
    print('Received message:', data.decode())
