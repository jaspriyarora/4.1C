import socket

# Define the host and port number
HOST = 'localhost'
PORT = 12345

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to a specific host and port number
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    # Print a message indicating that the server is listening
    print('Server listening on', (HOST, PORT))
    # Accept an incoming connection
    conn, addr = s.accept()
    # Print a message indicating that a connection has been established
    print('Connected by', addr)
    # Loop to receive and process incoming data from the client
    while True:
        # Receive data from the client
        data = conn.recv(1024)
        # If no data is received, break out of the loop
        if not data:
            break
        # Print the received message
        print('Received message:', data.decode())
        # If the message is 'Hello', send a greeting and ask for the client's name
        if data.decode() == 'Hello':
            conn.sendall('Hello, What’s your name?'.encode())
        # If the message is not 'Hello', assume it is the client's name and send a welcome message
        else:
            name = data.decode()
            print('Client name:', name)
            conn.sendall(f'Hello {name}, Welcome to SIT202'.encode())
