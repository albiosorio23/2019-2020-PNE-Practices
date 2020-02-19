class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created! ")


    def __str__(self):
        return self.strbases


    def len(self):
        return len(self.strbases)

#Main program
sequence_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

def print_seqs(seq_list):
    for seq in seq_list:
        print(f"Sequence {seq_list.index(seq)}: (Length: {seq.len()}) {seq}")

print_seqs(sequence_list)




