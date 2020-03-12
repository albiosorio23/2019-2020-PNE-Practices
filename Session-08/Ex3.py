import socket

# SERVER IP, PORT
PORT = 8080
IP = "127.0.0.1"
while True:
    # Ask the user for the message
    message_user = input("Enter a message: ")
    # Create the socket
    # We will always use this parameters: AF_INET y SOCK_STREAM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send data. No strings can be send, only bytes
    # It necesary to encode the string into bytes
    s.send(str.encode(message_user))

    # Close the socket
    s.close()
