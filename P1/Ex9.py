from Seq1 import Seq

s = Seq()
FOLDER = "../Session-04/"
FILENAME = "U5.txt"

print(f"Sequence: (Length: {s.len()}) {s.read_fasta(FOLDER + FILENAME)}")
print(f"  Bases: {s.count()}")
print(f"Reverse: {s.reverse()}")
print(f"Complement: {s.complement()}")