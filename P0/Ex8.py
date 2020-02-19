from Seq0 import *

FOLDER = "../Session-04/"
list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN"]
bases = ["A","G", "C", "T"]

for element in list:
    seq = seq_read_fasta(FOLDER + element)
    dict_bases = seq_count(seq)
    minimum = 0 #Para que se vaya quedando con el menor valor de los que vaya leyendo
    best = ""
    for base, value in dict_bases.items(): #
        while value > minimum:
            minimum = value
            best = base
    print ("Gene", element,": Most frequent Base:", best)