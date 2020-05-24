import socket
from Seq1 import Seq
import termcolor

IP = "127.0.0.1"  # local machines, asi no tienes que ir cambiando el IP
PORT = 8080

FOLDER = "../Session-04/"
txt = ".txt"

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
    print("Waiting for clients...")
    try:
        # Step 4: Wait for client to connect
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()

    else:

        # Step 5: Receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        response = ""

        if msg == "PING":
            response = "OK!\n"

        elif "GET" in msg:
            # Para coger solo el número
            seq_get = int(msg[msg.find(" ") + 1:]) # Seq_get es el número del 0-4 que introduce en la terminal
            # Devuelve la secuencia en la posición coorespondiente al nº seq_get
            response = list_response[seq_get]

        # Info command
        elif "INFO" in msg:
            gene_seq = msg[msg.find(" ")+1:] #Secuencia introducida en la terminal

            seq = Seq(gene_seq)
            seq_length = seq.len()

            print("Total length: ", seq_length)
            number_of_A = seq.count_base("A")
            percentage_A = "{:.1f}".format(100 * number_of_A / seq_length)
            number_of_G = seq.count_base("G")
            percentage_G = "{:.1f}".format(100 * number_of_G / seq_length)
            number_of_T = seq.count_base("T")
            percentage_T = "{:.1f}".format(100 * number_of_T / seq_length)
            number_of_C = seq.count_base("C")
            percentage_C = "{:.1f}".format(100 * number_of_C / seq_length)

            response = ("A: " + str(number_of_A)  +  " (" +percentage_A + "%)" + "\n" + "C: "+ str(number_of_C)   +  " (" + percentage_C + "%)" + "\n" + "G: " + str(number_of_G)  + " (" + percentage_G + "%)" + "\n" + "T: " + str(number_of_T)  + " (" + percentage_T + "%)" + "\n")

        elif "COMP" in msg:
            gene_seq = msg[msg.find(" ") + 1:]
            seq = Seq(gene_seq)
            response = seq.complement() + "\n"

        elif "REV" in msg:
            gene_seq = msg[msg.find(" ") + 1:]
            seq = Seq(gene_seq)
            response = seq.reverse() + "\n"

        elif "GENE" in msg:
            gene_name = msg[msg.find(" ") + 1:]
            s = Seq()
            s.read_fasta(FOLDER + gene_name + txt)
            response = str(s) + "\n"

        else:
            termcolor.cprint("Unknown command!!!", 'red')
            response = "Unkwnown command"

        termcolor.cprint(msg[:msg.find(" ")], "green")
        print (response)

        cs.send(response.encode())
        cs.close()
