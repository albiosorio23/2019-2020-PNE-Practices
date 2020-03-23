import socket

import termcolor

IP = "127.0.0.1"  # local machines, asi no tienes que ir cambiando el IP
PORT = 8080
# Step 1: creating the socket for comunicating
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))

# Step 3: Convert into a listening socket
ls.listen()

print("Server is configured!")

list_response = ["AGCGTA", "CTATGC", "GGATCG", "TGTAAA", "GGGTT"]

while True:

    try:
        # Step 4: Wait for client to connect
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server is done!")
        ls.close()
        exit()

    else:

        # Step 5: Receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        # space = msg.split("\n")[0].split(" ")
        # command1 = space[0]
        response = ""
        command2 = msg[1]

        if msg == "PING":
            response = "OK!\n"

        termcolor.cprint("PING command!", "green")
        print(response)

        # for i in range(list_response):
        elif "GET" in msg:
            seq_get = int(msg[msg.find(" ") + 1:]) # Seq_get es el número del 0-4 que introduce en la terminal
            response = list_response[seq_get]

        # Info command
        elif "INFO" in msg:
            

        cs.send(response.encode())
        cs.close()
