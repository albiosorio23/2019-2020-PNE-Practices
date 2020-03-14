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

c = Client(IP, PORT)
print(c)

s = Seq().read_fasta(FOLDER + FILENAME)
bases = str(s)

length = 10

print(f"Gene {FILENAME}: {bases}")
c.talk(f"Sending {FILENAME} Gene to the server, in fragments of {length} bases...")

for index in range(5):
    fragment = bases[index * length:(index + 1) * length]

    print(f"Fragment {index + 1}: {fragment}")
    c.talk(f"Fragment {index + 1}: {fragment}")

# -- Send the Gene
c.debug_talk(f"Sending ¨{FILENAME} Gene to the server...")
c.debug_talk(str(s))
