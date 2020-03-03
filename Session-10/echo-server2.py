import socket

import termcolor

IP = "212.128.253.150"
PORT = 8080
# Step 1: creating the socket for comunicating
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Step 3: Convert into a listening socket
ls.listen()

print("Server is configured!")
count_conections = 0
while True:

    try:
        # Step 4: Wait for client to connect
        (cs, client_ip_port) = ls.accept()
        count_conections = count_conections + 1

    except KeyboardInterrupt:
        print("Server is done!")
        ls.close()
        exit()

    else:

        # Step 5: Receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        print(f"CONNECTION {count_conections}. Client IP, PORT: ({IP},{PORT})")
        print("Received message:")
        termcolor.cprint(f"{msg}", "green")
        # termcolor.cprint(f"Received message: {msg}", "green")

        # Step 6: Send a response message to the client
        response = f"ECHO: {msg}\n"

        cs.send(response.encode())
        cs.close()
