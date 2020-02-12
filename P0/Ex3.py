from Seq0 import *

FOLDER = "../Session-04/"
list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN"]

for gene in list:
  seq = seq_read_fasta(FOLDER + gene)
  lseq = seq_len(seq)
  print(lseq)


print("Gene U5 ---> Length:", seq_len(FOLDER + list[0]), "\nGene ADA ---> Length:", "\nGene FRAT1 ---> Length:")