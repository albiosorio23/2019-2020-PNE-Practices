from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

FOLDER = "../Session-04/"
FILENAME = "FRAT1.txt"
# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

c1 = Client(IP, PORT)
c2 = Client(IP, PORT + 1)

print(c1)
print(c2)

s = Seq().read_fasta(FOLDER + FILENAME)
bases = str(s)

length = 10

print(f"Gene {FILENAME}: {bases}")
message = f"Sending {FILENAME} Gene to the server, in fragments of {length} bases..."

c1.talk(message)
c2.talk(message)

for index in range(5):
    fragment = bases[index * length:(index + 1) * length]

    # Client´s console
    print(f"Fragment {index + 1}: {fragment}")

    # Send tto the server
    message2 = f"Fragment {index + 1}: {fragment}"

    if index % 2:
        c2.talk(message2)
    else:
        c1.talk(message2)
