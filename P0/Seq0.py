#Ex 1
def seq_ping():
    print("OK!")

from pathlib import Path

#Ex 2
def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    seq_dna = file_contents
    index_finish = seq_dna.find ('\n')
    seq_dna = seq_dna[index_finish + 1:]
    seq_dna = seq_dna.replace("\n","")
    seq_dna = seq_dna[:20]  #Para que vaya hasta la base 20
    return seq_dna
#Ex 3

def seq_len(filename):
    file_contents = Path(filename).read_text()
    seq_dna = file_contents
    index_finish = seq_dna.find('\n')
    seq_dna = seq_dna[index_finish + 1:]
    seq_dna = seq_dna.replace("\n", "")
    return len(seq_dna)



