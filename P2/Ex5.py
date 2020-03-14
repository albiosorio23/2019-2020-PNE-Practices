from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

FOLDER = "../Session-04/"
FILENAME = "U5.txt"
# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

s = Seq().read_fasta(FOLDER + FILENAME)

# -- Send the Gene
c.debug_talk(f"Sending ¨{FILENAME} Gene to the server...")
c.debug_talk(str(s))
