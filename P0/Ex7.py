from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "U5.txt"

print("Frag:", seq_read_fasta(FOLDER + FILENAME)[:20])
print("Complement:", seq_complement(seq_read_fasta(FOLDER + FILENAME)[:20]))