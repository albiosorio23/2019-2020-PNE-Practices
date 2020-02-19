from Seq0 import *

FOLDER = "../Session-04/"
list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN"]
bases = ["A","G", "C", "T"]


for element in list:
    seq = seq_read_fasta(FOLDER + element) #Leer las sequencias de la lista
    print ("Genes:", element)
    for i in bases:
        print (i, ":", seq_count_base(seq, i))

