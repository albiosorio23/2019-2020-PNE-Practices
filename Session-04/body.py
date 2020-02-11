from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

seq_dna = file_contents
index_finish = seq_dna.find ('\n')
seq_dna = seq_dna[index_finish + 1:]
print (seq_dna)