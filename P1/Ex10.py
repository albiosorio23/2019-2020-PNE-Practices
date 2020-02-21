from Seq1 import Seq

s = Seq()
FOLDER = "../Session-04/"
list = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN", "RNU6_269P.txt"]
bases = ["A","G", "C", "T"]

for element in list:
    seq = s.read_fasta(FOLDER + element)
    dict_bases = s.count()
    minimum = 0 #Para que se vaya quedando con el menor valor de los que vaya leyendo
    best = ""
    for base, value in dict_bases.items():
        while value > minimum:
            minimum = value
            best = base
    print ("Gene", element,": Most frequent Base:", best)