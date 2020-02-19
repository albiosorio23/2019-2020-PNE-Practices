from Seq0 import *

FOLDER = "../Session-04/"
list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN"]

for gene in list:
  seq = seq_read_fasta(FOLDER + gene)
  print(f"Gene {gene} ---> Length: {seq_len(seq)}")